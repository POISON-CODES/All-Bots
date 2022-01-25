from db import db

from discord.ext.commands import command
from discord.ext.commands import Cog
from discord.ext.commands import has_permissions
from discord import Embed

class Administrator(Cog):
       def __init__(self, bot):
              self.bot = bot

       @command(name='prefix', aliases=['edit_prefix', 'change_prefix', 'new_prefix'], brief='Change bot prefix for server.')
       @has_permissions(manage_guild=True)
       async def prefix_change_command(self, ctx, new: str):
              f"""Allows you to change bot prefix for your Server.
              Syntax: ``{ctx.prefix}prefix [new_prefix]``
              
              Note: Feature for multiple prefixes will be added soon."""

              db.exec(f'UPDATE guilds SET PREFIX = ? WHERE GUILD_ID = ?', str(new), ctx.guild.id)
              e=Embed(description=f'New Prefix for this Server is `{new}`.', color=0xFFFFFF)
              await ctx.send(embed=e)


def setup(bot):
       bot.add_cog(Administrator(bot))