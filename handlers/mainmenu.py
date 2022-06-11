from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from start_bot import dp, dialogue
from keyboards.mainmenu_settings_keyboard import mainSettings_kb
from keyboards.mainmenu_keyboard import mainMenu_kb
from keyboards.setting_change_goal_keyboard import change_goal_kb
from keyboards.back_keyboard import back_kb
from states.situation import MainMenu
from model import model


# TODO use dictionaries instead of if or match case, also make code more readible
# TODO goal = target, term

# Return to main menu from any state
async def return_to_menu(message: types.Message, state: FSMContext):
    await message.answer("Главное меню", reply_markup=mainMenu_kb)
    await MainMenu.main.set()


async def main_menu(message: types.Message, state: FSMContext):
    if message.text == 'Настройки':
        await message.answer(dialogue['mainmenu']['settings'], reply_markup=mainSettings_kb)
        await MainMenu.settings.set()
    if message.text == 'Помощь':
        await message.answer("Помощь")
    if message.text == 'Задачи':
        await message.answer("Задачи")


async def main_settings(message: types.Message, state: FSMContext):
    if message.text == "Изменить цель":
        user_id = message.from_user.id
        target = model.customers.find_one({"user_id": user_id})["goal"]
        term = model.customers.find_one({"user_id": user_id})["term"]
        await message.answer(dialogue['registration']['confirm'].format(target, term), reply_markup=change_goal_kb)
        await MainMenu.change_goal_settings.set()
    if message.text == "Частота сессий":
        await message.answer("Частота сессий")
    if message.text == "Назад":
        await message.answer("Главное меню", reply_markup=mainMenu_kb)
        await MainMenu.main.set()


async def change_goal_setting(message: types.Message, state: FSMContext):
    if message.text == "Изменить цель":
        user_id = message.from_user.id
        target = model.customers.find_one({"user_id": user_id})["goal"]
        await message.answer(dialogue['mainmenu']['ask_change_goal'].format(target), reply_markup=back_kb)
        await MainMenu.change_target.set()
    if message.text == "Изменить срок":
        user_id = message.from_user.id
        term = model.customers.find_one({"user_id": user_id})["term"]
        await message.answer(dialogue['mainmenu']['ask_change_term'].format(term), reply_markup=back_kb)
        await MainMenu.change_term.set()
    if message.text == "Назад":
        await message.answer(dialogue['mainmenu']['settings'], reply_markup=mainSettings_kb)
        await MainMenu.settings.set()


async def change_goal_ask(message: types.message, state: FSMContext):
    if message.text == "Назад":
        user_id = message.from_user.id
        target = model.customers.find_one({"user_id": user_id})["goal"]
        term = model.customers.find_one({"user_id": user_id})["term"]
        await message.answer(dialogue['registration']['confirm'].format(target, term), reply_markup=change_goal_kb)
        await MainMenu.change_goal_settings.set()
        return

    user_id = message.from_user.id
    text = message.text
    model.customers.update_one({"user_id": user_id}, {"$set": {"goal": text}})
    target = model.customers.find_one({"user_id": user_id})["goal"]
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['registration']['confirm'].format(target, term), reply_markup=change_goal_kb)
    await MainMenu.change_goal_settings.set()


async def change_term_ask(message: types.message, state: FSMContext):
    if message.text == "Назад":
        user_id = message.from_user.id
        goal = model.customers.find_one({"user_id": user_id})["goal"]
        term = model.customers.find_one({"user_id": user_id})["term"]
        await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=change_goal_kb)
        await MainMenu.change_goal_settings.set()
        return

    user_id = message.from_user.id
    text = message.text
    model.customers.update_one({"user_id": user_id}, {"$set": {"term": text}})
    target = model.customers.find_one({"user_id": user_id})["goal"]
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['registration']['confirm'].format(target, term), reply_markup=change_goal_kb)
    await MainMenu.change_goal_settings.set()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(return_to_menu, Text(equals="Главное меню"), state='*')
    dp.register_message_handler(change_term_ask, state=MainMenu.change_term)
    dp.register_message_handler(change_goal_ask, state=MainMenu.change_target)
    dp.register_message_handler(change_goal_setting, state=MainMenu.change_goal_settings)
    dp.register_message_handler(main_settings, state=MainMenu.settings)
    dp.register_message_handler(main_menu, state='*')
