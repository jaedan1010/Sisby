import asyncio
import aiohttp
import discord
pingpongurl = "https://builder.pingpong.us/api/builder/5ef73186e4b0a5ea92dbf5db/integration/v0.2/custom/"
pingpongauth = "Basic a2V5OmMzZGU2ZGI0ODAxZmU1MzVjNjY1MmZkNzEzMjJhN2Vh"
client = discord.Client()
@client.event
async def on_ready():
    print("ready")
@client.event
async def on_message(message):
    if message.author.bot: return
    header = {
        'Authorization': pingpongauth,
        'Content-Type': 'application/json'
    }
    param = {
        'request': {
            'query': message.content
        }
    }
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.post(pingpongurl+f'/{message.author.id}', json=param) as res:
            data = await res.json()
            assert 'response' in data
            assert 'replies' in data['response']
            for reply in data['response']['replies']:
                if 'text' in reply:
                    await message.channel.send(reply['text'])
client.run("NzI3Mzc2NDEzMTYxODE2MDg2.Xvq8IQ.klRja_iwGR2ncl9En_znNc2pgI8")