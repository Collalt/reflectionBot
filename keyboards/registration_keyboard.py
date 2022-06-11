from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Confirm goal
button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Изменить срок')
button3 = KeyboardButton('Продолжить')

reg_confirm_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_confirm_kb.row(button1, button2).add(button3)

# Session interval
button1 = KeyboardButton('EveryDay')
button2 = KeyboardButton('EveryWeek')
button3 = KeyboardButton('Custom')

reg_session_settings_kb = ReplyKeyboardMarkup(resize_keyboard=True)
reg_session_settings_kb.row(button1, button2).add(button3)

# Registration

button = KeyboardButton('Создать цель')

reg_start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_start_kb.add(button)

# Change target

button = KeyboardButton('Изменить цель')

reg_change_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_change_goal_kb.add(button)

# Change term
button = KeyboardButton('Изменить срок')

change_term_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_term_kb.add(button)

