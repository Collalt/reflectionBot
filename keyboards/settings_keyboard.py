from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('EveryDay')
button2 = KeyboardButton('EveryWeek')
button3 = KeyboardButton('Custom')

settings_kb = ReplyKeyboardMarkup(resize_keyboard=True)

settings_kb.row(button1, button2).add(button3)
