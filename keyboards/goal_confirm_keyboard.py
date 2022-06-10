from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Изменить срок')
button3 = KeyboardButton('Настройка')

confirm_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

confirm_goal_kb.row(button1, button2).add(button3)
