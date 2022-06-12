from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from inline_calendar.inline_calendar import InlineCalendar
import datetime



# Confirm goal
button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Изменить срок')
button3 = KeyboardButton('Продолжить')

reg_confirm_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_confirm_kb.row(button1, button2).add(button3)

# Session interval
button1 = KeyboardButton('Каждый день')
button2 = KeyboardButton('Каждую неделю')
button3 = KeyboardButton('Своя настройка')

reg_session_settings_kb = ReplyKeyboardMarkup(resize_keyboard=True)
reg_session_settings_kb.row(button1, button2).add(button3)

# Registration

button = KeyboardButton('Создать цель')

reg_start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_start_kb.add(button)

# Registration change goal_text

button = KeyboardButton('Изменить цель')

reg_change_goal_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
reg_change_goal_kb.add(button)

# Registration change term
button = KeyboardButton('Изменить срок')

change_term_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
change_term_kb.add(button)

reg_choose_term = ReplyKeyboardMarkup(resize_keyboard=True)


button = "Продолжить"

reg_choose_term.add(button)

