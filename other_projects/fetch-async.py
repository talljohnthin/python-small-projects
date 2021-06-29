import aiohttp
import asyncio


async def fetch_dog():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://dog.ceo/api/breed/boxer/images/random') as response:
            json = await response.json()
            return json


async def fetch_cat():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.thecatapi.com/v1/images/search') as response:
            json = await response.json()
            return json


async def main():
    tasks = await asyncio.gather(fetch_dog(), fetch_cat())

    for task in tasks:
        print(task)

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())
