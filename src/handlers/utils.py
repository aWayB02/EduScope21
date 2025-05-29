from aiogram.types import Message
from handlers.buttons import main_menu
from .shemas import Participant
from pydantic import validate_call


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


@validate_call
def template_participant(key, personality: Participant):

    participant = {
        "login": f"Логин: <b>{personality.login}</b>\n",
        "flow": f"Поток: <b>{personality.className}</b> 📆\n",
        "statusOfTraining": f"statusOfTraining: <b>{parallelName_status[personality.parallelName]}</b>\n",
        "exp": f"exp: <b>{personality.expValue}</b> 🎯\n",
        "level": f"level: <b>{personality.level}</b> ⚡️\n",
        "expToTheNextLevel": f"expToTheNextLevel: <b>{personality.expToNextLevel}</b> 📈\n",
        "coins": f"coins: <b>{personality.coins}</b> 💸\n",
        "tribe": f"tribe: <b>{tribes.get(personality.name, personality.name)}</b>\n",
        "peerReviewPoints": f"peerReviewPoints: <b>{personality.peerReviewPoints}</b>\n",
        "codeReviewPoints": f"codeReviewPoints: <b>{personality.codeReviewPoints}</b>\n",
        "placeInTheTribe": f"Место в трайбе: <b>{personality.rank}</b> 📊\n",
        "location_in_campus": f"Локация: <b>{personality.clusterName} | ряд {personality.row} | место {personality.number}</b>\n",
        "location_not_in_campus": f"Локация: <b>Отсутствует в кампусе</b> ❌\n",
        "logtime": f"Время работы за неделю (в часах): <b>{personality.logtime}</b>",
    }

    return participant[key]


@validate_call
async def send_info_participant(status, message: Message, participant: Participant):

    if status:  # survival camp
        if participant.active is not None:  # not in campus
            await message.answer(
                f"{template_participant("login", participant)}"
                f"{template_participant("flow", participant)}"
                f"{template_participant("statusOfTraining", participant)}"
                f"{template_participant("exp", participant)}"
                f"{template_participant("level", participant)}"
                f"{template_participant("expToTheNextLevel", participant)}"
                f"{template_participant("coins", participant)}"
                f"{template_participant("tribe", participant)}"
                f"{template_participant("peerReviewPoints", participant)}"
                f"{template_participant("codeReviewPoints", participant)}"
                f"{template_participant("location_not_in_campus", participant)}"
                f"{template_participant("logtime", participant)}",
                parse_mode="HTML",
                reply_markup=main_menu(),
            )
            return
        await message.answer(
            f"{template_participant("login", participant)}"
            f"{template_participant("flow", participant)}"
            f"{template_participant("statusOfTraining", participant)}"
            f"{template_participant("exp", participant)}"
            f"{template_participant("level", participant)}"
            f"{template_participant("expToTheNextLevel", participant)}"
            f"{template_participant("coins", participant)}"
            f"{template_participant("tribe", participant)}"
            f"{template_participant("peerReviewPoints", participant)}"
            f"{template_participant("codeReviewPoints", participant)}"
            f"{template_participant("location_in_campus", participant)}",
            f"{template_participant("logtime", participant)}",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return

    # Core program
    if participant.active is None:  # not in campus
        await message.answer(
            f"{template_participant("login", participant)}"
            f"{template_participant("flow", participant)}"
            f"{template_participant("statusOfTraining", participant)}"
            f"{template_participant("exp", participant)}"
            f"{template_participant("level", participant)}"
            f"{template_participant("expToTheNextLevel", participant)}"
            f"{template_participant("coins", participant)}"
            f"{template_participant("tribe", participant)}"
            f"{template_participant("placeInTheTribe", participant)}"
            f"{template_participant("peerReviewPoints", participant)}"
            f"{template_participant("codeReviewPoints", participant)}"
            f"{template_participant("location_in_campus", participant)}"
            f"{template_participant("logtime", participant)}",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return
    await message.answer(
        f"{template_participant("login", participant)}"
        f"{template_participant("flow", participant)}"
        f"{template_participant("statusOfTraining", participant)}"
        f"{template_participant("exp", participant)}"
        f"{template_participant("level", participant)}"
        f"{template_participant("expToTheNextLevel", participant)}"
        f"{template_participant("coins", participant)}"
        f"{template_participant("tribe", participant)}"
        f"{template_participant("placeInTheTribe", participant)}"
        f"{template_participant("peerReviewPoints", participant)}"
        f"{template_participant("codeReviewPoints", participant)}"
        f"{template_participant("location_not_in_campus", participant)}"
        f"{template_participant("logtime", participant)}",
        parse_mode="HTML",
        reply_markup=main_menu(),
    )
