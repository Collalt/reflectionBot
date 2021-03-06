from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Main menu change goal
button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Изменить срок')
button3 = KeyboardButton('Назад')

# TODO change name of keyboard
configure_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
configure_goal_kb.row(button1, button2).add(button3)

# Change term
button = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Назад')

change_goal_text_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_goal_text_kb.add(button).add(button2)

# Change term
button = KeyboardButton('Изменить срок')
button2 = KeyboardButton('Назад')

change_term_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_term_kb.add(button).add(button2)
