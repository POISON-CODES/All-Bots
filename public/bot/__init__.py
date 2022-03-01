import discord
from discord.ext import commands

from ..db import db
import time

class BotMain(commands.Bot):
        def __init__(self):
                super().__init__(command_prefix=self.get_prefix, intents=discord.Intents.all())


        def get_prefix(self, message):   
                prefix=db.field('SELECT PREFIX FROM prefixes WHERE GUILD_ID = ?', message.guild.id)
                return commands.when_mentioned_or(str(prefix))(self, message)

        
        async def on_ready(self):
                print(self.user.name)
                print(self.user.id)
                print('Logged in...')
                self.start_time=time.time()


        async def startup(self, VERSION):
                token=''
                self.VERSION=VERSION
                self.TOKEN=token
                self.run(token)