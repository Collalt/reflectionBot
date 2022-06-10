from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from os import getenv

db_uri = 'mongodb+srv://{}:{}@cluster0.2ugr3.mongodb.net/?retryWrites=true&w=majority'.format(getenv('DB_LOGIN'), getenv('DB_PASSWORD'))

bot = Bot(token=getenv('BOT_TOKEN'))
storage = MongoStorage(uri=db_uri)
dp = Dispatcher(bot, storage=storage)
