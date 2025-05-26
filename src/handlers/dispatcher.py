from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token="7696341778:AAFr1VqDVfIKTqsvp6nguvQpFGjSnpDDjZk")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
