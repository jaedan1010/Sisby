import discord
import asyncio
import datetime
import koreanbots
import datetime
import os
import random
import math
import json
import aiohttp
from dotenv import load_dotenv
load_dotenv(verbose=True)
client = discord.Client()
token = os.getenv("TOKEN")
ver = "Beta"
prefix = "시스비"
owner = [726350177601978438]
# 삼성해피트리
heimteam = [726350177601978438, 700561761690189875, 723670306102837258, 447934468603379724, 524515155254444032, 647736678815105037]
# 삼성해피트리, OwO(Discord-api), 수현, 준홍, 배인블, mswgen
bughunter = [726350177601978438, 534214957110394881]
# 삼성해피트리, 제토
Bot = koreanbots.Client(client, os.getenv("KOREANBOTS_TOKEN"))
ready = 727361177604325396
bug = 727361427173670923
botsv = 727361381157830658
건의 = 727361465274597388
pingpongurl = os.getenv("PINGPONG_URL")
pingpongauth = os.getenv("PINGPONG_AUTH")

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    await client.get_channel(int(ready)).send(embed = discord.Embed(title="봇이 준비되었습니다.").set_footer(text=client.user, icon_url=client.user.avatar_url_as(format=None, static_format="png", size=1024)))

@client.event
async def on_guild_join(guild):
    try:
        await guild.owner.send(embed = discord.Embed(title="봇을 초대해주셔서 감사합니다!", description=f"안녕하세요! {client.user.name} 개발자 삼성해피트리입니다!\n봇을 {guild.name}에 초대해주셔서 대단히 감사드리고,\n앞으로도 여러분의 서버를 위해 노력하겠습니다!\n[하트를 눌러주시면 저에게 큰 힘이 됩니다!](https://koreanbots.dev/bots/726376311710548049)").set_footer(text=client.user, icon_url=client.user.avatar_url_as(format=None, static_format="png", size=1024)))
    except:
        pass
    await client.get_channel(int(botsv)).send(embed = discord.Embed(title="봇 접속 서버 수 변동됨.", description=f"전 : {len(client.guilds)-1}\n후 : {len(client.guilds)}").set_footer(text=client.user, icon_url=client.user.avatar_url_as(format=None, static_format="png", size=1024))) 

@client.event
async def on_guild_remove(guild):
    await client.get_channel(int(botsv)).send(embed = discord.Embed(title="봇 접속 서버 수 변동됨.", description=f"전 : {len(client.guilds)+1}\n후 : {len(client.guilds)}").set_footer(text=client.user, icon_url=client.user.avatar_url_as(format=None, static_format="png", size=1024))) 

@client.event
async def on_message(message):
    try:
        if not message.content.startswith(f"{prefix}"): return
        if message.author.bot: return
        if message.content == f"{prefix} 도움말" or message.content == f"{prefix} help":
            a = random.choice([discord.Colour.red(), discord.Colour.orange(), discord.Colour.green(), discord.Colour.blue(), discord.Colour.purple()])
            await message.channel.send(embed=discord.Embed(colour=a, title=f"{client.user.name} 도움말", description=f"""
접두사 : {prefix}, 버전 : {ver}
<> = 필수, [] = 선택, () = 필요한 권한

**"커맨드"**
{prefix} 정보 [@유저 맨션]
> 유저의 정보를 조회합니다.
{prefix} 서버정보
> 서버정보를 조회합니다.
{prefix} 건의 <건의내용>
> {client.user.name}에서 필요한 기능을 건의합니다.
{prefix} 핑퐁 <아무말>
> 핑퐁빌더로 말합니다.
{prefix} 초대
> 봇 초대링크를 알려줍니다.
{prefix} 핑
> {client.user.name}의 핑입니다!

**"일정 권한이 필요한 커맨드"**
{prefix} 청소 <메세지를 청소할 숫자>
> {client.user.name}으로 해당 채널의 채팅을 <메세지를 청소할 숫자>만큼 지웁니다. (메세지 관리하기 권한)
{prefix} 킥 <@유저 맨션>
> {client.user.name}으로 해당 유저를 추방합니다. (멤버 추방하기 권한)
{prefix} 밴 <@유저 맨션>
> {client.user.name}으로 해당 유저를 차단합니다. (멤버 차단하기 권한)
{prefix} 언밴 <@유저 맨션>
> {client.user.name}으로 해당 유저를 언밴합니다. (멤버 차단하기 권한)
{prefix} 공지 <제목>&&<내용>
> {client.user.name}으로 공지를 발신합니다. (Bot Developer 권한)
{prefix} 건답 <내용>
> {client.user.name}으로 건의한 내용을 답변합니다! (Bot Developer 권한)
"""))
        if message.content == f"{prefix}" or message.content == f"{prefix} hellothisisverification":
            await message.channel.send(f"안녕하세요! 저는 {client.user.name}이에요! 시스비는 현재 {ver} 버전이고, 주인은 {client.get_user(726350177601978438)}(726350177601978438)입니다!\n저는 인공지능이에요! 접두사는 `{prefix}`입니다!")

        if message.content.startswith(f"{prefix} 정보"):
            if str(message.content[7:]) == '':
                user = message.author
                date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                    discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                    discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                    discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                user_status = status_dict[user.status]
                badge = ""
                if message.author.id in owner:
                    badge += "<:dev:715085684905345064> Sisby Developer\n"
                if message.author.id in heimteam:
                    badge += "<:heimteam:730330765212254251> Team Heim"
                if message.author.id in bughunter:
                    badge += "<:bughunter:730322955212423269> Sisby Bug Hunter\n"
                else:
                    badge += "**뱃지가 없습니다!**"
                if not len(message.author.roles) == 1:
                    roles = [role for role in user.roles]
                    embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                else:
                    embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"유저정보 - {user}")
                embed.set_thumbnail(url=user.avatar_url)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                embed.add_field(name="아이디", value=f"{user.id}", inline=False)
                embed.add_field(name="닉네임", value=f"{user.display_name}", inline=False)
                embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                try:
                    embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                    embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                except:
                    embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                embed.add_field(name="Sisby Badge", value=f"{badge}", inline=False)
                embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                await message.channel.send(embed=embed)
            else:
                try:
                    user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                    if user.bot == False:
                        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                        status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                            discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                            discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                            discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                        user_status = status_dict[user.status]
                        badge = ""
                        if user.id in owner:
                            badge += "<:dev:715085684905345064> Sisby Developer\n"
                        if user.id in heimteam:
                            badge += "<:heimteam:730330765212254251> Team Heim\n"
                        if user.id in bughunter:
                            badge += "<:bughunter:730322955212423269> Sisby Bug Hunter\n"
                        else:
                            badge += "**뱃지가 없습니다!**"
                        if not len(user.roles) == 1:
                            roles = [role for role in user.roles]
                            embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"유저정보 - {user}")
                        else:
                            embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                        embed.set_thumbnail(url=user.avatar_url)
                        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                        embed.add_field(name="아이디", value=f"{user.id}", inline=False)
                        embed.add_field(name="닉네임", value=f"{user.display_name}", inline=False)
                        embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                        try:
                            embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                            embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                        except:
                            embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                        embed.add_field(name="Sisby Badge", value=f"{badge}", inline=False)
                        embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                        await message.channel.send(embed=embed)
                    else:
                        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                        status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                            discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                            discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                            discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                        user_status = status_dict[user.status]
                        if not len(user.roles) == 1:
                            roles = [role for role in user.roles]
                            embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"봇정보 - {user}")
                        else:
                            embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"봇정보 - {user}")
                        embed.set_thumbnail(url=user.avatar_url)
                        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                        embed.add_field(name="봇 아이디", value=f"{user.id}", inline=False)
                        embed.add_field(name="봇 닉네임", value=f"{user.display_name}", inline=False)
                        embed.add_field(name="봇 생성일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                        try:
                            embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                            embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                        except:
                            embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                        embed.add_field(name="현재 봇 상태", value=f"{user_status}", inline=False)
                        embed.add_field(name="봇 초대링크 (관리자 권한)", value=f"[초대하기](https://discordapp.com/oauth2/authorize?client_id={user.id}&scope=bot&permissions=8)", inline=False)
                        await message.channel.send(embed=embed)
                except:
                    user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                    if user.bot == False:
                        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                        status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                            discord.Status.offline: '<:status_offline:728527943831126036> 오프라인',
                            discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                            discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                        user_status = status_dict[user.status]
                        badge = ""
                        if user.id in owner:
                            badge += "<:dev:715085684905345064> Sisby Developer\n"
                        if user.id in heimteam:
                            badge += "<:heimteam:730330765212254251> Team Heim\n"
                        if user.id in bughunter:
                            badge += "<:bughunter:730322955212423269> Sisby Bug Hunter\n"
                        else:
                            badge += "**뱃지가 없습니다!**"
                        if not len(user.roles) == 1:
                            roles = [role for role in user.roles]
                            embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"유저정보 - {user}")
                        else:
                            embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                        embed.set_thumbnail(url=user.avatar_url)
                        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                        embed.add_field(name="아이디", value=f"{user.id}", inline=False)
                        embed.add_field(name="닉네임", value=f"{user.display_name}", inline=False)
                        embed.add_field(name="가입일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                        try:
                            embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                            embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                        except:
                            embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                        embed.add_field(name="Sisby Badge", value=f"{badge}", inline=False)
                        embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                        await message.channel.send(embed=embed)
                    else:
                        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                        status_dict: dict = {discord.Status.online: '<:status_online:726399733026914335> 온라인',
                            discord.Status.offline: '<:status_offline:726399732930576434> 오프라인',
                            discord.Status.idle: "<:status_idle:726399733081571348> 자리비움",
                            discord.Status.do_not_disturb: "<:status_dnd:726399732557283386> 방해금지"}
                        user_status = status_dict[user.status]
                        if not len(user.roles) == 1:
                            roles = [role for role in user.roles]
                            embed=discord.Embed(colour=message.author.color, timestamp=message.created_at, title=f"봇정보 - {user}")
                        else:
                            embed=discord.Embed(colour=0xff00, timestamp=message.created_at, title=f"봇정보 - {user}")
                        embed.set_thumbnail(url=user.avatar_url)
                        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                        embed.add_field(name="봇 아이디", value=f"{user.id}", inline=False)
                        embed.add_field(name="봇 닉네임", value=f"{user.display_name}", inline=False)
                        embed.add_field(name="봇 생성일", value=f"{str(date.year)}년 {str(date.month)}월 {str(date.day)}일", inline=False)
                        try:
                            embed.add_field(name=f"가진 역할들({len(roles)-1}개)", value=f" ".join([role.mention for role in roles][1:]), inline=False)
                            embed.add_field(name="가장 높은 역할", value=f"{user.top_role.mention}", inline=False)
                        except:
                            embed.add_field(name=f"가진 역할들", value=f"**소유한 역할이 없습니다!**", inline=False)
                        embed.add_field(name="현재 봇 상태", value=f"{user_status}", inline=False)
                        embed.add_field(name="봇 초대링크 (관리자 권한)", value=f"[초대하기](https://discordapp.com/oauth2/authorize?client_id={user.id}&scope=bot&permissions=8)", inline=False)
                        await message.channel.send(embed=embed)

        if message.content == f"{prefix} 서버정보":
            embed = discord.Embed(colour=0xff00, title=f"서버정보 - {message.guild.name}", timestamp=message.created_at)
            embed.add_field(name="서버 이름", value=message.guild.name, inline=False)
            embed.add_field(name="서버 ID", value=message.guild.id, inline=False)
            embed.add_field(name="서버 주인", value=f"{message.guild.owner}\n └ <@{message.guild.owner.id}>", inline=False)
            embed.add_field(name="서버 주인 ID", value=message.guild.owner.id, inline=False)
            embed.add_field(name="서버 국가", value=message.guild.region, inline=False)
            embed.add_field(name="서버 제작일", value = message.guild.created_at.strftime("20%y년 %m월 %d일"), inline=False)
            embed.add_field(name="서버 멤버 수", value = f'전체 유저 : {len(message.guild.members)}명\n └ 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명 | 봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}개', inline=False)
            embed.add_field(name="서버 채널 수", value = f'전체 채널 : {len(message.guild.channels)}개\n └ 채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개', inline=False)
            embed.add_field(name="서버 이모지 수", value = f'{len(message.guild.emojis)}개', inline=False)

            if message.guild.afk_channel != None:
                embed.add_field(name=f'서버 잠수 채널', value=f'⭕ | 잠수 채널이 존재합니다.({message.guild.afk_channel.name} (타이머: {message.guild.afk_timeout}))', inline=False)
            else:
                embed.add_field(name=f'서버 잠수 채널', value=f'❌ | 잠수 채널이 존재하지 않습니다.', inline=False)
            if message.guild.system_channel != None:
                embed.add_field(name=f'서버 시스템 채널', value=f'⭕ | 시스템 채널이 존재합니다.({message.guild.system_channel.name} (<#{message.guild.system_channel.id}>))', inline=False)
            else:
                embed.add_field(name=f'서버 시스템 채널', value=f'❌ | 시스템 채널이 존재하지 않습니다.', inline=False)
            embed.add_field(name=f'서버 부스트 레벨', value=f'Level {message.guild.premium_tier}', inline=False)
            embed.add_field(name=f'서버 부스트 개수', value=f'Boost {message.guild.premium_subscription_count}', inline=False)
            embed.set_thumbnail(url=message.guild.icon_url)
            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        if message.content.startswith(f"{prefix} 킥"):
            if message.guild.get_member(client.user.id).guild_permissions.kick_members == True:
                if message.author.guild_permissions.kick_members:
                    try:
                        try:
                            user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                        except:
                            user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                        if user.id == message.author.id:
                            await message.channel.send("자신을 킥하는것은 그른 선택이에요!")
                        else:
                            try:
                                reason = message.content.split('&&')[1]
                            except:
                                reason = "사유 없음"
                            await message.guild.kick(user, reason = f"{reason}")
                            await message.channel.send(f"``{message.author}``에 의해서 ``{user}``를 추방하였습니다.\n사유 : {reason}")
                            try:
                                await user.send(f"``{message.author}``에 의해서 ``{user}``를 추방하였습니다.\n사유 : {reason}")
                            except:
                                pass
                    except IndexError:
                        await message.channel.send("형식이 틀린거같아요... 형식은 ``시스비 킥 <유저 맨션>&&<사유>``에요!")
                    except:
                        await message.channel.send("추방할 사람의 권한이 너무 높거나 그 유저가 서버에 없습니다.")
                else:
                    await message.channel.send("당신은 권한이 없어요!\n필요 권한 : **``멤버 추방하기``**")
            else:
                await message.channel.send("제가 킥을 할 수 있는 권한을 가지고 있지 않아요!\n필요 권한 : **``멤버 추방하기``**")

        if message.content.startswith(f"{prefix} 밴"):
            if message.guild.get_member(client.user.id).guild_permissions.ban_members == True:
                if message.author.guild_permissions.ban_members:
                    try:
                        try:
                            user = int(message.content.split('<@')[1].split('>')[0])
                        except:
                            user = int(message.content.split('<@!')[1].split('>')[0])
                        print(user)
                        if user == message.author.id:
                            await message.channel.send("자신을 밴하는것은 그른 선택이에요!")
                        else:
                            try:
                                reason = message.content.split('&&')[1]
                            except:
                                reason = "사유 없음"
                            un = await client.fetch_user(user)
                            await message.guild.ban(await client.fetch_user(user), reason=f"{reason}")
                            await message.channel.send(f"``{message.author}``에 의해서 ``{un}``를 차단하였습니다.\n사유 : {reason}")
                    except IndexError:
                        await message.channel.send("형식이 틀린거같아요... 형식은 ``시스비 밴 <유저 맨션>&&<사유>``에요!")
                    except Exception as ex:
                        await message.channel.send(f"밴할 사람의 권한이 너무 높습니다. {ex}")
                else:
                    await message.channel.send("당신은 권한이 없어요!\n필요 권한 : **``멤버 차단하기``**")
            else:
                await message.channel.send("제가 밴을 할 수 있는 권한을 가지고 있지 않아요!\n필요 권한 : **``멤버 차단하기``**")

        if message.content.startswith(f"{prefix} 언밴"):
            if message.guild.get_member(client.user.id).guild_permissions.ban_members:
                if message.author.guild_permissions.ban_members:
                    try:
                        try:
                            user = int(message.content.split('<@')[1].split('>')[0])
                        except:
                            user = int(message.content.split('<@!')[1].split('>')[0])
                        print(user)
                        try:
                            reason = message.content.split('&&')[1]
                        except:
                            reason = "사유 없음"
                        un = await client.fetch_user(user)
                        await message.guild.unban(await client.fetch_user(user), reason=f"{reason}")
                        await message.channel.send(f"``{message.author}``에 의해서 ``{un}``를 언밴하였습니다.\n사유 : {reason}")
                    except IndexError:
                        await message.channel.send("형식이 틀린거같아요... 형식은 ``시스비 언밴 <유저 맨션>&&<사유>``에요!")
                    except:
                        await message.channel.send(f"언밴할 사람의 권한이 너무 높습니다.")
                else:
                    await message.channel.send("당신은 권한이 없어요!\n필요 권한 : **``멤버 차단하기``**")
            else:
                await message.channel.send("제가 언밴을 할 수 있는 권한을 가지고 있지 않아요!\n필요 권한 : **``멤버 차단하기``**")

        if message.content.startswith(f"{prefix} 건의"):
            if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                await message.channel.send("건의사항을 입력해주세요.")
            else:
                msg = message.content[7:]
                await client.get_channel(int(건의)).send(embed = discord.Embed(title="건의가 들어왔어요!", description=msg).set_footer(text=f"{message.author}의 건의, {message.author.id}", icon_url=message.author.avatar_url))
                await message.channel.send(f"{message.author.mention}님! 건의가 완료되었습니다!")
                try:
                    await message.delete()
                except:
                    pass

        if message.content == f"{prefix} 핑":
            msg = await message.channel.send(f"**🏓 Pinging...**")
            ping = round(client.latency * 1000)
            if ping >= 0 and ping <= 100:
                pings = "매우좋음"
            elif ping >= 101 and ping <= 200:
                pings = "좋음" 
            elif ping >= 201 and ping <= 500:
                pings = "보통"
            elif ping >= 501 and ping <= 1000:
                pings = "나쁨"
            elif ping >= 1000:
                pings = "매우나쁨"
            embed = discord.Embed(colour=discord.Colour.red(), title=f"{client.user.name}의 핑", description=f"핑은 {ping}ms입니다!\n상태는 {pings}이네요!")
            embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
            await msg.edit(content="**🏓 Pong!**", embed=embed)

        if message.content.startswith(f"{prefix} 공지"):
            Data = await Bot.getBot(client.user.id)
            if message.author.id in owner:
                msg = message.content[7:]
                oksv = 0
                embed = discord.Embed(
                    title = msg.split('&&')[0],
                    description = msg.split('&&')[1] + f"\n\n이 채널에 공지가 오기 싫다면 `봇-공지` 채널을 만들어주세요!\n[{client.user.name} SUPPORT](https://discord.gg/HWZBBnR)\n[{client.user.name} 좋아요 누르기](https://koreanbots.dev/bots/726376311710548049) {Data.votes} ❤",
                    colour = discord.Colour.blue(),
                    timestamp = message.created_at
                ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - 인증됨') .set_thumbnail(url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                for i in client.guilds:
                    arr = [0]
                    alla = False
                    flag = True
                    z = 0
                    for j in i.channels:
                        arr.append(j.id)
                        z+=1
                        if "봇-공지" in j.name or "봇_공지" in j.name or "봇공지" in j.name or "bot_announcement" in j.name or "봇ㆍ공지" in j.name:
                            if str(j.type)=='text':
                                try:
                                    oksv += 1
                                    await j.send(embed=embed)
                                    alla = True
                                except:
                                    pass
                                break
                    if alla==False:
                        try:
                            chan=i.channels[1]
                        except:
                            pass
                        if str(chan.type)=='text':
                            try:
                                oksv += 1
                                await chan.send(embed=embed)
                            except:
                                pass
                await message.channel.send(f"**`📢 공지 발신 완료 📢`**\n\n{len(client.guilds)}개의 서버 중 {oksv}개의 서버에 발신 완료, {len(client.guilds) - oksv}개의 서버에 발신 실패")
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.')

        if message.content == f"{prefix} 초대":
            Data = await Bot.getBot(client.user.id)
            embed = discord.Embed(title=f"{client.user.name} 봇 초대하기", description=f"[봇 초대하기](https://discord.com/oauth2/authorize?client_id=726376311710548049&permissions=70641734&scope=bot)\n[KOREANBOTS](https://koreanbots.dev/bots/726376311710548049) {Data.votes} ❤")
            await message.channel.send(embed=embed)

        if message.content.startswith(f"{prefix} 청소"):
            if message.guild.get_member(client.user.id).guild_permissions.manage_messages:
                if message.author.guild_permissions.manage_messages:
                    try:
                        number = message.content.split(' ')[2]
                        print(number)
                        await message.delete()
                        await message.channel.purge(limit = int(number))
                        embed = discord.Embed(title="채팅 청소 완료!", description=f"{int(number)}개의 메세지를 삭제했어요!\n\n||~~모조리 싹다 갈아엎어 주세요~~||")
                        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                        msg = await message.channel.send(embed=embed)
                        await asyncio.sleep(5)
                        await msg.delete()
                    except IndexError:
                        await message.channel.send("형식이 틀린거같아요... 형식은 ``시스비 청소 <삭제할 메세지 개수>``에요!")
                else:
                    await message.channel.send("당신은 권한이 없어요!\n필요 권한 : **``메세지 관리하기``**")
            else:
                await message.channel.send("제가 청소를 할 수 있는 권한을 가지고 있지 않아요!\n필요 권한 : **``메세지 관리하기``**")

        if message.content.startswith(f"{prefix} 핑퐁"):
            msg = message.content[7:]
            header = {
                'Authorization': pingpongauth,
                'Content-Type': 'application/json'
            }
            param = {
                'request': {
                    'query': msg
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

        if message.content.startswith(f"{prefix} 컴파일"):
            if message.author.id in owner:
                a=message.content[8:]
                try:
                    msg=await message.channel.send(embed=discord.Embed(color=0x2F3136, title="컴파일하는중...",description=f"""📥INPUT📥
```py
{a}
```
📤OUTPUT📤
```py
evaling...
```"""))
                    aa=await eval(a)
                except Exception as e:
                    await msg.edit(embed=discord.Embed(color=0x2F3136, title="컴파일 결과",description=f"""📥INPUT📥
                
```py
{a}          
```
📤OUTPUT📤
```py
{e}
```"""))
                    try:
                        aa = eval(a)
                    except Exception as e:
                        await msg.edit(embed=discord.Embed(color=0x2F3136, title="컴파일 결과",description=f"""📥INPUT📥
                
```py
{a}
```
📤OUTPUT📤
```py
{e}
```"""))
                    else:
                        await msg.edit(embed=discord.Embed(color=0x2F3136, title=f"컴파일 결과",description=f"""📥INPUT📥
```py
{a}
```
📤OUTPUT📤
```py
{aa}
```""")) 
                else:
                    await msg.edit(embed=discord.Embed(color=0x2F3136, title="컴파일 결과",description=f"""📥INPUT📥
```py
{a}
```
📤OUTPUT📤
```py
{aa}
```"""))
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.')

        if message.content.startswith(f"{prefix} 건답"):
            if message.author.id in owner:
                msg = message.content[7:]
                user = msg.split('&&')[0]
                description = msg.split('&&')[1]
                try:
                    await client.get_user(int(user)).send(f"{description}\n\n발신인 : {message.author}")
                except Exception as ex:
                    await message.channel.send(f"오류가 발생했어요! 아마도 DM을 못보내서 오류난거같은데 확인해보세요!\n오류 : {ex}")
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.')

    except Exception as ex:
        await client.get_channel(int(bug)).send(embed = discord.Embed(title="버그가 발생하였습니다.", description=ex).set_footer(text=message.author, icon_url=message.author.avatar_url))
        await message.channel.send(f"오류가 발생하였습니다.\n오류 내용 : {ex}")

async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"{prefix} 도움말 | 버전 {ver}"))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"{prefix} 도움말 | {len(client.guilds)}개의 서버"))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"{prefix} 도움말 | {len(client.users)}명의 유저"))
        await asyncio.sleep(10)
        Data = await Bot.getBot(client.user.id)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"{prefix} 도움말 | {Data.votes}개의 Koreanbots 하트"))
        await asyncio.sleep(10)
client.loop.create_task(my_background_task())

client.run(token)