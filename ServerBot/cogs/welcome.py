import discord
from discord.ext import commands


import cogs.config as cfg

class Welcomer(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                super().__init__()


        @commands.Cog.listener()
        async def on_member_join(self, member: discord.Member ):
                if not member.guild is self.bot.guild:
                        return
                embed=discord.Embed(title='Welcome!', description=f"""__WELCOME TO {member.guild.name}__
> Enjoy your time here.

> Order Bots here <#952493014385852476>

> Get help with coding in <#952503446056079412>

> Get Support here <#952494035396878377>

> Take Self Roles in <#952480054141681674>
""", color=self.bot.COLOR)
                embed.timestamp = discord.utils.utcnow()

                welcome_channel=self.bot.get_channel(cfg.WELCOME_CHANNEL)

                await welcome_channel.send(content=f'{member.mention}', embed = embed)




async def setup(bot):
        await bot.add_cog(Welcomer(bot))