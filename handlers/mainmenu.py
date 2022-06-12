from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from start_bot import dp, dialogue
from keyboards.mainmenu_keyboard import mainMenu_kb, mainSettings_kb
from keyboards.goals_keyboard import configure_goal_kb, change_goal_text_kb
from keyboards.back_keyboard import back_kb
from keyboards.tasks_keyboard import tasks_kb
from states.situation import MainMenu, Tasks
from model import users


# TODO use dictionaries instead of if or match case, also make code more readible
# TODO goal = target, term
# TODO move change goal to separate handlers

# Return to main menu from any state
async def return_to_menu(message: types.Message, state: FSMContext):
    await message.answer("Главное меню", reply_markup=mainMenu_kb)
    await MainMenu.main.set()


# Main menu
async def main_menu(message: types.Message, state: FSMContext):
    if message.text == 'Настройки':
        await message.answer(dialogue['mainmenu']['settings'], reply_markup=mainSettings_kb)
        await MainMenu.settings.set()
    if message.text == 'Помощь':
        await message.answer("Помощь")
    if message.text == 'Задачи':
        await message.answer(dialogue['tasks']['main'], reply_markup=tasks_kb)
        await Tasks.main.set()


# Main menu settings
async def main_settings(message: types.Message, state: FSMContext):
    if message.text == "Настроить цель":
        user_id = message.from_user.id

        user = users.get_user(user_id)

        goal_text = user["goal"]["text"]
        goal_term = user["goal"]["term"]
        await message.answer(dialogue['registration']['confirm'].format(goal_text, goal_term), reply_markup=configure_goal_kb)
        await MainMenu.change_goal_settings.set()
    if message.text == "Частота сессий":
        await message.answer("Частота сессий")
    if message.text == "Назад":
        await message.answer("Главное меню", reply_markup=mainMenu_kb)
        await MainMenu.main.set()


# Select change target or term
async def change_goal_setting(message: types.Message, state: FSMContext):
    if message.text == "Изменить цель":
        user_id = message.from_user.id

        user = users.get_user(user_id)

        goal_text = user["goal"]["text"]
        await message.answer(dialogue['mainmenu']['ask_change_goal_text'].format(goal_text), reply_markup=back_kb)
        await MainMenu.change_target.set()
    if message.text == "Изменить срок":
        user_id = message.from_user.id

        user = users.get_user(user_id)

        goal_term = user["goal"]["term"]
        await message.answer(dialogue['mainmenu']['ask_change_goal_term'].format(goal_term), reply_markup=back_kb)
        await MainMenu.change_term.set()
    if message.text == "Назад":
        await message.answer(dialogue['mainmenu']['settings'], reply_markup=mainSettings_kb)
        await MainMenu.settings.set()


# Change target
async def change_goal_text_ask(message: types.message, state: FSMContext):
    if message.text == "Назад":
        user_id = message.from_user.id

        user = users.get_user(user_id)

        goal_text = user["goal"]["text"]
        goal_term = user["goal"]["term"]

        await message.answer(dialogue['registration']['confirm'].format(goal_text, goal_term), reply_markup=configure_goal_kb)
        await MainMenu.change_goal_settings.set()
        return

    user_id = message.from_user.id
    text = message.text

    user = users.edit_user_goal(user_id, goal_text = text)

    goal_text = user["goal"]["text"]
    goal_term = user["goal"]["term"]

    await message.answer(dialogue['registration']['confirm'].format(goal_text, goal_term), reply_markup=configure_goal_kb)
    await MainMenu.change_goal_settings.set()


# Change term
async def change_term_ask(message: types.message, state: FSMContext):
    if message.text == "Назад":
        user_id = message.from_user.id

        user = users.get_user(user_id)

        goal_text = user["goal"]["text"]
        goal_term = user["goal"]["term"]

        await message.answer(dialogue['registration']['confirm'].format(goal_text, goal_term), reply_markup=configure_goal_kb)
        await MainMenu.change_goal_settings.set()
        return

    user_id = message.from_user.id
    text = message.text

    user = users.edit_user_goal(user_id, goal_term = text)

    goal_text = user["goal"]["text"]
    goal_term = user["goal"]["term"]
    
    await message.answer(dialogue['registration']['confirm'].format(goal_text, goal_term), reply_markup=configure_goal_kb)
    await MainMenu.change_goal_settings.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(return_to_menu, Text(equals="Главное меню"), state='*')
    dp.register_message_handler(change_term_ask, state=MainMenu.change_term)
    dp.register_message_handler(change_goal_text_ask, state=MainMenu.change_target)
    dp.register_message_handler(change_goal_setting, state=MainMenu.change_goal_settings)
    dp.register_message_handler(main_settings, state=MainMenu.settings)
    dp.register_message_handler(main_menu, state='*')
