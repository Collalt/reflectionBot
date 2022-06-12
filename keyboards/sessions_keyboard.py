from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# Set session interval
# Mon, Tue, Wed, Thu, Fri, Sat, Sun
# Понедельник день бездельник

week_ru = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
week_en = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
               "Декабрь"]

reg_week_kb = InlineKeyboardMarkup(row_width=7)
cb = CallbackData("session_interval", "week_day", "action")

buttons = []
for day in week_ru:
    buttons.append(InlineKeyboardButton(text=day, callback_data=cb.new(week_day=day, action = "-")))
button = InlineKeyboardButton(text="Продолжить", callback_data=cb.new(week_day="-", action = "continue"))
reg_week_kb.add(*buttons).add(button)


mainmenu_week_kb = InlineKeyboardMarkup(row_width=7)
mainmenu_week_kb.add(*buttons)



