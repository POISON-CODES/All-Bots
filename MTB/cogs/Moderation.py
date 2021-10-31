import discord
from discord.ext import commands
import time
import asyncio

from discord.ui import view


class Confirmation(discord.ui.View):
       def __init__(self,bot):
              self.bot = bot

       @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
       async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
              return True


       @discord.ui.button(label='Cancel', style=discord.ButtonStyle.danger)
       async def red(self, button: discord.ui.Button, interaction: discord.Interaction):
              return False



class Moderation(commands.Cog):
       def __init__(self,bot):
              self.bot = bot


       @commands.command()
       @commands.has_permissions(administrator = True)
       async def kick(self, ctx, user: discord.User, reason = None):
              if reason == None:
                     reason = "No reason provided."

              embed = discord.Embed(title = "Kick", description = f'Are you sure you want to kick {user.mention}?\n Reason : ```{reason}```', color = discord.Color.red())
              value = await ctx.send(embed = embed, view = Confirmation)
              if value==True:
                     user.kick(reason = reason)

              else:
                     await ctx.send('Aborted!')



def setup(bot):
       bot.add_cog(Moderation(bot))