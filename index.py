import discord
import asyncio
import datetime
import koreanbots
import os
import json
client = discord.Client()
with open('config.json') as f:
    data = json.load(f)
token = data['TOKEN']
ver = "Beta"
prefix = "시스비"
owner = 726350177601978438
Bot = koreanbots.Client(client, data['KOREANBOTS_TOKEN'])
ready = 726582051758800959
bug = 726646354407063595
botsv = 726646974501355573
건의 = 726647069548347432

@client.event
async def on_ready():
    print(client.user.name)
    print("ready")
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name=f"{client.user.name} 버전 {ver}"))
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
        if message.content == f"{prefix} 도움말" or message.content == f"{prefix} help":
            await message.channel.send(f"")
        if message.content == f"{prefix}" or message.content == f"{prefix} hellothisisverification":
            await message.channel.send(f"안녕하세요! 저는 {client.user.name}이에요! 시스비는 현재 {ver} 버전이고, 주인은 {client.get_user(726350177601978438)}(726350177601978438)입니다!\n저는 인공지능이에요! 접두사는 `{prefix}`입니다!")

        if message.content.startswith(f"{prefix} 정보"):
            if str(message.content[7:]) == '':
                user = message.author
                date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                status_dict: dict = {discord.Status.online: '<:status_online:726399733026914335> 온라인',
                    discord.Status.offline: '<:status_offline:726399732930576434> 오프라인',
                    discord.Status.idle: "<:status_idle:726399733081571348> 자리비움",
                    discord.Status.do_not_disturb: "<:status_dnd:726399732557283386> 방해금지"}
                user_status = status_dict[user.status]
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
                embed.add_field(name="현재 유저 상태", value=f"{user_status}", inline=False)
                await message.channel.send(embed=embed)
            else:
                try:
                    user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                    if user.bot == False:
                        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                        status_dict: dict = {discord.Status.online: '<:status_online:726399733026914335> 온라인',
                            discord.Status.offline: '<:status_offline:726399732930576434> 오프라인',
                            discord.Status.idle: "<:status_idle:726399733081571348> 자리비움",
                            discord.Status.do_not_disturb: "<:status_dnd:726399732557283386> 방해금지"}
                        user_status = status_dict[user.status]
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
                except:
                    user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                    if user.bot == False:
                        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                        status_dict: dict = {discord.Status.online: '<:status_online:726399733026914335> 온라인',
                            discord.Status.offline: '<:status_offline:726399732930576434> 오프라인',
                            discord.Status.idle: "<:status_idle:726399733081571348> 자리비움",
                            discord.Status.do_not_disturb: "<:status_dnd:726399732557283386> 방해금지"}
                        user_status = status_dict[user.status]
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
                            await message.guild.kick(user, reason = f"{message.author}에 의해서 {user}를 추방하였습니다.\n사유 : {reason}")
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
                            await message.guild.ban(await client.fetch_user(user), reason=f"{message.author}에 의해서 {un}를 차단하였습니다.\n사유 : {reason}")
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
            if message.guild.get_member(client.user.id).guild_permissions.ban_members == True:
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
                        await message.guild.unban(await client.fetch_user(user), reason=f"{message.author}에 의해서 {un}를 언밴하였습니다.\n사유 : {reason}")
                        await message.channel.send(f"``{message.author}``에 의해서 ``{un}``를 언밴하였습니다.\n사유 : {reason}")
                    except IndexError:
                        await message.channel.send("형식이 틀린거같아요... 형식은 ``시스비 밴 <유저 맨션>&&<사유>``에요!")
                    except:
                        await message.channel.send(f"언밴할 사람의 권한이 너무 높습니다.")
                else:
                    await message.channel.send("당신은 권한이 없어요!\n필요 권한 : **``멤버 차단하기``**")
            else:
                await message.channel.send("제가 밴을 할 수 있는 권한을 가지고 있지 않아요!\n필요 권한 : **``멤버 차단하기``**")

        if message.content.startswith(f"{prefix} 건의"):
            if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                await message.channel.send("건의사항을 입력해주세요.")
            else:
                msg = message.content[7:]
                await client.get_channel(int(건의)).send(embed = discord.Embed(title="건의가 들어왔어요!", description=msg).set_footer(text=message.author, icon_url=message.author.avatar_url))
                await message.channel.send(f"{message.author.mention}님! 건의가 완료되었습니다!")
                try:
                    await message.delete()
                except:
                    pass

        if message.content == f"{prefix} 오픈소스":
            await message.channel.send(embed = discord.Embed(colour=0xff00, title="Sisby OPEN SOURCE", description=f"여기에는 Sisby의 오픈소스가 담겨있어요!\n[여기를 확인해보세요!](https://github.com/samsunghappytree123/Sisby)").set_footer(text=message.author, icon_url=message.author.avatar_url))

    except Exception as ex:
        await message.channel.send(f"오류가 발생하였습니다.\n오류 내용 : {ex}")
        await client.get_channel(int(bug)).send(embed = discord.Embed(title="버그가 발생하였습니다.", description=ex).set_footer(text=message.author, icon_url=message.author.avatar_url))

client.run(token)