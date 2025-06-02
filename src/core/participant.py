import aiohttp
from dotenv import load_dotenv
import os
from math import ceil
import logging
from .config import ENDPOINTS

load_dotenv("keys.env")


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


async def get_participant_info(login) -> dict:
    """
    returns information about the users
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["baseInfoParticipant"](login)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                coalition_info = await get_coalition_info(login)
                participant_coins = await get_participant_coins(login)
                participant_workstation = await get_participant_workstation(login)
                participant_logtime = {"logtime": await get_participant_logtime(login)}
                participant_feedback = await get_participant_feedback(login)
                data = [
                    coalition_info,
                    participant_coins,
                    participant_workstation,
                    participant_logtime,
                    participant_feedback,
                ]
                for d in data:
                    ans.update(d)
                return ans


async def get_participant_workstation(login) -> dict:
    """
    returns information about the participant's of workstation
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantWorkstation"](login)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                if "application/json" != responce.headers.get("content-type", None):
                    return {"active": False}

                ans = await responce.json()
                return ans


async def get_coalition_info(login) -> dict:
    """
    returns coalition info about participant
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["coalitionInfo"](login)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans

            return {}


async def get_participant_coins(login) -> dict:
    """
    returns participants points
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantCoins"](login)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:

                ans = await responce.json()
                return ans

            return {}


async def get_participant_logtime(login) -> dict:

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantLogtime"](login)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                ans = await responce.text()
                return ceil(float(ans))

            return {}


async def get_participant_feedback(login):

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantFeedback"](login)

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                responce = await responce.json()

                return responce

            return {}
