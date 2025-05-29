import asyncio
from handlers import dispatcher
from handlers import start
from handlers import cluster
from handlers import user
import redis.asyncio as redis


async def main():
    db = redis.Redis(host="localhost", port=6379, db=0)
    dispatcher.db = db
    await dispatcher.dp.start_polling(dispatcher.bot)


if __name__ == "__main__":
    asyncio.run(main())
