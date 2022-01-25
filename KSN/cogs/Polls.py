import discord
from discord.ext import commands
import asyncio

class Polls(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              super().__init__()


       @commands.command(help='Generates a Poll in designated Channel.', aliases=['voting', 'opinions', 'fanselect'])
       @commands.has_permissions(administrator = True)
       async def poll(self, ctx, channel: discord.TextChannel):
              embed=discord.Embed(color=discord.Color(0xFFE100))
              def check(msg):
                     return msg.channel == ctx.channel and msg.author == ctx.author
              await ctx.send(f'Enter Title')
              titl=await self.bot.wait_for('message', check=check, timeout=300)
              embed.title= titl.content
              embed.description='\u200b'
              em=await ctx.send(embed = embed)
              await ctx.send('Enter Description.')
              desc=await self.bot.wait_for('message', check=check, timeout=300)
              embed.description=desc
              await em.edit(embed = embed)
              i=1    


       @poll.error
       async def poll_Err(self, ctx, error):
              if isinstance(error, asyncio.TimeoutError):
                     await ctx.send('Timeout. Please retry and answer faster.')
                     return


def setup(bot):
       bot.add_cog(Polls(bot))