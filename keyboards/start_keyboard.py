from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = KeyboardButton('Создать цель')

start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

start_kb.add(button)
