import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from api.clusters import get_cluster
from api.participant import get_participant_login, get_participant_workstation

bot = Bot(token="7696341778:AAFr1VqDVfIKTqsvp6nguvQpFGjSnpDDjZk")
dp = Dispatcher()


# def main_menu():
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="Кластеры", callback_data="open_cluster")],
#         ]
#     )


# def cluster():
#     return InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text="Denal", callback_data="Denal")],
#             [InlineKeyboardButton(text="Ezdel", callback_data="Ezdel")],
#             [InlineKeyboardButton(text="Sabar", callback_data="Sabar")],
#             [InlineKeyboardButton(text="Tesham", callback_data="Tesham")],
#         ]
#     )


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    res = await get_participant_workstation("dariogen")
    await message.answer(str(res))


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
