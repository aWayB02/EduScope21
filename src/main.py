import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from api.clusters import get_cluster
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from api.participant import get_participant_login

bot = Bot(token="7696341778:AAFr1VqDVfIKTqsvp6nguvQpFGjSnpDDjZk")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Кластеры", callback_data="open_cluster")],
            [InlineKeyboardButton(text="Найти пользователя", callback_data="get_user")],
        ]
    )


class GetUserInput(StatesGroup):
    waiting_for_text = State()


def cluster():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Denal", callback_data="cluster:D")],
            [InlineKeyboardButton(text="Ezdel", callback_data="cluster:E")],
            [InlineKeyboardButton(text="Sabar", callback_data="cluster:S")],
            [InlineKeyboardButton(text="Tesham", callback_data="cluster:T")],
            [InlineKeyboardButton(text="Назад", callback_data="back")],
        ]
    )


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Peer to Peer {message.from_user.first_name}!", reply_markup=main_menu()
    )


@dp.message(GetUserInput.waiting_for_text)
async def get_user_info(message: types.Message, state: FSMContext):
    login = message.text
    ans = await get_participant_login(login)
    await message.answer((str(ans)))
    await state.clear()


@dp.callback_query(F.data == "get_user")
async def get_name_user(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, введите имя пира:")
    await state.set_state(GetUserInput.waiting_for_text)
    await callback.answer()


@dp.callback_query(F.data == "open_cluster")
async def get_open_cluster(callback: CallbackQuery):
    await callback.message.answer("Выберите кластер:", reply_markup=cluster())
    await callback.answer()


@dp.callback_query(F.data.startswith("cluster:"))
async def get_cluster_info(callback: CallbackQuery):
    name = callback.data.split(":")[-1]
    names_clusters = {"D": "Denal", "E": "Ezdel", "S": "Sabar", "T": "Tesham"}
    info = await get_cluster(names_clusters[name])
    total_places, free_places, occupied_places = info
    await callback.message.answer(
        f"Кластер <b>{names_clusters[name]}</b>\n"
        f"всего мест: <b>{total_places}</b>\n"
        f"свободных мест: <b>{free_places}</b>\n"
        f"занятых мест: <b>{occupied_places}</b>",
        parse_mode="HTML",
        reply_markup=cluster(),
    )
    await callback.answer()


@dp.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer(f"Главное меню:", reply_markup=main_menu())
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
