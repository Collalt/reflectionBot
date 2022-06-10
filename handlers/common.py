from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from start_bot import bot, dp, dialogue
from keyboards.start_keyboard import start_kb


async def start_command_handler(message: types.message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    await message.answer(dialogue['common']['start'], reply_markup=start_kb)


async def help_command_handler(message: types.message):
    await message.answer(dialogue['common']['help'])


async def cancel_command_handler(message: types.message, state: FSMContext):
    await message.answer(dialogue['common']['cancel'])
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command_handler, commands=['start'], state='*')
    dp.register_message_handler(help_command_handler, commands=['help'], state='*')
    dp.register_message_handler(cancel_command_handler, commands=['cancel'], state='*')
