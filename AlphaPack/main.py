import discord
from discord.ext import commands
import cogs.config as cfg
import time
from cogs.verify import *

bot = commands.Bot(command_prefix=commands.when_mentioned_or('?'), intents=discord.Intents.all())

@bot.event
async def on_ready():

       print(f'Logged in as {bot.user.name}')
       print(f'{bot.user.id}')
       bot.add_view(VerifyButton())


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))

initial_extensions = ['jishaku',
                     f'cogs.ModMail',
                     f'cogs.ModMailcmds',
                     f'cogs.verify']

for extension in initial_extensions:
       try:
              bot.load_extension(extension)
              print(f'Loadeded {extension}')
       except:
              print(f'Couldnt load {extension}')

bot.run(cfg.TOKEN)