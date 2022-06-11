from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Main menu
button1 = KeyboardButton('Задачи')
button2 = KeyboardButton('Помощь')
button3 = KeyboardButton('Настройки')

mainMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu_kb.row(button1, button2).add(button3)

# Main menu settings
button1 = KeyboardButton('Изменить цель')
button2 = KeyboardButton('Частота сессий')
button3 = KeyboardButton('Назад')

mainSettings_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainSettings_kb.row(button1, button2).add(button3)
