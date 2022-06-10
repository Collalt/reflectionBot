from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('EveryDay')
button2 = KeyboardButton('EveryWeek')
button3 = KeyboardButton('Custom')

initial_settings_kb = ReplyKeyboardMarkup(resize_keyboard=True)

initial_settings_kb.row(button1, button2).add(button3)
