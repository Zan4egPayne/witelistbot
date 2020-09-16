# Клан Волков Copyright 2020 By Zan4eg#5557
# Импорты библиотек

import discord
from discord.ext import commands
import asyncio
import datetime
from datetime import timedelta
import os
from Cybernator import Paginator as pag


PREFIX = 'c.' # Переменная префикса

Bot = commands.Bot( command_prefix = PREFIX ) # Установка префикса бота
@Bot.remove_command('help') #Удаление стандартной комманды help

# При загрузке бота
@Bot.event
async def on_ready():
    activity = discord.Game(name = "Клан Волков | c.help", url='https://twitch.com/zan4egpayne')
    await Bot.change_presence( status = discord.Status.online, activity = activity )
    print("Logged in as Клан Волков!")
    print("Клан Волков Copyright 2020 By Zan4eg#5557")
    print("Бот запущен и готов к работе!")
    while True:
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = "c.help") )
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = discord.Activity(type = discord.ActivityType.watching, name = f"{len(Bot.guilds)} серверов!") )
        await asyncio.sleep(8)
        await Bot.change_presence( status = discord.Status.online, activity = activity )

@commands.cooldown(1, 5, commands.BucketType.user)
@Bot.command()
async def ping(ctx):
    em = discord.Embed(title="".format(ctx.guild.name), description="", color=0x8a8c8f)
    em.set_author(name="")
    em.add_field(name="Ping", value='Понг! :ping_pong:', inline=True)
    em.add_field(name="MS", value=f'Пинг бота: **{ctx.bot.latency * 1000:,.2f}ms**', inline=True)
    await ctx.send(embed=em)

@commands.cooldown(1, 5, commands.BucketType.user)
@Bot.command()
async def team(ctx):
    em1 = discord.Embed(title="Наша команда".format(ctx.guild.name), description="", color=0x8a8c8f)
    em1.set_author(name="5/25")
    em1.add_field(name="Создатели", value='Zan4eg#5557 \n ! ЗОВУТ ВОЛОДЯ#9279', inline=True)
    em1.add_field(name="Волки", value='! (сосиска )крутой#4455 \n ! 𝙿𝚊𝚝𝚁𝟷𝙺 (Volk)#7846 \n Drafick#5570 \n ilyaka777(волк)#4450 \n Katorhen#4802', inline=True)
    em2 = discord.Embed(title="Наша команда".format(ctx.guild.name), description="", color=0x8a8c8f)
    em2.set_author(name="10/25")
    em2.add_field(name="Создатели", value='Zan4eg#5557 \n ! ЗОВУТ ВОЛОДЯ#9279', inline=True)
    em2.add_field(name="Волки", value='kreker(Волк)#1967 \n M¡llan¡um#7777 \n NikitaGame2007#8896 \n regzet56#3270 \n Salearka#5052', inline=True)
    em3 = discord.Embed(title="Наша команда".format(ctx.guild.name), description="", color=0x8a8c8f)
    em3.set_author(name="15/25")
    em3.add_field(name="Создатели", value='Zan4eg#5557 \n ! ЗОВУТ ВОЛОДЯ#9279', inline=True)
    em3.add_field(name="Волки", value='E N J O Y#5501 \n чипоолино#6164 \n (О_о) SLAVIK_GAMES#3333 \n [КВА]ALopitux#5489 \n DIAS147 (♠♥ВОЛК♣♦) ████████ 99%#2914', inline=True)
    em4 = discord.Embed(title="Наша команда".format(ctx.guild.name), description="", color=0x8a8c8f)
    em4.set_author(name="20/25")
    em4.add_field(name="Создатели", value='Zan4eg#5557 \n ! ЗОВУТ ВОЛОДЯ#9279', inline=True)
    em4.add_field(name="Волки", value='Donitolius#3437 \n FlayZer#0539 \n lololoahja#4436 \n MirbiTrack#8528 \n Nemo Reaper#9708', inline=True)
    em5 = discord.Embed(title="Наша команда".format(ctx.guild.name), description="", color=0x8a8c8f)
    em5.set_author(name="25/25")
    em5.add_field(name="Создатели", value='Zan4eg#5557 \n ! ЗОВУТ ВОЛОДЯ#9279', inline=True)
    em5.add_field(name="Волки", value='Кто-то#9656 \n XackerPro#7001 \n Бафик#7356 \n 𝓓𝓪𝓝𝓲𝓬𝓱 シ#9592 \n Егорну#5104', inline=True)    
    embeds = [em1, em2, em3, em4, em5]

    message = await ctx.send(embed=em1)
    page = pag(Bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()

# Навигация по командам
@Bot.command( pass_context = True )
async def help( ctx, amount = 1 ):
    await ctx.channel.purge( limit = amount )
    
    emb1=discord.Embed( title = 'Навигация по командам :pushpin:', colour= 0x31f5f5 )
    emb1.add_field( name = '``{}ping``'.format( PREFIX ), value = 'Узнать пинг бота.' )
    emb1.add_field( name = '``{}team``'.format( PREFIX ), value = 'Узнать состав нашей команды.' )
    embeds = [emb1]

    message = await ctx.send(embed=emb1)
    page = pag(Bot, message, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()
    
    
token = os.environ.get('BOT_TOKEN')
Bot.run( str(token) )