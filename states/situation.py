from aiogram.dispatcher.filters.state import State, StatesGroup


class Goal(StatesGroup):
    waiting_for_goal = State()
    waiting_for_term = State()


class Task(StatesGroup):
    waiting_for_task = State()

# class DayReflection(StatesGroup):


# class WeekReflection(StatesGroup):
