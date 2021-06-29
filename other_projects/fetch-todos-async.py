import aiohttp
import asyncio


async def get_todos():
    async with aiohttp.ClientSession() as session:
        response = await session.get('https://jsonplaceholder.typicode.com/todos/1')
        print(await response.json())

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(get_todos())
