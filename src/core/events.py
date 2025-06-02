import aiohttp
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from .config import ENDPOINTS
from .utils import get_msk_time

load_dotenv()


async def get_events():

    date = datetime.now()
    from_date = date.strftime("%Y-%m-%dT00:00:00Z")
    to_date = (date + timedelta(days=10)).strftime("%Y-%m-%dT00:00:00Z")
    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = ENDPOINTS["events"]
    params = {"from": from_date, "to": to_date, "limit": 4}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as responce:

            if responce.status == 200:

                responce = await responce.json()

                if len(responce["events"]) == 0:
                    return False

                events = []
                for event in responce["events"]:
                    startDateTime = event["startDateTime"]
                    endDateTime = event["endDateTime"]

                    new_event = {
                        "name": event["name"],
                        "description": event["description"],
                        "location": event["location"],
                        "startDateTime": get_msk_time(startDateTime),
                        "endDateTime": get_msk_time(endDateTime),
                    }

                    events.append(new_event)

                text = "\n\n".join(
                    f"📌 <b>{event['name']}</b>\n🕒 С {event['startDateTime']} до {event['endDateTime']}\n📝 {event['description']} \n<b>Локация: {event["location"]}</b>"
                    for event in events
                )

                return text
