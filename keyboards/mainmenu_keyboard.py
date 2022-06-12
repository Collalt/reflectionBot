from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Main menu
button1 = KeyboardButton('Задачи')
button2 = KeyboardButton('Помощь')
button3 = KeyboardButton('Настройки')

mainMenu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu_kb.row(button1, button2).add(button3)

# Main menu settings
button1 = KeyboardButton('Настроить цель')
button2 = KeyboardButton('Частота сессий')
button3 = KeyboardButton('Назад')
button4 = KeyboardButton('Настроить таймзону')

mainSettings_kb = ReplyKeyboardMarkup(resize_keyboard=True)
mainSettings_kb.row(button1, button2, button4).add(button3)
