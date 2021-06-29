import aiohttp
import asyncio


async def get_todos():
    async with aiohttp.ClientSession() as session:

        for number in range(1, 6):
            async with session.get(f'https://jsonplaceholder.typicode.com/todos/{number}') as response:
                json = await response.json()
                print("Title: ", json['title'])


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_todos())
