from aiogram.dispatcher.filters.state import State, StatesGroup


class Goal(StatesGroup):
    waiting_for_goal = State()
    waiting_for_term = State()
    waiting_for_confirm = State()
    waiting_for_preferences = State()


class MainMenu(StatesGroup):
    main = State()
    settings = State()
    change_goal_settings = State()
    change_goal = State()
    change_term = State()
    help = State()

class Task(StatesGroup):
    waiting_for_task = State()

# class DayReflection(StatesGroup):


# class WeekReflection(StatesGroup):
