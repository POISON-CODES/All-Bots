import discord
from discord.ext import commands
import time
import cogs.config as cfg
import json
from cogs.ticket import *
from cogs.order import *
from cogs.buttons import *


intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('%'), intents=intents)
bot.case_insensitive = True


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'{bot.user.id}')
    bot.add_view(TICKET())
    bot.add_view(CLOSE())
    bot.add_view(ORDERBUTTON(bot))
    bot.add_view(BUTTON2(bot))
    bot.add_view(BUTTON1(bot))


@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send(f'my default prefix is `%` or <@!{bot.user.id}>')
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))


@bot.event
async def on_guild_join(guild):
    data = {}
    for member in guild.members:
        data[str(member.id)] = 0

    with open('cogs/values.json', 'r') as f:
        datajson = json.load(f)

    datajson[str(guild.id)] = data

    with open("cogs/values.json", "w") as f:
        json.dump(datajson, f, indent=4)


initial_extensions = ['jishaku',
                      f'cogs.ModMail',
                      f'cogs.ModMailcmds',
                      f'cogs.ticket',
                      f'cogs.order']

for extension in initial_extensions:
    try:
        bot.load_extension(extension)
        print(f'Loaded {extension}')
    except:
        print(f"Couldn't load {extension}")

# for extension in initial_extensions:
#        bot.load_extension(extension)


bot.run(str(cfg.TOKEN))
