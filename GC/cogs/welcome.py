import discord
from discord.ext import commands
import cogs.config as cfg

class WELCOME(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.Cog.listener()
       async def on_member_join(self, member: discord.Member):

              description = (f'{member.mention} just joined the server. We now have {len(member.guild.members)}\n\n'
                            f'Hey, {member.mention} Thanks for joining **{member.guild.name}**\n\n'
                            f'Make sure to check <#{int(cfg.RULES)}>\n'
                            f'Order FX over at <#{int(cfg.ORDER)}>\n\n'
                            f'Thank you for joining.\n'
                            f'Hope you like your stay here.')

              embed = discord.Embed(title = 'Welcome', description = description, color = discord.Color(0xFFFFFF))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{member.guild.name} | {member.guild.id}', icon_url = member.guild.icon.url)

              channel = member.guild.get_channel(cfg.WELCOME)
              await channel.send(embed = embed)


       @commands.Cog.listener()
       async def on_member_remove(self, member: discord.Member):
              description = (f'**{member.name}** just left us.\n'
                            f"We're now **{len(member.guild.members)}** members.\n")
              embed = discord.Embed(title = 'Farewell', description = description, color = discord.Color(0xFFFFFF))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{member.guild.name} | {member.guild.id}', icon_url = member.guild.icon.url)

              channel = member.guild.get_channel(cfg.FAREWELL)
              await channel.send(embed = embed)

def setup(bot):
       bot.add_cog(WELCOME(bot))