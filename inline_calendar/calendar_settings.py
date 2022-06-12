from inline_calendar.inline_calendar import InlineCalendar
import datetime

inline_calendar = InlineCalendar()
week_ru = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
               "Декабрь"]

inline_calendar.init(datetime.date.today(),
                     min_date=datetime.date.today(),
                     max_date=datetime.date.today() + datetime.timedelta(weeks=9999),
                     month_names=month_names,
                     days_names=week_ru)