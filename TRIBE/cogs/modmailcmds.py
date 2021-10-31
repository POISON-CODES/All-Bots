from datetime import datetime
import discord
import sys
from discord import embeds
from discord.ext import commands
from discord.ext.commands import Greedy
import time
import json
import asyncio
from discord.role import Role


class ModMailCommands(commands.Cog):

       def __init__(self, bot):
              self.bot = bot

       @commands.command(brief="Replies to a user Ticket")
       async def reply(self, ctx, *, args):
              if len(args) > 1000:
                     await ctx.send('Message is too long!\nTry again with a shorter message.')
                     return

              embed=discord.Embed(title=f'{ctx.author.name} says:', description=args, color=discord.Color.red())
              embed.set_footer(text=f'{ctx.guild.name} | {ctx.guild.id}')
              
              for m in ctx.guild.members:
                     if m.id==int(ctx.channel.name):
                            await m.send(embed=embed)

       @reply.error
       async def noarg(self, ctx, error):
              if isinstance(error, commands.MissingRequiredArgument):
                     await ctx.send('No message given.')



       @commands.command(brief="Closes a Ticket")
       async def close(self, ctx, *, args=None):
              global description

              if args==None:
                     description='No Reason Given.'
              else:
                     description=args

              embed=discord.Embed(title=f'Ticket Closed',description=description, color=discord.Color.red())
              embed.set_footer(text=f'{ctx.guild.name} | {ctx.guild.id}')
              
              for m in ctx.guild.members:
                     if m.id==int(ctx.channel.name):
                            await m.send(embed=embed)

              await ctx.channel.delete()

def setup(bot):
       bot.add_cog(ModMailCommands(bot))