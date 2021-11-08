import discord
import os
from discord import embeds
from discord.activity import Game
from discord.ext import commands
from discord.ext.commands import Greedy
import time
from cogs.selfRoles import *

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'logged in as {bot.user},{bot.user.id}')
    persistent_views_added = False
    if not persistent_views_added:
        bot.add_view(Game())
        persistent_views_added = True


@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send('my default prefix is `!`')
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))    


@bot.command()
#@commands.has_role('BOT-Admins') 
async def announce(ctx, channel: discord.TextChannel = None, *, args = None):

     """--announce 'mention channel' 'announcement'"""
    
     if channel == None and args == None:
          embed = discord.Embed(title = 'Invalid channel and Message', description = 'You missed the ``Channel`` and ``Message`` argument', color = discord.Color.red())
          embed.add_field(name = 'Try:', value = f'```{ctx.prefix}announce <mention channel here> <your message here>\nDo not include "<>".```', inline = False)
          
          await ctx.send(embed = embed)
    
     elif channel == None and args != None:
          embed = discord.Embed(title = 'Invalid Channel', description = 'You missed the ``Channel``argument', color = discord.Color.red())
          embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention Channel here> <your message here>\nDo not include "<>".```', inline = False)
          
          await ctx.send(embed = embed)
    
     elif channel != None and args == None:
          embed = discord.Embed(title = 'Invalid Message', description = 'You missed the ``Message``argument', color = discord.Color.red())
          embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention Channel here> <your message here>\nDo not include "<>".```', inline = False)
          
          await ctx.send(embed = embed)
    
     else:
          embed = discord.Embed(title = 'ANNOUNCEMENT', description = f'{args}', color = discord.Color.random())
          embed.set_thumbnail(url=ctx.guild.icon.url)
          
          await channel.send(embed = embed)
          '''if args.member.mentions > 0:
          for i in args.mentions:
            await ctx.send(i, delete_after = 2)
          await channel.send(args)'''

initial_extensions = ['cogs.modmail',
                    'cogs.modmailcmds', 
                    'cogs.selfRoles',
                    'cogs.memjoin']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f'loaded {extension}')
        except:
            print(f'Could not load {extension}')

bot.run('ODkxNzEyODM2MjE1MTI4MDY0.YVCWSw.d6Y7aNkyVbRX3Q-cA_oLebM-6HI')