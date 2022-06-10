from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from os import getenv
import json

db_uri = 'mongodb+srv://{}:{}@cluster0.2ugr3.mongodb.net/?retryWrites=true&w=majority'.format(getenv('DB_LOGIN'), getenv('DB_PASSWORD'))

file = open('dialogue.json', 'r', encoding='utf-8')
dialogue = json.load(file)

bot = Bot(token=getenv('BOT_TOKEN'))
storage = MongoStorage(uri=db_uri)
dp = Dispatcher(bot, storage=storage)

file.close()
