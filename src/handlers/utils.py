from aiogram.types import Message
from handlers.buttons import main_menu
from .shemas import Participant


def training_status(status):
    return status == "Survival camp"


parallelName_status = {
    "Core program": "Core program ✅",
    "Survival camp": "Survival camp 🟡",
}

tribes = {
    "Erzi": "Erzi 🦅",
    "Lom": "Lom 🦁",
    "Borz": "Borz 🐺",
    "Guv": "Guv 🗻",
    "Are": "Are 🌋",
    "Loam": "Loam 🏔",
}


async def send_info_participant(status, message: Message, data: dict):
    from pprint import pprint

    pprint(data)

    participant = Participant(**data)

    if status:  # survival camp
        if participant.active is not None:
            await message.answer(
                f"Логин: <b>{participant.login}</b> 👤\n"
                f"Поток: <b>{participant.className}</b> 📆\n"
                f"Cтатус обучения: <b>{parallelName_status[participant.parallelName]}</b>\n"
                f"Xp: <b>{participant.expValue}</b> 🎯\n"
                f"Level: <b>{participant.level}</b> ⚡️\n"
                f"Опыт до следующего уровня: <b>{participant.expToNextLevel}</b> 📈\n"
                f"Coins: <b>{participant.coins}</b> 💸\n"
                f"Трайб: <b>{tribes.get(participant.name, participant.name)}</b>\n"
                f"peerReviewPoints: <b>{participant.peerReviewPoints}</b>\n"
                f"codeReviewPoints: <b>{participant.codeReviewPoints}</b>\n"
                f"Локация: <b>Отсутствует в кампусе</b> ❌\n",
                parse_mode="HTML",
                reply_markup=main_menu(),
            )
            return
        await message.answer(
            f"Логин: <b>{participant.login}</b> 👤\n"
            f"Поток: <b>{participant.className}</b> 📆\n"
            f"Cтатус обучения: <b>{parallelName_status[participant.parallelName]}</b>\n"
            f"Xp: <b>{participant.expValue}</b> 🎯\n"
            f"Level: <b>{participant.level}</b> ⚡️\n"
            f"Опыт до следующего уровня: <b>{participant.expToNextLevel}</b> 📈\n"
            f"Coins: <b>{participant.coins}</b> 💸\n"
            f"Трайб: <b>{tribes.get(participant.name, participant.name)}</b>\n"
            f"peerReviewPoints: <b>{participant.peerReviewPoints}</b> 💸\n"
            f"codeReviewPoints: <b>{participant.codeReviewPoints}</b> 💸\n"
            f"Локация: <b>{participant.clusterName} | ряд {participant.row} | Место {participant.number}</b>\n",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return

    # Core program
    if "active" not in data.keys():
        await message.answer(
            f"Логин: <b>{participant.login}</b>\n"
            f"Поток: <b>{participant.className}</b>\n"
            f"Cтатус обучения: <b>{parallelName_status[participant.parallelName]}</b>\n"
            f"Xp: <b>{participant.expValue}</b> 🎯\n"
            f"Level: <b>{participant.level}</b> ⚡️\n"
            f"Опыт до следующего уровня: <b>{participant.expToNextLevel}</b> 📈\n"
            f"Coins: <b>{participant.coins}</b> 💸\n"
            f"peerReviewPoints: <b>{participant.peerReviewPoints}</b>\n"
            f"codeReviewPoints: <b>{participant.codeReviewPoints}</b>\n"
            f"Трайб: <b>{tribes.get(participant.name, participant.name)}</b>\n"
            f"Место в трайбе: <b>{participant.rank}</b> 📊\n"
            f"Локация: <b>{participant.clusterName} | ряд {participant.row} | Место {participant.number}</b>\n",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return
    await message.answer(
        f"Логин: <b>{participant.login}</b>\n"
        f"Поток: <b>{participant.className}</b>\n"
        f"Cтатус обучения: <b>{parallelName_status[participant.parallelName]}</b>\n"
        f"Xp: <b>{participant.expValue}</b> 🎯\n"
        f"Level: <b>{participant.level}</b> ⚡️\n"
        f"Опыт до следующего уровня: <b>{participant.expToNextLevel}</b> 📈\n"
        f"Coins: <b>{participant.coins}</b> 💸\n"
        f"peerReviewPoints: <b>{participant.peerReviewPoints}</b>\n"
        f"codeReviewPoints: <b>{participant.codeReviewPoints}</b>\n"
        f"Трайб: <b>{tribes.get(participant.name, participant.name)}</b>\n"
        f"Место в трайбе: <b>{participant.rank}</b> 📊\n"
        f"Локация: <b>Отсутствует в кампусе</b> ❌\n",
        parse_mode="HTML",
        reply_markup=main_menu(),
    )
