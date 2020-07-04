import re
import discord
import lavalink
client = discord.Client()
token = "NzI3Mzc2NDEzMTYxODE2MDg2.Xv_yFA.cZdmlFkppUddkYAlEpthY0Dfae4"
url_rx = re.compile(r'https?://(?:www\.)?.+')
@client.event
async def on_ready():
    print("ready")
    print(url_rx)
@client.event
async def on_message(message):
    if message.content == "hello":
        print("bye")
client.run(token)