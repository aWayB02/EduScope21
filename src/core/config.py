import os
from dotenv import load_dotenv


load_dotenv("api.env")
load_dotenv("keys.api")

API_BASE_URL = os.getenv("API_BASE_URL")
API_BASE_URL_PARTICIPANT = os.getenv("API_BASE_URL_PARTICIPANT")

ENDPOINTS = {
    "baseInfoParticipant": lambda login: f"{API_BASE_URL_PARTICIPANT}{login}",
    "cluster": f"{API_BASE_URL}/campuses/{os.getenv("ID")}/clusters",
    "participantWorkstation": lambda login: f"{API_BASE_URL_PARTICIPANT}{login}/workstation",
    "coalitionInfo": lambda login: f"{API_BASE_URL_PARTICIPANT}{login}/coalition",
    "participantCoins": lambda login: f"{API_BASE_URL_PARTICIPANT}{login}/points",
    "participantLogtime": lambda login: f"{API_BASE_URL_PARTICIPANT}{login}/logtime",
    "participantFeedback": lambda login: f"{API_BASE_URL_PARTICIPANT}{login}/feedback",
    "events": f"{API_BASE_URL}/events",
}
