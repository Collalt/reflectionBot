from aiogram import types, Dispatcher
from start_bot import bot, dp, dialogue
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from states.situation import Goal
from keyboards.settings_keyboard import settings_kb
from keyboards.change_goal_keyboard import change_goal_kb
from keyboards.mainmenu_keyboard import mainMenu_kb
from keyboards.goal_confirm_keyboard import confirm_goal_kb
from keyboards.change_term_keyboard import change_term_kb
from model import model


async def create_goal_button(message: types.message):
    user_id = message.from_user.id
    # if model.customers.find_one({"user_id": user_id}):
    #     return
    model.customers.insert_one({"user_id": user_id})
    await message.answer(dialogue['registration']['goal'], reply_markup=types.ReplyKeyboardRemove())
    await Goal.waiting_for_goal.set()


async def change_goal(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['goal'], reply_markup=types.ReplyKeyboardRemove())
    await Goal.waiting_for_goal.set()


async def change_term(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['term'], reply_markup=types.ReplyKeyboardRemove())
    await Goal.waiting_for_term.set()


async def set_up_goal(message: types.message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    model.customers.update_one({"user_id": user_id}, {"$set": {"goal": text}})
    await message.answer(dialogue['registration']['term'], reply_markup=change_goal_kb)
    await Goal.next()


async def set_up_term(message: types.message, state: FSMContext):
    text = message.text
    user_id = message.from_user.id
    model.customers.update_one({"user_id": user_id}, {"$set": {"term": text}})
    goal = model.customers.find_one({"user_id": user_id})["goal"]
    term = model.customers.find_one({"user_id": user_id})["term"]
    await message.answer(dialogue['registration']['confirm'].format(goal, term), reply_markup=confirm_goal_kb)
    await Goal.next()


async def goal_confirm(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['preferences'], reply_markup=settings_kb)
    await Goal.next()


async def set_up_preferences(message: types.message, state: FSMContext):
    await message.answer(dialogue['registration']['done'], reply_markup=mainMenu_kb)
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(create_goal_button, Text(equals='Создать цель'))
    dp.register_message_handler(change_goal, Text(equals='Изменить цель'), state=(Goal.waiting_for_term, Goal.waiting_for_confirm))
    dp.register_message_handler(change_term, Text(equals='Изменить срок'), state=Goal.waiting_for_confirm)
    dp.register_message_handler(set_up_goal, state=Goal.waiting_for_goal)
    dp.register_message_handler(set_up_term, state=Goal.waiting_for_term)
    dp.register_message_handler(goal_confirm, state=Goal.waiting_for_confirm)
    dp.register_message_handler(set_up_preferences, state=Goal.waiting_for_preferences)
