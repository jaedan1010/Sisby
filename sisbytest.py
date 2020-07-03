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
    user = message.author
    status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
        discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
        discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
        discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
    user_status = status_dict[user.status]
    await message.channel.send(embed = discord.Embed(title="user status", description=f"{user}님의 상태는 {user_status}"))
client.run("NzI3Mzc2NDEzMTYxODE2MDg2.Xvq8IQ.klRja_iwGR2ncl9En_znNc2pgI8")