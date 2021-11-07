import discord
from discord.ext import commands
from discord.ui import view
import cogs.ROLES as cfg

class Game(discord.ui.View):
       def __init__(self):
              super().__init__(timeout= None)

       @discord.ui.button(label = 'CODM', style=discord.ButtonStyle.green, custom_id="CODM")
       async def CODM(self, button = discord.ui.Button, interaction = discord.Interaction):
              CODM = interaction.guild.get_role(int(cfg.CODM))
              if CODM in interaction.user.roles:
                     await interaction.user.remove_roles(CODM, reason = "SELF ROLES.")
                     await interaction.response.send_message(f'Removed {CODM.mention}.', ephemeral=True)
              else:
                     await interaction.user.add_roles(CODM, reason = "SELF ROLES.")
                     await interaction.response.send_message(f'Added {CODM.mention}', ephemeral=True)

       @discord.ui.button(label = "BGMI", style= discord.ButtonStyle.green, custom_id="BGMI")
       async def BGMI(self, button = discord.ui.Button, interaction = discord.Interaction):
              BGMI = interaction.guild.get_role(int(cfg.BGMI))
              if BGMI in interaction.user.roles:
                     await interaction.user.remove_roles(BGMI, reason = "SELF ROLES.")
                     await interaction.response.send_message(f'Removed {BGMI.mention}.', ephemeral=True)
              else:
                     await interaction.user.add_roles(BGMI, reason = "SELF ROLES.")
                     await interaction.response.send_message(f'Added {BGMI.mention}', ephemeral=True)

       @discord.ui.button(label = "FREE FIRE", style= discord.ButtonStyle.green, custom_id="FF")
       async def FF(self, button = discord.ui.Button, interaction = discord.Interaction):
              FF = interaction.guild.get_role(int(cfg.FF))
              if FF in interaction.user.roles:
                     await interaction.user.remove_roles(FF, reason = "SELF ROLES.")
                     await interaction.response.send_message(f'Removed {FF.mention}.', ephemeral=True)
              else:
                     await interaction.user.add_roles(FF, reason = "SELF ROLES.")
                     await interaction.response.send_message(f'Added {FF.mention}', ephemeral=True)

                     



class Main(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command()
       async def SR1(self, ctx):
              view = Game()
              embed = discord.Embed(title = f"Choose Game", description = f'<@&{cfg.CODM}>\n'
                                                                          f'<@&{cfg.BGMI}>\n'
                                                                          f'<@&{cfg.FF}>\n', color = discord.Color.green())
              
              await ctx.send(embed = embed, view = view)


def setup(bot):
       bot.add_cog(Main(bot))