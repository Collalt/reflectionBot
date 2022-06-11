from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button1 = KeyboardButton('Добавить задачу')
button2 = KeyboardButton('Удалить задачу')
button3 = KeyboardButton('Назад')

tasks_kb = ReplyKeyboardMarkup(resize_keyboard=True)

tasks_kb.row(button1, button2).add(button3)
