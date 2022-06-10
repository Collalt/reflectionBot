from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Частота сессий')
button3 = KeyboardButton('Назад')

mainSettings_kb = ReplyKeyboardMarkup(resize_keyboard=True)

mainSettings_kb.row(button1, button2).add(button3)
