from aiogram import Router
from aiogram import types
from handlers.buttons import main_menu
from aiogram import types, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from core.participant import get_participant_info
from .dispatcher import dp
from .utils import send_info_participant, training_status

router = Router()


class GetUserInput(StatesGroup):
    waiting_for_text = State()


@router.message(GetUserInput.waiting_for_text)
async def get_user_info(message: types.Message, state: FSMContext):
    login = message.text.lower()
    data = await get_participant_info(login)
    await send_info_participant(training_status(data["parallelName"]), message, data)
    await state.clear()


@router.message(F.text)
async def is_no_valid_input(message: Message):
    await message.answer_sticker(
        "CAACAgIAAxkBAAIBmmgzbIEOenYtcwzYNbCPPI35g_RZAAIldQACtRZ4STRZWNqBgPpLNgQ"
    )


@router.callback_query(F.data == "get_user")
async def get_name_user(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Пожалуйста, введите имя пира:")
    await state.set_state(GetUserInput.waiting_for_text)
    await callback.answer()


@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.answer(f"Главное меню:", reply_markup=main_menu())
    await callback.answer()


dp.include_router(router)
