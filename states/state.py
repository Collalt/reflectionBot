from aiogram.dispatcher.filters.state import State, StatesGroup, StatesGroupMeta


class Registration(StatesGroup):
    create_goal = State()
    waiting_for_goal_text = State()
    waiting_for_goal_term = State()
    waiting_for_confirm = State()
    waiting_for_preferences = State()
    waiting_for_goal_text_change = State()
    waiting_for_goal_term_change = State()
    waiting_for_customize_session = State()
    waiting_for_timezone = State()

class MainMenu(StatesGroup):
    main = State()
    settings = State()
    change_goal_settings = State()
    change_target = State()
    change_term = State()
    help = State()
    customize_session = State()
    customize_timezone = State()


class Tasks(StatesGroup):
    main = State()
    add = State()
    delete = State()

# class DayReflection(StatesGroup):


# class WeekReflection(StatesGroup):
