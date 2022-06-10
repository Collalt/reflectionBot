from aiogram import types, Dispatcher
from start_bot import bot, dp
from aiogram.dispatcher import FSMContext
from states.situation import Goal
from keyboards.settings_keyboard import settings_kb


async def set_up_goal(message: types.message, state: FSMContext):
    # TODO save goal to database
    await message.answer('Great goal \n Now set up term')
    await Goal.next()


async def set_up_term(message: types.message, state: FSMContext):
    # TODO edit goal, term before continue
    await message.answer('Nice, configure preferences before we continue', reply_markup=settings_kb)
    await Goal.next()


async def set_up_preferences(message: types.message, state: FSMContext):
    await message.answer('Changed', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(set_up_goal, state=Goal.waiting_for_goal)
    dp.register_message_handler(set_up_term, state=Goal.waiting_for_term)
    dp.register_message_handler(set_up_preferences, state=Goal.waiting_for_preferences)
