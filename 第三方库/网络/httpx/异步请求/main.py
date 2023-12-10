import httpx
import asyncio


async def fetch(url):
    async with httpx.AsyncClient() as client:
        res = await client.get(url)
        print(res.text)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch("https://httpbin.org/get"))
