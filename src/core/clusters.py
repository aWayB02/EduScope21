import aiohttp
from dotenv import load_dotenv
import os

load_dotenv()


async def get_cluster(cluster):
    """
    returns information about capacity cluster
    """

    url = (
        "https://edu-api.21-school.ru/services/21-school/api/v1/campuses/"
        + os.getenv("ID")
        + "/clusters"
    )
    headers = {"Authorization": f"Bearer {os.getenv("JWT")}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as responce:

            if responce.status == 200:
                ans = await responce.json()
                for cluster_info in ans["clusters"]:
                    if cluster_info["name"][0] == cluster[0]:
                        capacity = cluster_info["capacity"]
                        available = capacity - cluster_info["availableCapacity"]
                        return (capacity, cluster_info["availableCapacity"], available)

            # записываем в лог
