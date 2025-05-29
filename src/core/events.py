import aiohttp
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, timezone

load_dotenv()


async def get_events():

    d = datetime.now()
    from_date = d.strftime("%Y-%m-%dT00:00:00Z")
    to_date = (d + timedelta(days=10)).strftime("%Y-%m-%dT00:00:00Z")
    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}
    url = "https://edu-api.21-school.ru/services/21-school/api/v1/events"
    params = {"from": from_date, "to": to_date, "limit": 4}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as responce:

            if responce.status == 200:

                responce = await responce.json()

                if len(responce["events"]) == 0:
                    return False

                def get_msk_time(date: str):

                    dt_utc = datetime.fromisoformat(date.replace("Z", "+00:00"))
                    moscow_time = dt_utc.astimezone(timezone(timedelta(hours=3)))
                    return moscow_time.strftime("%-d %B %Y года, %H:%M (МСК)")

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
