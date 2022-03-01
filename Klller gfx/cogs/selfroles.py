import discord
from discord.ext import commands

class ReactionRoles(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.Cog.listener()
       async def on_raw_reaction_add():
              pass



def setup(bot):
       bot.add_cog(ReactionRoles(bot))