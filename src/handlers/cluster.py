from aiogram import Router
from .dispatcher import dp
from aiogram import F
from aiogram.types import (
    CallbackQuery,
)
from handlers.buttons import cluster
from api.clusters import get_cluster
from handlers.buttons import main_menu

router = Router()


names_clusters = {
    "D": ("Denal", 3),
    "E": ("Ezdel", 2),
    "S": ("Sabar", 3),
    "T": ("Tesham", 2),
}


@router.callback_query(F.data == "open_cluster")
async def get_open_cluster(callback: CallbackQuery):
    await callback.message.answer("Выберите кластер:", reply_markup=cluster())
    await callback.answer()


@router.callback_query(F.data.startswith("cluster:"))
async def get_cluster_info(callback: CallbackQuery):
    name = callback.data.split(":")[-1]
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


dp.include_router(router)
