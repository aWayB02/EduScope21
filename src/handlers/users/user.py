from aiogram import Router
from aiogram import types
from buttons.b import main_menu
from aiogram import types, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from ..dispatcher import dp
from .utils import send_info_participant, training_status, not_found_user
from redis_service.cache import save_user_to_redis, get_user_from_redis
from handlers import dispatcher
from redis.asyncio import Redis
from core.events import get_events

router = Router()


class GetUserInput(StatesGroup):
    waiting_for_text = State()


@router.message(GetUserInput.waiting_for_text)
async def get_user_info(message: types.Message, state: FSMContext):
    db: Redis = dispatcher.db
    login = message.text.lower()
    data = await get_user_from_redis(login, db)
    if not data:
        data = await save_user_to_redis(login, db)
    if not data:
        await not_found_user(message)
    else:
        await send_info_participant(
            training_status(data["parallelName"]), message, data
        )
    await state.clear()


@router.message(F.text)
async def is_no_valid_input(message: Message):
    await message.answer_sticker(
        "CAACAgIAAxkBAAIBmmgzbIEOenYtcwzYNbCPPI35g_RZAAIldQACtRZ4STRZWNqBgPpLNgQ",
        reply_markup=main_menu(),
    )


@router.callback_query(F.data == "get_user")
async def get_name_user(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, введите имя пира:")
    await state.set_state(GetUserInput.waiting_for_text)
    await callback.answer()


@router.callback_query(F.data == "events")
async def events(callback: CallbackQuery):
    text = await get_events()
    if not text:
        await callback.message.answer(
            "В ближайшее время мероприятий нет. Следите за обновлениями!",
            reply_markup=main_menu(),
        )
    else:
        await callback.message.answer(text, parse_mode="HTML", reply_markup=main_menu())

    await callback.answer()


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer(f"Главное меню:", reply_markup=main_menu())
    await callback.answer()


dp.include_router(router)
