import discord
from discord.ext import commands

import time

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from discord.ext.commands import Bot as Botbase
from cogs.OS.Panels import MainPanel

from db import db

import config as cfg
import asyncio

initial_extensions=['jishaku',
                        'cogs.OS.Panels',
                        'cogs.OS.Pricings',
                        'cogs.tags']

class Bot(Botbase):
        def __init__(self):
                self.scheduler=AsyncIOScheduler()
                self.db=db                
                self.db.autosave(self.scheduler)
                self.scheduler.start()

                self.color=discord.Color(0x5AFFBB)

                super().__init__(command_prefix=commands.when_mentioned_or(cfg.PREFIX), owner_ids=[724283255959978057], intents=discord.Intents.all())


        async def on_message(self, message):
                if message.content.startswith(f"<@!{self.user.id}>") and len(message.content) == len(f"<@!{self.user.id}>"):
                        embed=discord.Embed(description=f'my default prefix is `{cfg.PREFIX}`',color=self.color)
                        await message.channel.send(embed=embed)
                await self.process_commands(message)


        async def on_ready(self):
                print(f'Logged in as {self.user.name} | {self.user.id}')
                self.startup_time=int(time.time())

                self.add_view(MainPanel())
                
                await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Graphics Studio'))

        async def setup(self):
                for extension in initial_extensions:
                        try:
                                await self.load_extension(extension)
                                print(f'Loaded {extension}')
                        except Exception as e:
                                print(f'Couldnt load {extension}')
                                print(e)

                        # await self.load_extension(extension)
                        # print(f'Loaded {extension}')
                                
                await super().start(token=str(cfg.TOKEN))