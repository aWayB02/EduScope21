import aiohttp
import aiohttp.client_exceptions
from dotenv import load_dotenv
import os


load_dotenv()


async def get_participant_login(login):
    """
    returns information about the users
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = "https://edu-api.21-school.ru/services/21-school/api/v1/participants/" + login

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans

            # записываем лог


async def get_participant_workstation(login):
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
                    return "Пользователь не на месте."

            # записываем лог
