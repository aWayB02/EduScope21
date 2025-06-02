from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os

load_dotenv("keys.env")


bot = Bot(os.getenv("TOKEN"))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
