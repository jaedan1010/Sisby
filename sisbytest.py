import asyncio
import aiohttp
import discord
client = discord.Client()
@client.event
async def on_ready():
    print("ready")
@client.event
async def on_message(message):
    if message.author.bot: return
    m = message.content
    header = {
        'Authorization': os.getenv("PINGPONG_AUTH"),
        'Content-Type': 'application/json'
    }
    param = {
        'request': {
            'query': m.content[4:]
        }
    }
    async with aiohttp.ClientSession(headers=header) as session:
        async with session.post(os.getenv('PINGPOING_URL')+f'/{message.author.id}', json=param) as res:
            data = await res.json()
            assert 'response' in data
            assert 'replies' in data['response']
            for reply in data['response']['replies']:
                if 'text' in reply:
                    await message.channel.send(reply['text'])
client.run("NzI3Mzc2NDEzMTYxODE2MDg2.Xvq8IQ.klRja_iwGR2ncl9En_znNc2pgI8")