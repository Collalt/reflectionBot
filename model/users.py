from model import model
import copy

users = model.db['users']

User = {
  "goal": {
    "text": None,
    "term": None,
    "term_start": None,
  },
  "tasks_list": [],
  "completed_tasks": [],
  "session_frequency": [],
  "time_zone": None,
  "learned_topics": []
}


def get_user(user_id):
    if user_id is None:
        raise ValueError("user_id is not provided")
        
    return users.find_one({"_id": user_id})


def add_user(user_id):
    if user_id is None:
        raise ValueError("user_id is not provided")

    newUser = copy.deepcopy(User)
    newUser["_id"] = user_id

    users.insert_one(newUser)

    return users.find_one({"_id": user_id})


def edit_user(user_id, goal=None, tasks=None):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        newData = copy.deepcopy(User)
        newData["goal"] = goal or user["goal"]
        newData["tasks_list"] = tasks or user["tasks_list"]

        users.update_one({"_id": user_id}, {"$set": newData})
        return users.find_one({"_id": user_id})
    else:
        raise ValueError("User with provided id not found")


def edit_user_goal(user_id, goal_text=None, goal_term=None):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        newGoalData = { "text": None, "term": None}
        newGoalData["text"] = goal_text or user["goal"]["text"]
        newGoalData["term"] = goal_term or user["goal"]["term"]

        return edit_user(user_id, goal=newGoalData)
    else:
        raise ValueError("User with provided id not found")