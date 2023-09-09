import aiohttp
import asyncio

link = 'https://youtube.com/shorts/o_THqt5IpOg?si=rB5bPP5dRM98fFtk'
url = f'https://fasttube.ir/?url={link}'

async def audio():
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url) as response:
            json = await response.json()
            audio = json['data']['audios']['m4a'][0]['url']

async def mp4():
    async with aiohttp.ClientSession() as session:
        async with session.post(url=url) as response:
            json = await response.json()
            mp4 = json['data']['formats'][0]['url']

asyncio.run(audio())