import aiohttp
import aiohttp.client_exceptions
from dotenv import load_dotenv
import os

load_dotenv()


async def get_participant_info(login) -> dict:
    """
    returns information about the users
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = "https://edu-api.21-school.ru/services/21-school/api/v1/participants/" + login

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                coalition_info = await get_coalition_info(login)
                participant_coins = await get_participant_coins(login)
                participant_workstation = await get_participant_workstation(login)
                ans.update(coalition_info)
                ans.update(participant_coins)
                ans.update(participant_workstation)
                return ans

            # записываем лог


async def get_participant_workstation(login) -> dict:
    """
    returns information about the participant's of workstation
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = (
        "https://edu-api.21-school.ru/services/21-school/api/v1/participants/"
        + login
        + "/workstation"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                try:
                    ans = await responce.json()
                    return ans
                except aiohttp.client_exceptions.ContentTypeError:
                    return {"active": "Нет на месте"}

            # записываем лог


async def get_coalition_info(login):
    """
    returns coalition info about participant
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = (
        "https://edu-api.21-school.ru/services/21-school/api/v1/participants/"
        + login
        + "/coalition"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans

            # записываем лог


async def get_participant_coins(login):
    """
    returns participants' points
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = (
        "https://edu-api.21-school.ru/services/21-school/api/v1/participants/"
        + login
        + "/points"
    )

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans
