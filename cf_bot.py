from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import main
import os
main.load_dotenv(".env")
storage = MemoryStorage()
bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher(bot)