import discord
from discord.ext import commands
import cogs.config as cfg

class WELCOME(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.Cog.listener()
       async def on_member_join(self, member: discord.Member):

              description = f"""Hey {member.mention} , welcome to Hexagon Creative!

Check out <#942757231106084884> to know about us and always see the description of the channel and the pinned messages to know more about that particular channel.

Read and remember <#942757573994643517> of our server.

Must take the roles from <#943092517413482506> ."""

              embed = discord.Embed(title = 'Welcome', description = description, color = discord.Color(0x29F8FF))
              embed.timestamp = discord.utils.utcnow()
              embed.set_author(name=member.name, icon_url= member.avatar.url if member.avatar is not None else self.bot.user.avatar.url)
              embed.set_footer(text = 'Enjoy in this Server!')
              embed.set_image(url='https://tenor.com/view/welcome-yellow-text-gif-13515266')
              channel = member.guild.get_channel(cfg.WELCOME)
              await channel.send(embed = embed)


       # @commands.Cog.listener()
       # async def on_member_remove(self, member: discord.Member):
       #        description = (f'**{member.name}** just left us.\n'
       #                      f"We're now **{len(member.guild.members)}** members.\n")
       #        embed = discord.Embed(title = 'Farewell', description = description, color = discord.Color(0xFFFFFF))
       #        embed.timestamp = discord.utils.utcnow()
       #        embed.set_footer(text = f'{member.guild.name} | {member.guild.id}', icon_url = member.guild.icon.url)

       #        channel = member.guild.get_channel(cfg.FAREWELL)
       #        await channel.send(embed = embed)

def setup(bot):
       bot.add_cog(WELCOME(bot))