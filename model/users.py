from model import model
import copy
from datetime import datetime

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
  "session_time": None,
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


def edit_user(user_id, goal=None, tasks_list=None, completed_tasks=None, time_zone = None, session_frequency=None, session_time=None, learned_topics=None):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        new_data = copy.deepcopy(User)
        new_data["goal"] = goal or user["goal"]
        new_data["tasks_list"] = tasks_list or user["tasks_list"]
        new_data["completed_tasks"] = completed_tasks or user["completed_tasks"]
        new_data["time_zone"] = time_zone or user["time_zone"]
        new_data["session_frequency"] = session_frequency or user["session_frequency"]
        new_data["session_time"] = session_time or user["session_time"]
        new_data["learned_topics"] = learned_topics or user["learned_topics"]

        users.update_one({"_id": user_id}, {"$set": new_data})
        return users.find_one({"_id": user_id})
    else:
        raise ValueError("User with provided id not found")


def edit_user_goal(user_id, goal_text=None, goal_term=None, term_start=None):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        new_goal_data = { "text": None, "term": None, "term_start": datetime.now()}
        new_goal_data["text"] = goal_text or user["goal"]["text"]
        new_goal_data["term"] = goal_term or user["goal"]["term"]
        new_goal_data["term_start"] = term_start or user["goal"]["term_start"]

        return edit_user(user_id, goal=new_goal_data)
    else:
        raise ValueError("User with provided id not found")


def add_task_user(user_id, task_id):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        new_tasks_list = user["tasks_list"].copy()
        new_tasks_list.append(task_id)

        return edit_user(user_id, tasks_list=new_tasks_list)
    else:
        raise ValueError("User with provided id not found")


def add_completed_task_user(user_id, task_id):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        new_tasks_list = user["completed_tasks"].copy()
        new_tasks_list.append({"_id": task_id, "completion_time": datetime.now()})

        return edit_user(user_id, completed_tasks=new_tasks_list)
    else:
        raise ValueError("User with provided id not found")

def delete_task_user(user_id, task_id):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        new_tasks_list = []

        for id in user["tasks_list"]:
            if id != task_id:
                new_tasks_list.append(id)

        return edit_user(user_id, tasks_list=new_tasks_list)
    else:
        raise ValueError("User with provided id not found")

def add_learned_topic_user(user_id, learned_topic_text = None, learned_topic_status = None):
    if user_id is None:
        raise ValueError("user_id is not provided")

    if learned_topic_text is None or learned_topic_status is None:
        raise ValueError("learned_topic_text or learned_topic_status is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        new_learned_topics = user["learned_topics"]
        new_learned_topics.append({"text": learned_topic_text, "status": learned_topic_status})

        return edit_user(user_id, learned_topics=new_learned_topics)
    else:
        raise ValueError("User with provided id not found")