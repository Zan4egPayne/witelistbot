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
        
@Bot.command()
@commands.cooldown(1, 99999999999999999999, commands.BucketType.user)
async def whitelist(ctx, nick = None):
    channel = Bot.get_channel( 755862633172959283 )
    if nick is None:
        await ctx.send(f"**{ctx.author}**, укажите ник сервера майнкрафт \n Пример команды: ***m.whitelist ``Ник``***")
    else:
        await channel.send( 'whitelist add ' + nick )
        await ctx.send('Игрок под ником: ' + nick + ' был добавлен в вайтлист.')
    
token = os.environ.get('BOT_TOKEN')
Bot.run( str(token) )
