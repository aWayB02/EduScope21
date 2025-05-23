import aiohttp
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


async def fetch(url):

    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                ans = await responce.json()
                return ans


async def main():

    result = await fetch()
    from pprint import pprint

    pprint(result)


asyncio.run(main())
