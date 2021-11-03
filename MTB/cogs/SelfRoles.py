import discord
from discord.ext import commands
from discord.ui import view

class SelfRoleDemo1(discord.ui.View):
       def __init__(self, ctx):
              self.ctx = ctx
              super().__init__(timeout= None)

       @discord.ui.button(emoji='<:CODMBR:797376126212374528>', style=discord.ButtonStyle.green, custom_id="CODMSR")
       async def CODM(self, button = discord.ui.Button, interaction = discord.Interaction):
              await interaction.response.send_message('CODM ROLE', ephemeral = True)

       @discord.ui.button(emoji="<:MTB:792844123945566238>", style= discord.ButtonStyle.primary, custom_id="MTBSR")
       async def MTB(self, button = discord.ui.Button, interaction = discord.Interaction):
              await interaction.response.send_message('MTB ROLE', ephemeral = True)


class Main(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command()
       async def SR1(self, ctx):

              view = SelfRoleDemo1(ctx = ctx)
              await ctx.send('SR1', view = view)


def setup(bot):
       bot.add_cog(Main(bot))