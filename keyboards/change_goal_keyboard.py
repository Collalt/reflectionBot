from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = KeyboardButton('Изменить цель')

change_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

change_goal_kb.add(button)
