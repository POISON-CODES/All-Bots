from apscheduler.schedulers.asyncio import AsyncIOScheduler
from db import db

from discord.ext.commands import Bot as BotBase
from discord.ext.commands import when_mentioned_or
from discord import Intents


OWNER_IDS=[724283255959978057]

extensions=['jishaku',
              'bot.cogs.Admin',
              'bot.cogs.General']

def get_prefix(bot, message):
	prefix = db.field(f"SELECT PREFIX FROM guilds WHERE GUILD_ID = {message.guild.id}")
	return when_mentioned_or(str(prefix))(bot, message)

class Bot(BotBase):
       def __init__(self):

              self.READY=False
              self.schedular=AsyncIOScheduler()
              self.GUILD=None

              db.autosave(self.schedular)
              
              super().__init__(command_prefix=get_prefix, owner_ids=OWNER_IDS, intents=Intents.all())

       def run(self, version):
              self.VERSION=version

              with open('./bot/token', 'r', encoding='utf-8') as f:
                     self.TOKEN=f.read()

              print('running bot...')
              super().run(self.TOKEN, reconnect=True) 

       async def on_connect(self):
              print('Bot Connected')

       async def on_disconnect(self):
              print('Bot Disconnected')

       async def on_guild_join(self, guild):
              db.exec(f'INSERT INTO guilds (GUILD_ID, PREFIX) VALUES ({guild.id}, "+")')
              db.commit()

       async def on_ready(self):

              for ex in extensions:
                     try:
                            self.load_extension(ex)
                            print(f'Loaded {ex} cog.')
                     except Exception as e:
                            print(e)
                            print(f'Couldnt load {ex} cog')

       
              if not self.READY:
                     self.READY=True
                     self.GUILD=self.get_guild(921832080474800159)
                     self.schedular.start()


                     print('Bot is Online')

              

bot=Bot()