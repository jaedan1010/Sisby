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
    print(message.author.is_on_mobile())
client.run("NzI3Mzc2NDEzMTYxODE2MDg2.Xvq8IQ.klRja_iwGR2ncl9En_znNc2pgI8")