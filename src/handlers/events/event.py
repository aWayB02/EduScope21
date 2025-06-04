from core.events import get_events
from buttons.b import main_menu
from aiogram import F, Router
from aiogram.types import CallbackQuery
from ..dispatcher import dp

router = Router()


@router.callback_query(F.data == "events")
async def events(callback: CallbackQuery):
    events = await get_events()
    if not events:
        await callback.message.answer(
            "В ближайшее время мероприятий нет. Следите за обновлениями!",
            reply_markup=main_menu(),
        )
    else:
        await callback.message.answer(
            events, parse_mode="HTML", reply_markup=main_menu()
        )

    await callback.answer()


dp.include_router(router)
