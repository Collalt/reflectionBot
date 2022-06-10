from dotenv import load_dotenv
load_dotenv()

from aiogram.utils import executor
from start_bot import dp
from handlers import common, registration
from model import model
import logging


logging.basicConfig(level=logging.INFO)

common.register_handlers(dp)
registration.register_handlers(dp)

executor.start_polling(dp)