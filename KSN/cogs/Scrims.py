import discord
from discord.ext import commands
import asyncio
import cogs.config as cfg

class Scrims(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              super().__init__()

       @commands.command(aliases=['scrimsss', 'sss', 'post'], help='Posts Scrim ss in specified channel')
       async def results(self, ctx, channel: discord.TextChannel):
              role= ctx.guild.get_role(int(cfg.SCRIMSROLE))
              embed=discord.Embed(color=discord.Color(0xFFE100))
              if not role in ctx.author.roles:
                     embed.title=f'Missing Roles'
                     embed.description=f'You do not have <@&{cfg.SCRIMSROLE}> role to use this command.'
                     await ctx.send(embed = embed)
                     return
              
              await ctx.send('Enter title [ex: ``Team Beta vs Team Alpha (2-1)``]')
              def check(message):
                     return message.author==ctx.author and message.channel == ctx.channel
              try:
                     message= await self.bot.wait_for('message', check=check, timeout=300)
                     embed.description=message.content
                     msg=await ctx.send(embed = embed)
                     listofembeds=[embed]
                     await ctx.send(f'Enter **LINK** for screenshot (Please Enter 1 at a time) or `done` to Finish')
                     link= await self.bot.wait_for('message', check=check, timeout=300)
                     if link.content.startswith('http'):
                            pass
                     elif link.content.lower=='done':
                            await channel.send(embed=embed)
                            return
                     try:
                            embed.set_image(url=link.content)
                     except Exception as e:
                            print(e)
                            await ctx.send('Image could not be set. Waiting for error evaluation')
                            return 
                     await msg.edit(embed = embed)
                     var=True
                     while var is True:
                            await ctx.send('Enter Next **link** or type `done` to finish.')
                            link= await self.bot.wait_for('message', check=check, timeout=300)
                            if link.content.startswith('http'):
                                   embed=discord.Embed(color=discord.Color(0xFFE100))
                                   embed.set_image(url=link.content)
                                   listofembeds.append(embed)
                                   await msg.edit(embeds=listofembeds)
                            elif link.content.lower()=='done':
                                   await channel.send(embeds=listofembeds)
                                   await ctx.send('Done')
                                   var=False
                                   return
                                                     
                                   
                            
              except asyncio.TimeoutError:
                     await ctx.send('Timeout!')
                     return
def setup(bot):
       bot.add_cog(Scrims(bot))