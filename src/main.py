import asyncio
from handlers import dispatcher
from handlers import start
from handlers import cluster
from handlers import user


async def main():
    await dispatcher.dp.start_polling(dispatcher.bot)


if __name__ == "__main__":
    asyncio.run(main())
