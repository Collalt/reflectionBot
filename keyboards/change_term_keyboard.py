from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button = KeyboardButton('Изменить срок')

change_term_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

change_term_kb.add(button)
