from aiogram.filters.command import Command
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Кластеры 🖥️", callback_data="open_cluster")],
            [
                InlineKeyboardButton(
                    text="Найти пользователя 🔍", callback_data="get_user"
                )
            ],
            [InlineKeyboardButton(text="Правила 📜", callback_data="a")],
            [InlineKeyboardButton(text="Часто задаваемые вопросы", callback_data="v")],
        ]
    )


def cluster():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1️⃣ Denal", callback_data="cluster:D")],
            [InlineKeyboardButton(text="2️⃣ Ezdel", callback_data="cluster:E")],
            [InlineKeyboardButton(text="3️⃣ Sabar", callback_data="cluster:S")],
            [InlineKeyboardButton(text="4️⃣ Tesham", callback_data="cluster:T")],
            [InlineKeyboardButton(text="⏪ Назад", callback_data="back")],
        ]
    )
