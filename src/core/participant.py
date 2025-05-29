import aiohttp
from dotenv import load_dotenv
import os
from math import ceil

load_dotenv()


async def get_participant_info(login) -> dict:
    """
    returns information about the users
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = f"https://edu-api.21-school.ru/services/21-school/api/v1/participants/{login}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                coalition_info = await get_coalition_info(login)
                participant_coins = await get_participant_coins(login)
                participant_workstation = await get_participant_workstation(login)
                participant_logtime = await get_participant_logtime(login)
                participant_feedback = await get_participant_feedback(login)
                ans.update(coalition_info)
                ans.update(participant_coins)
                ans.update(participant_workstation)
                ans.update({"logtime": participant_logtime})
                ans.update(participant_feedback)
                return ans

            # записываем лог


async def get_participant_workstation(login) -> dict:
    """
    returns information about the participant's of workstation
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = f"https://edu-api.21-school.ru/services/21-school/api/v1/participants/{login}/workstation"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                if "application/json " != responce.headers.get("content-type", None):
                    return {"active": False}

                ans = await responce.json()
                return ans

            # записываем лог


async def get_coalition_info(login):
    """
    returns coalition info about participant
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = f"https://edu-api.21-school.ru/services/21-school/api/v1/participants/{login}/coalition"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans

            # записываем лог

            return {}


async def get_participant_coins(login):
    """
    returns participants points
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = f"https://edu-api.21-school.ru/services/21-school/api/v1/participants/{login}/points"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans

            return {}


async def get_participant_logtime(login):

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = f"https://edu-api.21-school.ru/services/21-school/api/v1/participants/{login}/logtime"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                ans = await responce.text()
                return ceil(float(ans))

            return {}


async def get_participant_feedback(login):

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = f"https://edu-api.21-school.ru/services/21-school/api/v1/participants/{login}/feedback"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                responce = await responce.json()

                return responce

            return {}
