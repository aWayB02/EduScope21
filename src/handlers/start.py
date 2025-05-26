from aiogram import Router
from .dispatcher import dp
from aiogram import types
from aiogram.filters.command import Command
from handlers.buttons import main_menu

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f"Peer to Peer {message.from_user.first_name}! 🍐", reply_markup=main_menu()
    )


dp.include_router(router)
