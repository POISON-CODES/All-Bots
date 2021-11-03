import discord
from discord import embeds 
from discord.ext import commands
from discord.ext.commands import Greedy
import json
import asyncio

class Games(discord.ui.View):
       def __init__(self, ctx):
              super().__init__(timeout=None)
              self.ctx = ctx
              
       @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
       async def BGMI(self, button: discord.ui.Button, interaction: discord.Interaction):
              await interaction.user.add_roles()

class SelfRoles(commands.Cog):

       def __init__(self, bot):
              self.bot = bot

       @commands.command()
       @commands.has_permissions(administrator = True)
       async def SR(self, ctx):




       

def setup(bot):
       bot.add_cog(SelfRoles(bot))