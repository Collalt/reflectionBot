from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('Task')
button2 = KeyboardButton('Help')
button3 = KeyboardButton('Settings')

mainMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True)

mainMenu_kb.row(button1, button2).add(button3)
