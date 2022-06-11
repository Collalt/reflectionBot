from aiogram import types, Dispatcher
from start_bot import dialogue
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from states.situation import Goal, MainMenu
from keyboards.mainmenu_keyboard import mainMenu_kb
from keyboards.registration_keyboard import reg_confirm_kb, reg_change_goal_kb, reg_session_settings_kb
from model import users

# TODO refactor as mainmenu


async def registration_choose_goal(message: types.message):
    user_id = message.from_user.id
    if ((users.get_user(user_id)) is None):
        users.add_user(user_id)
    if message.text == 'Создать цель':
        await message.answer(dialogue['registration']['goal'], reply_markup=types.ReplyKeyboardRemove())
        await Goal.waiting_for_goal.set()


async def change_goal(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['goal'], reply_markup=types.ReplyKeyboardRemove())
    await Goal.waiting_for_goal.set()
    # TODO make separate menu for changing


async def change_term(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['term'], reply_markup=types.ReplyKeyboardRemove())
    await Goal.waiting_for_term.set()
    # TODO make separate menu for changing


async def goal_chosen(message: types.message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    users.edit_user_goal(user_id, goal_text=text)
    await message.answer(dialogue['registration']['term'], reply_markup=reg_change_goal_kb)
    await Goal.next()


async def term_chosen(message: types.message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    
    user = users.edit_user_goal(user_id, goal_term=text)

    goal = user["goal"]["text"]
    term = user["goal"]["term"]

    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=reg_confirm_kb)
    await Goal.next()


async def goal_confirm(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['preferences'], reply_markup=reg_session_settings_kb)
    await Goal.next()


async def set_up_preferences(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['done'], reply_markup=mainMenu_kb)
    await state.finish()
    await MainMenu.main.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration_choose_goal, Text(equals='Создать цель'))
    dp.register_message_handler(change_goal, Text(equals='Изменить цель'), state=(Goal.waiting_for_term, Goal.waiting_for_confirm))
    dp.register_message_handler(change_term, Text(equals='Изменить срок'), state=Goal.waiting_for_confirm)
    dp.register_message_handler(goal_chosen, state=Goal.waiting_for_goal)
    dp.register_message_handler(term_chosen, state=Goal.waiting_for_term)
    dp.register_message_handler(goal_confirm, state=Goal.waiting_for_confirm)
    dp.register_message_handler(set_up_preferences, state=Goal.waiting_for_preferences)
