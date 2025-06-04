import asyncio
from handlers import dispatcher

from handlers import start
from handlers.clusters import cluster
from handlers.users import user
from handlers.events import event
import redis.asyncio as redis
import logging


async def main():
    db = redis.Redis(host="localhost", port=6379, db=0)
    # logging.basicConfig(
    #     filename="users.log",
    #     level=logging.INFO,
    #     filemode="a",
    #     format="%(asctime)s %(message)s",
    # )
    # logging.getLogger("aiogram").setLevel(logging.WARNING)
    dispatcher.db = db
    await dispatcher.dp.start_polling(dispatcher.bot)


if __name__ == "__main__":
    asyncio.run(main())
