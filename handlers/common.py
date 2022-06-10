from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State
from start_bot import bot, dp, dialogue
from emoji import emojize
from states.situation import Goal


async def start_command_handler(message: types.message):
    # TODO check if user exist in DataBase
    await message.answer(emojize(dialogue['common']['start']['text']))
    await Goal.waiting_for_goal.set()


async def help_command_handler(message: types.message):
    await message.answer(dialogue['common']['help']['text'])


async def cancel_command_handler(message: types.message, state: FSMContext):
    await message.answer(dialogue['common']['cancel']['text'])
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    message.reply("Canceled")


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command_handler, commands=['start'])
    dp.register_message_handler(help_command_handler, commands=['help'], state='*')
    dp.register_message_handler(cancel_command_handler, commands=['cancel'], state='*')
