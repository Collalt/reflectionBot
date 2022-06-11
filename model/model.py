from os import getenv
from pymongo import MongoClient

db_uri = 'mongodb+srv://{}:{}@cluster0.2ugr3.mongodb.net/?retryWrites=true&w=majority'.format(getenv('DB_LOGIN'),
                                                                                              getenv('DB_PASSWORD'))
client = MongoClient(db_uri)

db = client["database"]

customers = db["users"]
users = db['users']


async def get_user(user_id):
    if user_id is None:
        raise ValueError("user_id is not provided")
    return users.find_one({"_id": user_id})


async def add_user(user_id):
    if user_id is None:
        raise ValueError("user_id is not provided")

    return users.insert_one({"_id": user_id})


async def edit_user(user_id, goal=None, term=None):
    if user_id is None:
        raise ValueError("user_id is not provided")

    user = users.find_one({"_id": user_id})

    if user is not None:
        newData = {}
        newData.goal = goal or user.goal
        newData.term = term or user.term

        return users.update_one({"_id": user_id}, {"$set": newData})
    else:
        raise ValueError("User with provided id not found")
