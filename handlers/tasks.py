from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from start_bot import dp, dialogue
from keyboards.mainmenu_keyboard import mainMenu_kb
from states.state import MainMenu, Tasks
from model import model


async def tasks_main(message: types.Message, state: FSMContext):
    if message.text == 'Удалить задачу':
        await message.answer("Удалить")
    if message.text == 'Добавить задачу':
        await message.answer("Добавить")
    if message.text == 'Назад':
        await message.answer("Главное меню", reply_markup=mainMenu_kb)
        await MainMenu.main.set()

dp.register_message_handler(tasks_main, state=Tasks.main)

