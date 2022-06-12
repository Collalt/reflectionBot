from aiogram import types, Dispatcher
from start_bot import dialogue
from aiogram.dispatcher import FSMContext
from states.state import Registration, MainMenu
from keyboards.mainmenu_keyboard import mainMenu_kb
from keyboards.registration_keyboard import reg_confirm_kb, reg_session_settings_kb
from model import users


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

    await message.answer(dialogue['registration']['term'])
    await Registration.waiting_for_goal_term.set()


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
        goal_term = user["goal"]["term"]
        await message.answer(dialogue['registration']['ask_change_goal_term'].format(goal_term))
        await Registration.waiting_for_goal_term_change.set()
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
    if message.text == "EveryDay":
        await message.answer(dialogue['registration']['done'], reply_markup=mainMenu_kb)
        await MainMenu.main.set()
    if message.text == "EveryWeek":
        await message.answer(dialogue['registration']['done'], reply_markup=mainMenu_kb)
        await MainMenu.main.set()
    if message.text == "Custom":
        await message.answer(dialogue['registration']['done'], reply_markup=mainMenu_kb)
        await MainMenu.main.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(registration_stage_one, state=Registration.create_goal)
    dp.register_message_handler(registration_stage_two, state=Registration.waiting_for_goal_text)
    dp.register_message_handler(registration_confirmation_ask, state=Registration.waiting_for_goal_term)
    dp.register_message_handler(registration_confirmation, state=Registration.waiting_for_confirm)
    dp.register_message_handler(change_goal_text, state=Registration.waiting_for_goal_text_change)
    dp.register_message_handler(change_goal_term, state=Registration.waiting_for_goal_term_change)
    dp.register_message_handler(registration_preferences, state=Registration.waiting_for_preferences)
