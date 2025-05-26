from aiogram.types import Message
from handlers.buttons import main_menu


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


async def send_info_participant(status, message: Message, data):

    (
        login,
        coalitionName,
        coins,
        peerReviewPoints,
        codeReviewPoints,
        className,
        parallelName,
        expValue,
        level,
        expToNextLevel,
    ) = (
        data["login"],
        data["name"],
        data["coins"],
        data["peerReviewPoints"],
        data["codeReviewPoints"],
        data["className"],
        data["parallelName"],
        data["expValue"],
        data["level"],
        data["expToNextLevel"],
    )

    if "active" not in data.keys():
        clusterName = data["clusterName"]
        row = data["row"]
        number = data["number"]

    from pprint import pprint

    pprint(data)

    if status:  # survival camp
        if "active" in data.keys():
            await message.answer(
                f"Логин: <b>{login}</b> 👤\n"
                f"Поток: <b>{className}</b> 📆\n"
                f"Cтатус обучения: <b>{parallelName_status[parallelName]}</b>\n"
                f"Xp: <b>{expValue}</b> 🎯\n"
                f"Level: <b>{level}</b> ⚡️\n"
                f"Опыт до следующего уровня: <b>{expToNextLevel}</b> 📈\n"
                f"Coins: <b>{coins}</b> 💸\n"
                f"Трайб: <b>{tribes[coalitionName]}</b>\n"
                f"peerReviewPoints: <b>{peerReviewPoints}</b>\n"
                f"codeReviewPoints: <b>{codeReviewPoints}</b>\n"
                f"Локация: <b>Отсутствует в кампусе</b> ❌\n",
                parse_mode="HTML",
                reply_markup=main_menu(),
            )
            return
        await message.answer(
            f"Логин: <b>{login}</b> 👤\n"
            f"Поток: <b>{className}</b> 📆\n"
            f"Cтатус обучения: <b>{parallelName_status[parallelName]}</b>\n"
            f"Xp: <b>{expValue}</b> 🎯\n"
            f"Level: <b>{level}</b> ⚡️\n"
            f"Опыт до следующего уровня: <b>{expToNextLevel}</b> 📈\n"
            f"Coins: <b>{coins}</b> 💸\n"
            f"Трайб: <b>{tribes[coalitionName]}</b>\n"
            f"peerReviewPoints: <b>{peerReviewPoints}</b> 💸\n"
            f"codeReviewPoints: <b>{codeReviewPoints}</b> 💸\n"
            f"Локация: <b>{clusterName} | ряд {row} | Место {number}</b>\n",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return

    # Core program
    rank = data["rank"]
    if "active" not in data.keys():
        await message.answer(
            f"Логин: <b>{login}</b>\n"
            f"Поток: <b>{className}</b>\n"
            f"Cтатус обучения: <b>{parallelName_status[parallelName]}</b>\n"
            f"Xp: <b>{expValue}</b> 🎯\n"
            f"Level: <b>{level}</b> ⚡️\n"
            f"Опыт до следующего уровня: <b>{expToNextLevel}</b> 📈\n"
            f"Coins: <b>{coins}</b> 💸\n"
            f"peerReviewPoints: <b>{peerReviewPoints}</b>\n"
            f"codeReviewPoints: <b>{codeReviewPoints}</b>\n"
            f"Трайб: <b>{tribes[coalitionName]}</b>\n"
            f"Место в трайбе: <b>{rank}</b> 📊\n"
            f"Локация: <b>{clusterName} | ряд {row} | Место {number}</b>\n",
            parse_mode="HTML",
            reply_markup=main_menu(),
        )
        return
    await message.answer(
        f"Логин: <b>{login}</b>\n"
        f"Поток: <b>{className}</b>\n"
        f"Cтатус обучения: <b>{parallelName_status[parallelName]}</b>\n"
        f"Xp: <b>{expValue}</b> 🎯\n"
        f"Level: <b>{level}</b> ⚡️\n"
        f"Опыт до следующего уровня: <b>{expToNextLevel}</b> 📈\n"
        f"Coins: <b>{coins}</b> 💸\n"
        f"peerReviewPoints: <b>{peerReviewPoints}</b>\n"
        f"codeReviewPoints: <b>{codeReviewPoints}</b>\n"
        f"Трайб: <b>{tribes[coalitionName]}</b>\n"
        f"Место в трайбе: <b>{rank}</b> 📊\n"
        f"Локация: <b>Отсутствует в кампусе</b> ❌\n",
        parse_mode="HTML",
        reply_markup=main_menu(),
    )
