import discord
from discord.ext import commands
import cogs.config as cfg
from cogs.verify import *

intents = discord.Intents.all()

bot = commands.Bot(command_prefix = commands.when_mentioned_or('+'), intents=intents)

@bot.event
async def on_ready():

       print(f'Logged in as {bot.user.name}')
       print(f'{bot.user.id}')
       bot.add_view(VerifyButton())

initial_extensions = ['cogs.verify',
                     f'cogs.about',
                     f'jishaku',]

for extension in initial_extensions:
       try:
              bot.load_extension(extension)
              print(f'Loaded {extension}')
       except:
              print(f'Couldnt load {extension}')

       # for extension in initial_extensions:
       #        bot.load_extension(extension)

bot.run(cfg.TOKEN)