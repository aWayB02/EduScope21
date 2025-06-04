import aiohttp
from dotenv import load_dotenv
import os
from math import ceil
from .config import ENDPOINTS
import logging

load_dotenv("keys.env")


async def get_participant_info(login: str) -> dict:
    """
    Collects and returns full information about a participant,
    including data from multiple API sources.

    Args:
        login (str): student's login

    Returns:
        dict: Aggregated JSON data about the participant
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["baseInfoParticipant"](
        login
    )  # endpoint school 21 API baseInfoParticipant

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:

                full_info_student: dict = await response.json()
                # engaged other information about student
                other_info_student = [
                    await get_coalition_info(login),
                    await get_participant_coins(login),
                    await get_participant_workstation(login),
                    {"logtime": await get_participant_logtime(login)},
                    await get_participant_feedback(login),
                ]
                # associations all information

                for data in other_info_student:
                    full_info_student.update(data)

                # logging.info(
                # "✅ Пользователь '%s' найден. Сбор данных завершён успешно.",
                # full_info_student["login"],
                # )
                return full_info_student


async def get_participant_workstation(login: str) -> dict:
    """
    Checks whether the student is currenly on campus.

    if student is currently on campus, the API returns:
        Response body:
        {
            "clusterId": 36756,
            "clusterName": "name",
            "row": "n",
            "number": 4
        }
    if not, API responce will not be JSON (content-type != "application/json"),
    indicating that the student is not currently on campus

    Args:
        login (str): student's login

    Returns:
        dict: returns workstation location data if active, or {'active': False} if not
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantWorkstation"](
        login
    )  # endpoint school 21 API participant_workstation

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:
                if "application/json" != response.headers.get("content-type", None):
                    return {"active": False}

                ans = await response.json()
                return ans

            # logging.WARNING(
            #     f"WARNING: response status {response.status}, headers - {response.headers}"
            # )


async def get_coalition_info(login: str) -> dict:
    """
    Returns information about coalition, for examlpte, the API returns:
        {
            "coalitionId": 454,
            "name": "Erzi",
            "rank": 19
        }
    Here 'rank', is the student's place within the coalition

    if login is not found, the API return status 404, a response body like:
        {
            "status": 404,
            "exceptionUUID": "iBNiXKZmh7",
            "code": "NOT_FOUND",
            "message": "Not found user by login {login}"
        }

    Args:
        login (str): student's login

    Returns:
        dict: Coalition information if found, otherwise an empty dictionary
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["coalitionInfo"](login)  # endpoint school 21 API coalition

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:

                ans = await response.json()
                return ans

            # logging.WARNING(
            #     f"WARNING: response status {response.status}, headers - {response.headers}"
            # )
            return {}  # other errors


async def get_participant_coins(login: str) -> dict:
    """
    Returns information about the student's earned points and coints
    For example, the API returns:

        {
            "peerReviewPoints": 5,
            "codeReviewPoints": 5,
            "coins": 110
        }

    if login is not found, the API returns status 404, a response body like:

        {
            "status": 404,
            "exceptionUUID": "bkFpLVoJJV",
            "code": "NOT_FOUND",
            "message": "Not found user by login {login}"
        }

    Args:
        login (str): student's login

    Returns:
        dict: A dictionary with coin and point information if found, otherwise an anpty dictionary
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantCoins"](login)  # endpoint school 21 API

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:

                ans = await response.json()
                return ans

            # logging.WARNING(
            #     f"WARNING: response status {response.status}, headers - {response.headers}"
            # )
            return {}


async def get_participant_logtime(login: str) -> dict:
    """
    Returns information about how long does a student work at a workstation
    """

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantLogtime"](login)  # endpoint school 21 API

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:
                ans = await response.text()
                return ceil(float(ans))

            # logging.WARNING(
            #     f"WARNING: response status {response.status}, headers - {response.headers}"
            # )
            return {}


async def get_participant_feedback(login: str):

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["participantFeedback"](login)  # endpoint school 21 API

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:

            if response.status == 200:
                response = await response.json()

                return response

            # logging.WARNING(
            #     f"WARNING: response status {response.status}, headers - {response.headers}"
            # )
            return {}
