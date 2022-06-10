from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('Задачи')
button2 = KeyboardButton('Помощь')
button3 = KeyboardButton('Настройки')

mainMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True)

mainMenu_kb.row(button1, button2).add(button3)
