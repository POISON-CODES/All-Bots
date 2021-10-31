import discord
import sys
from discord import embeds
from discord.ext import commands
from discord.ext.commands import Greedy
import time
import json
'''from pretty_help import PrettyHelp'''


intents = discord.Intents.all()
intents.members = True




######################     JSON      #################
with open("config.json", "r") as f:
       config=json.load(f)

TOKEN=config['BOT']['TOKEN']
custom_prefix=config['GUILD']['PREFIX']




######################      JSON      #################
bot = commands.Bot(command_prefix=custom_prefix, intents=intents)

initial_extensions = ['cogs.modmail', 
                     'cogs.welcome',
                     'cogs.modmailcmds',
                     'cogs.buttons', 
                     'cogs.announcement']

@bot.event
async def on_message(message):
       if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
              embed = discord.Embed(description=f"My Default prefix here is ``{custom_prefix}``")
              await message.channel.send(embed=embed)
       await bot.process_commands(message)
    
@bot.event
async def on_ready():
       print('Bot is Ready!!')
       print(f'{bot.user}')
       print(f'{bot.user.id}')

if __name__ == '__main__':
       for extension in initial_extensions:
              try:
                     bot.load_extension(extension)
                     print(f'loaded {extension}')
              except:
                     print(f'Could not load {extension}')


bot.run(TOKEN)
