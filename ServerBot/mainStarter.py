import discord
from discord.ext import commands
import jishaku
from discord import app_commands
import os
import asyncio


import cogs.config as cfg
from db import db




intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or(str(cfg.PREFIX)), intents=intents)




@bot.event
async def on_ready():
        bot.GUILD=bot.get_guild(cfg.GUILD)

        bot.ERROR_LOG=bot.get_channel(cfg.ERROR_LOG)

        bot.VERSION=cfg.VERSION

        bot.COLOR=0xFFFFFF

        bot.db=db
  
        print(f'Logged in as {bot.user.name}')

        print(f'{bot.user.id}')
  
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{bot.GUILD.name}'))
        await bot.tree.sync(guild=discord.Object(id=950744623897251900))



initial_extensions = ['jishaku',
                        'cogs.welcome',
                        'cogs.BotTicket',
                        'cogs.Tags',
                        'cogs.Slash']


async def main():
    async with bot:
        for extension in initial_extensions:
                await bot.load_extension(extension)
        
        
        await bot.start(cfg.TOKEN)
asyncio.run(main())