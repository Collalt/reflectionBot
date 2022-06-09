from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from os import getenv

bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())
