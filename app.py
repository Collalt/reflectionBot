from aiogram.utils import executor
from start_bot import dp
from handlers import common, registration
import logging

logging.basicConfig(level=logging.INFO)

common.register_handlers(dp)

executor.start_polling(dp)
