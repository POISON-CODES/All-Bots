import discord
from discord.ext import commands
from cogs.General import PartnerView

from cogs.Tickets import *

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from discord.ext.commands import Bot as Botbase

from db import db

import config as cfg
import asyncio

initial_extensions=['jishaku',
                     f'cogs.Tickets',
                     f'cogs.welcome',
                     f'cogs.General',
                     f'cogs.Giveaways',]
                #      f'cogs.Roles']

class Bot(Botbase):
        def __init__(self):
                self.scheduler=AsyncIOScheduler()
                self.db=db                
                self.db.autosave(self.scheduler)
                self.scheduler.start()

                super().__init__(command_prefix=commands.when_mentioned_or(cfg.PREFIX), owner_ids=[724283255959978057], intents=discord.Intents.all())


        async def on_message(self, message):
                if message.content.startswith(f"<@!{self.user.id}>") and len(message.content) == len(f"<@!{self.user.id}>"):
                        embed=discord.Embed(description=f'my default prefix is `{cfg.PREFIX}`',color=discord.Color(0xFFE100))
                        await message.channel.send(embed=embed)
                await self.process_commands(message)


        async def on_ready(self):
                print(f'Logged in as {self.user.name} | {self.user.id}')
                self.startup_time=int(time.time())
                self.add_view(DropDown())
                self.add_view(PartnerView(link=''))
                await self.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='KINSMEN ESPORTS'))

        async def setup(self):
                for extension in initial_extensions:
                        # try:
                        #         await self.load_extension(extension)
                        #         print(f'Loaded {extension}')
                        # except Exception as e:
                        #         print(f'Couldnt load {extension}')
                        #         print(e)

                        await self.load_extension(extension)
                        print(f'Loaded {extension}')
                                
                await super().start(token=str(cfg.TOKEN))