from os import getenv
import pymongo
from pymongo import MongoClient

db_uri = 'mongodb+srv://{}:{}@cluster0.2ugr3.mongodb.net/?retryWrites=true&w=majority'.format(getenv('DB_LOGIN'), getenv('DB_PASSWORD'))
client = MongoClient(db_uri)

db = client["database"]

customers = db["customers"]