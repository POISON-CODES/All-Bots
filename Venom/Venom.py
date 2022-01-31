import discord
from discord.ext import commands
import time

bot= commands.Bot(command_prefix =commands.when_mentioned_or('?'), intents=discord.Intents.all())



@bot.event
async def on_ready():

       print(f'Logged in as {bot.user.name}')
       print(f'{bot.user.id}')


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))

initial_extensions = ['jishaku',
                     f'cogs.ModMail',
                     f'cogs.ModMailcmds']

for extension in initial_extensions:
       try:
              bot.load_extension(extension)
              print(f'Loadeded {extension}')
       except:
              print(f'Couldnt load {extension}')

bot.run('ODkyOTk0NTUyNzA3ODI5ODEx.YVU__A.MbG0HbsVtsNBMv0COpqpIV1ChQY')