from aiogram.dispatcher.filters.state import State, StatesGroup, StatesGroupMeta


class Goal(StatesGroup):
    waiting_for_goal = State()
    waiting_for_term = State()
    waiting_for_confirm = State()
    waiting_for_preferences = State()


class MainMenu(StatesGroup):
    main = State()
    settings = State()
    change_goal_settings = State()
    change_target = State()
    change_term = State()
    help = State()


class Tasks(StatesGroup):
    main = State()
    add = State()
    delete = State()

# class DayReflection(StatesGroup):


# class WeekReflection(StatesGroup):
