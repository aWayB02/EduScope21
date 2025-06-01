import redis.asyncio as redis
import json
from core.participant import get_participant_info


async def get_user_from_redis(login, db: redis.Redis):
    data = await db.get(login)
    if data is None:
        return False
    decoded = data.decode("utf-8")
    if decoded == "null":
        return False
    return json.loads(decoded)


async def save_user_to_redis(login, db: redis.Redis):
    data = await get_participant_info(login)
    await db.set(login, json.dumps(data), ex=60 * 60)
    json_str = await db.get(login)
    if json_str:
        return json.loads(json_str.decode("utf-8"))
    return False
