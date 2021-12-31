import discord
from discord.ext import commands
import cogs.config as cfg

class VerifyButton(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label = 'VERIFY', style=discord.ButtonStyle.green, custom_id = 'Verify:green')
       async def verify(self, button = discord.ui.Button, interaction = discord.Interaction):
              community = interaction.guild.get_role(int(cfg.COMMUNITY))

              if community in interaction.user.roles:
                     await interaction.response.send_message(f'You are already verified.', ephemeral = True)

              else:
                     await interaction.user.add_roles(community, reason = 'Verify Button')
                     await interaction.response.send_message(f'You are now verified with {community.mention} Role.', ephemeral = True)


class Verify(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command(hidden = True)
       async def verify(self, ctx):
              poison = self.bot.get_user(int(cfg.OWNER))
              guild = self.bot.get_guild(int(cfg.GUILD))
              embed = discord.Embed(title = 'Verify', description = 'Click on the button to verify yourself and get access to the server.', color = discord.Color.green())
              if not guild.icon is None:
                     embed.set_thumbnail(url=ctx.guild.icon)
              embed.set_footer(text = f'Bot Developed by {poison.name}#{poison.discriminator}')
              embed.timestamp=discord.utils.utcnow()
              view = VerifyButton()
              await ctx.send(embed = embed, view = view)

def setup(bot):
       bot.add_cog(Verify(bot))