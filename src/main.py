import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.types import (
    CallbackQuery,
    Message,
)
from api.clusters import get_cluster
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from api.participant import get_participant_info

from buttons import main_menu, cluster

bot = Bot(token="7696341778:AAFr1VqDVfIKTqsvp6nguvQpFGjSnpDDjZk")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


class GetUserInput(StatesGroup):
    waiting_for_text = State()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Peer to Peer {message.from_user.first_name}! 🍐", reply_markup=main_menu()
    )


@dp.message(GetUserInput.waiting_for_text)
async def get_user_info(message: types.Message, state: FSMContext):
    login = message.text.lower()
    data = await get_participant_info(login)
    if not data:
        await message.answer("Пользователь не найден:(", reply_markup=main_menu())
        await state.clear()
        return
    login, className, parallelName = (
        data["login"],
        data["className"],
        data["parallelName"],
    )
    expValue, level, expToNextLevel = (
        data["expValue"],
        data["level"],
        data["expToNextLevel"],
    )
    coalitionName, rank, coins = data["name"], data["rank"], data["coins"]
    if "active" in data:
        await message.answer(
            f"Логин: <b>{login} 👤</b>\n"
            f"Поток: <b>{className}</b>\n"
            f"Cтатус обучения: <b>{parallelName}</b> ✅\n"
            f"Xp: <b>{expValue}</b>\n"
            f"Level: <b>{level}</b> 📈\n"
            f"XpToNextLevel: <b>{expToNextLevel}</b>\n"
            f"Coins: <b>{coins}</b> 💸\n"
            f"Трайб: <b>{coalitionName}</b>\n"
            f"Место в трайбе: <b>{rank}</b> 📊\n"
            f"Локация: Отсутствует в кампусе❌",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        await state.clear()
        return
    clusterName = data["clusterName"]
    row = data["row"]
    number = data["number"]
    await message.answer(
        f"Логин: <b>{login} 👤</b>\n"
        f"Поток: <b>{className}</b>\n"
        f"Cтатус обучения: <b>{parallelName}</b> ✅\n"
        f"Xp: <b>{expValue}</b>\n"
        f"Level: <b>{level}</b> 📈\n"
        f"XpToNextLevel: <b>{expToNextLevel}</b>\n"
        f"Coins: <b>{coins}</b> 💸\n"
        f"Трайб: <b>{coalitionName}</b>\n"
        f"Место в трайбе: <b>{rank}</b> 📊\n"
        f"Локация: <b>{clusterName} | ряд {row} | Место {number}</b>\n",
        parse_mode="HTML",
        reply_markup=main_menu(),
    )
    await state.clear()


@dp.message(F.text)
async def is_no_valid_input(message: Message):
    await message.answer_sticker(
        "CAACAgIAAxkBAAIBmmgzbIEOenYtcwzYNbCPPI35g_RZAAIldQACtRZ4STRZWNqBgPpLNgQ"
    )


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
    names_clusters = {
        "D": ("Denal", 3),
        "E": ("Ezdel", 2),
        "S": ("Sabar", 3),
        "T": ("Tesham", 2),
    }
    data = await get_cluster(names_clusters[name][0])
    total_places, free_places, occupied_places = data
    await callback.message.answer(
        f"Кластер: <b>{names_clusters[name][0]} | Этаж: {names_clusters[name][1]}</b>\n"
        f"Рабочих станций всего: <b>{total_places} 🟢</b>\n"
        f"Доступные станции: <b>{free_places} 🆓</b>\n"
        f"Используемые станции: <b>{occupied_places} 🧑🏻‍💻</b>",
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
