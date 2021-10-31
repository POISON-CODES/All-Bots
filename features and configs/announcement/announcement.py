import discord
from discord import embeds
from discord import utils
from discord.ext import commands
from datetime import datetime
import time

class Announce(commands.Cog):
       def __init__(self, bot):
              self.bot=bot

       @commands.command()
       async def announce(self, ctx, channel: discord.TextChannel, *, args):
              #time.sleep(5)
              embed=discord.Embed(title=ctx.guild.name, description=args, color=discord.Color.random())
              embed.set_thumbnail(url=ctx.guild.icon)
              embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar.url)
              #embed.set_footer(text=datetime.utils.utcnow)

              await channel.send(embed=embed)


       @announce.error
       async def missingargument(self, ctx, error):
              if isinstance(error, commands.MissingRequiredArgument):
                     await ctx.send(f'Incorrect Usage.\n \nCorrect Usage: {ctx.prefix}announce `<channel>` `<Message>`')


def setup(bot):
       bot.add_cog(Announce(bot))