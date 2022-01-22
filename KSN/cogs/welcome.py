import discord
from discord.ext import commands
import cogs.config as cfg

class Welcomer(commands.Cog):
       def __init__(self, bot):
              super().__init__()

       
       @commands.Cog.listener()
       async def on_member_join(self, member: discord.Member ):
              embed=discord.Embed(title=f'<a:nitro:900703455759433778><a:diamond:900668875992096818> __KINSMEN ESPORTS__ <a:nitro:900703455759433778><a:diamond:900668875992096818>')
              embed.description=(f'Hey **{member.name}#{member.discriminator}**, Welcome to KINSMEN ESPORTS <a:KSN_Verified:864195922219892768>\n\n'
                                   f'⪦━━━━━━━━━━━━━━━━━━━━⪧\n\n'
                                   f'<a:redstar:900703292986912788><a:arrow:900668984494551080> Make sure to go through <#770628643381706752>,\nBreaking of any rules will lead to a mute/ban.\n\n'
                                   f'<a:redstar:900703292986912788><a:arrow:900668984494551080> Also do check <#858316361330982952> and take your roles.\n\n'
                                   f'<a:redstar:900703292986912788><a:arrow:900668984494551080> Interact with new people by talking in <#770665498450198529>.\n\n'
                                   f'<a:redstar:900703292986912788><a:arrow:900668984494551080>  If you are interested to join our clan then make sure to check out <#865431793611440188>.\n\n'
                                   f'⪦━━━━━━━━━━━━━━━━━━━━⪧\n\n'
                                   f'<a:diamond:900668875992096818><a:diamond:900668875992096818> **Thank You for joining our server and keep exploring our server** <a:diamond:900668875992096818><a:diamond:900668875992096818>')
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{member.guild.name} | {member.guild.id}')
              embed.color= discord.Color(0xFFE100)
              embed.set_thumbnail(url=member.avatar.url if not member.avatar is None else member.guild.icon.url)
              channel= member.guild.get_channel(int(cfg.WELCOME))
              await channel.send(content=f'{member.mention}',embed = embed)


def setup(bot):
       bot.add_cog(Welcomer(bot))