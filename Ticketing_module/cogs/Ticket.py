import discord
from discord.ext import commands
import asyncio
import asyncio
import cogs.config as cfg
from utils.embeds import PBEmbeds as e
import json

class Ticket(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              self.ticketnum=0
              super().__init__()

       @commands.command()
       async def create_ticket(self, ctx):
              with open('cogs/TicketConfig.json', 'r') as f:
                     data=json.load(f)

              if data[str(ctx.guild.id)]==None:
                     data[str(ctx.guild.id)]={"1": {}}
                     self.ticketnum=1
                     pass
              elif not data[str(ctx.guild.id)][2]==None:
                     embed=e.Err()
                     embed.description=f'You have exceeded your limit for free number of Tickets.'
                     await ctx.send(embed = embed)
                     return
              else:
                     self.ticketnum=2
                     data[str(ctx.guild.id)]['2']={}

              with open('cogs/TicketConfig.json','w') as f:
                            json.dump(data, f, indent = 4)
              if not ctx.author.has_guild_permissions(administrator=True):
                     title='Missing Permission'
                     desc=f'You do not have required Permissions to use this command `Administrator`'
                     await ctx.reply(embed = e.BE(title, desc))
                     return

              mg=await ctx.reply(embed=e.DescE(ctx, title=None, desc='```Enter number of types of ticket```'))
              count='0'
              def check(count):
                     return count.author==ctx.author and count.channel==ctx.channel
              try:
                     count=await self.bot.wait_for('message', check=check, timeout=300)
              except asyncio.TimeoutError:
                     await mg.edit(embed=e.TimeOUT())
                     return

              if not count.isdigit():
                     embed=e.Err()
                     e.description=f'``{count}`` is invalid Number. Please retry'
                     await ctx.send(embed=embed)
                     return
              if int(count)>5:
                     embed=e.DescE(desc=f'You cannot have more than 5 options in a Ticket Menu ``YET!!``.')
                     embed.set_footer(text=f'Option to add more than 5 options will be added soon.')
                     await count.message.reply(embed = embed)
                     return

              for i in range(int(count)):
                     await ctx.send()

              






def setup(bot):
       bot.add_cog(Ticket(bot))