from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Main menu change goal
button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Изменить срок')
button3 = KeyboardButton('Назад')

# TODO change name of keyboard
change_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_goal_kb.row(button1, button2).add(button3)

# Registration change term
button = KeyboardButton('Изменить цель')

change_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_goal_kb.add(button)

# Registration change term
button = KeyboardButton('Изменить срок')

change_term_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_term_kb.add(button)
