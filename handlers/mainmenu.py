from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from aiogram.dispatcher.filters import Text
from start_bot import bot, dp, dialogue
from keyboards.mainmenu_settings_keyboard import mainSettings_kb
from keyboards.mainmenu_keyboard import mainMenu_kb
from keyboards.setting_change_goal_keyboard import change_goal_kb
from keyboards.back_keyboard import back_kb
from states.situation import Goal, MainMenu
from model import model


async def main_settings(message: types.Message, state: FSMContext):
    await message.answer(dialogue['mainmenu']['settings'], reply_markup=mainSettings_kb)
    await MainMenu.settings.set()


async def change_goal_setting(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    goal = model.customers.find_one({"user_id": user_id})["goal"]
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=change_goal_kb)
    await MainMenu.change_goal_settings.set()


async def change_goal_ask(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    goal = model.customers.find_one({"user_id": user_id})["goal"]
    await message.answer(dialogue['mainmenu']['ask_change_goal'].format(goal), reply_markup=back_kb)
    await MainMenu.change_goal.set()


async def new_goal_chosen(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    model.customers.update_one({"user_id": user_id}, {"$set": {"goal": text}})
    goal = model.customers.find_one({"user_id": user_id})["goal"]
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=change_goal_kb)
    await MainMenu.main.set()


async def change_term_ask(message: types.message, state: FSMContext):
    user_id = message.from_user.id
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['mainmenu']['ask_change_term'].format(term), reply_markup=back_kb)
    await MainMenu.change_term.set()


async def new_term_chosen(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    text = message.text
    model.customers.update_one({"user_id": user_id}, {"$set": {"term": text}})
    goal = model.customers.find_one({"user_id": user_id})["goal"]
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=change_goal_kb)
    await MainMenu.main.set()


async def back_handler(message: types.Message, state: FSMContext):
    await message.answer(dialogue['common']['cancel'], reply_markup=mainMenu_kb)
    await MainMenu.main.set()
    # TODO send back to previous menu, not main menu


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(back_handler,Text(equals='Назад'), state='*')
    dp.register_message_handler(main_settings, state=MainMenu.main)
    dp.register_message_handler(change_goal_setting, state=MainMenu.settings)
    dp.register_message_handler(change_goal_ask, Text(equals='Изменить цель'), state=MainMenu.change_goal_settings)
    dp.register_message_handler(new_goal_chosen, state=MainMenu.change_goal)
    dp.register_message_handler(change_term_ask, Text(equals='Изменить срок'), state=MainMenu.change_goal_settings)
    dp.register_message_handler(new_term_chosen, state=MainMenu.change_term)


