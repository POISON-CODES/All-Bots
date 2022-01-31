import discord
from discord.ext import commands
import cogs.config as cfg
from cogs.Tickets import *


bot=commands.Bot(case_insensitive=False, command_prefix=commands.when_mentioned_or(str(cfg.PREFIX)), intents=discord.Intents.all(), owner_ids=[724283255959978057])

@bot.event
async def on_ready():
       print(f'Logged in as {bot.user.name} | {bot.user.id}')
       bot.startup_time=int(time.time())
       bot.add_view(DropDown())



initial_extensions=['jishaku',
                     f'cogs.Tickets',
                     f'cogs.welcome',
                     f'cogs.General',
                     f'cogs.Scrims']

for extension in initial_extensions:
       try:
              bot.load_extension(extension)
              print(f'Loaded {extension}')
       except Exception as e:
              print(f'Couldnt load {extension}')
              print(e)


bot.run(cfg.TOKEN)