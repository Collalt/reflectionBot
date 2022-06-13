from aiogram import types, Dispatcher
from start_bot import dialogue, bot, dp
from aiogram.dispatcher import FSMContext
from states.state import Registration, MainMenu
from keyboards.mainmenu_keyboard import mainMenu_kb
from keyboards.registration_keyboard import reg_confirm_kb, reg_session_settings_kb
from keyboards.sessions_keyboard import reg_week_kb, cb
from inline_calendar.inline_calendar import InlineCalendar
from inline_calendar.calendar_settings import week_ru, month_names
from contextlib import suppress
from aiogram.utils.exceptions import MessageNotModified
import datetime

from model import users

inline_calendar = InlineCalendar()


# Start user registration, ask for goal
async def registration_stage_one(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    if (users.get_user(user_id)) is None:
        users.add_user(user_id)
    if message.text == 'Создать цель':
        await message.answer(dialogue['registration']['goal'], reply_markup=types.ReplyKeyboardRemove())
        await Registration.waiting_for_goal_text.set()


# Save user goal text and ask goal term
async def registration_stage_two(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    users.edit_user_goal(user_id, goal_text=message.text)

    inline_calendar.init(
        base_date=datetime.date.today(),
        min_date=datetime.date.today(),
        max_date=datetime.date.today() + datetime.timedelta(weeks=9999),
        month_names=month_names,
        days_names=week_ru)

    await message.answer("Выберите дату используя календарь", reply_markup=inline_calendar.get_keyboard())
    await Registration.waiting_for_goal_term.set()


@dp.callback_query_handler(inline_calendar.filter(), state=Registration.waiting_for_goal_term)
async def calendar_callback_handler(q: types.CallbackQuery, callback_data: dict, state: FSMContext):
    with suppress(MessageNotModified):
        await bot.answer_callback_query(q.id)
        user_id = q.from_user.id

        return_data = inline_calendar.handle_callback(q.from_user.id, callback_data)

        if return_data is not None:
            users.edit_user_goal(user_id, goal_term=str(return_data))

        user = users.get_user(user_id)
        goal = user["goal"]["text"]
        term = user["goal"]["term"]

        if callback_data["action"] == "CONTINUE" and term is not None:

            await bot.send_message(user_id,dialogue['registration']['confirm'].format(goal, term),
                                   reply_markup=reg_confirm_kb)
            await Registration.waiting_for_confirm.set()

        if return_data is None:
            await bot.edit_message_reply_markup(chat_id=q.from_user.id, message_id=q.message.message_id,
                                                reply_markup=inline_calendar.get_keyboard(q.from_user.id))
        else:
            picked_data = return_data
            await bot.edit_message_text(text=picked_data, chat_id=q.from_user.id, message_id=q.message.message_id,
                                        reply_markup=inline_calendar.get_keyboard())


async def registration_confirmation_ask(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    users.edit_user_goal(user_id, goal_term=message.text)

    user = users.get_user(user_id)
    goal = user["goal"]["text"]
    term = user["goal"]["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=reg_confirm_kb)
    await Registration.waiting_for_confirm.set()


# Change goal, term or continue registration
async def registration_confirmation(message: types.message, state: FSMContext):
    user_id = message.from_user.id

    user = users.get_user(user_id)

    goal = user["goal"]["text"]
    term = user["goal"]["term"]

    if message.text == "Изменить цель":
        goal_text = user["goal"]["text"]
        await message.answer(dialogue['registration']['ask_change_goal_text'].format(goal_text))
        await Registration.waiting_for_goal_text_change.set()
        return

    if message.text == "Изменить срок":

        inline_calendar.init(
            base_date=datetime.date.today(),
            min_date=datetime.date.today(),
            max_date=datetime.date.today() + datetime.timedelta(weeks=9999),
            month_names=month_names,
            days_names=week_ru)

        goal_term = user["goal"]["term"]

        await message.answer("Ваш срок{}".format(goal_term), reply_markup=inline_calendar.get_keyboard())
        await Registration.waiting_for_goal_term.set()
        return

    if message.text == "Продолжить":
        await message.answer(dialogue['registration']['preferences'], reply_markup=reg_session_settings_kb)
        await Registration.waiting_for_preferences.set()


async def change_goal_text(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    users.edit_user_goal(user_id, goal_text=message.text)
    user = users.get_user(user_id)
    goal = user["goal"]["text"]
    term = user["goal"]["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=reg_confirm_kb)
    await Registration.waiting_for_confirm.set()


async def change_goal_term(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    users.edit_user_goal(user_id, goal_term=message.text)
    user = users.get_user(user_id)
    goal = user["goal"]["text"]
    term = user["goal"]["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=reg_confirm_kb)
    await Registration.waiting_for_confirm.set()


# Set up timezone and session interval
async def registration_preferences(message: types.message, state: FSMContext):
    if message.text == "Каждый день":
        user_id = message.from_user.id
        users.edit_user(user_id, session_frequency='Сб')
        await message.answer(dialogue["registration"]["timezone"], reply_markup=types.ReplyKeyboardRemove())
        await Registration.waiting_for_timezone.set()
    if message.text == "Каждую неделю":
        user_id = message.from_user.id
        users.edit_user(user_id, session_frequency=week_ru)
        await message.answer(dialogue["registration"]["timezone"], reply_markup=types.ReplyKeyboardRemove())
        await Registration.waiting_for_timezone.set()
    if message.text == "Своя настройка":
        await message.answer("Опа па па", reply_markup=reg_week_kb)
        await Registration.waiting_for_customize_session.set()


async def registration_ask_timezone(message: types.Message, state: FSMContext):
# TODO regex
    timezone = message.text

    user_id = message.from_user.id
    users.edit_user(user_id, time_zone=timezone)
    await message.answer(dialogue['registration']['done'], reply_markup=mainMenu_kb)
    await MainMenu.main.set()


setup = []
@dp.callback_query_handler(cb.filter(week_day=week_ru), state=Registration.waiting_for_customize_session)
async def callbacks_session_setup(call: types.CallbackQuery, callback_data: dict):
    data = callback_data["week_day"]
    if data in setup:
        setup.remove(data)
    else:
        setup.append(data)

    sorted_frequency = []

    for day in week_ru:
        if day in setup:
            sorted_frequency.append(day)

    ans = ' '.join(map(str, sorted_frequency))
    await call.message.edit_text(text="Ваше сообщение "+ ans, reply_markup=reg_week_kb)
    await call.answer()


@dp.callback_query_handler(cb.filter(action='continue'), state=Registration.waiting_for_customize_session)
async def callbacks_session_setup_finish(call: types.CallbackQuery, callback_data: dict):
    user_id = call.from_user.id
    users.edit_user(user_id, session_frequency=setup)
    await call.message.answer(dialogue["registration"]["timezone"], reply_markup=types.ReplyKeyboardRemove())
    await Registration.waiting_for_timezone.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration_stage_one, state=Registration.create_goal)
    dp.register_message_handler(registration_stage_two, state=Registration.waiting_for_goal_text)
    dp.register_message_handler(registration_confirmation_ask, state=Registration.waiting_for_goal_term)
    dp.register_message_handler(registration_confirmation, state=Registration.waiting_for_confirm)
    dp.register_message_handler(change_goal_text, state=Registration.waiting_for_goal_text_change)
    dp.register_message_handler(change_goal_term, state=Registration.waiting_for_goal_term_change)
    dp.register_message_handler(registration_preferences, state=Registration.waiting_for_preferences)
    dp.register_message_handler(registration_ask_timezone, state=Registration.waiting_for_timezone)
