from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = KeyboardButton('Назад')

back_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

back_kb.add(button)
