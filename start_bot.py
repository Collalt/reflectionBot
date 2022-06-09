from config import TOKEN
from aiogram import Bot, Dispatcher
from os import getenv

bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher(bot)
