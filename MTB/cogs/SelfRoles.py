import discord
from discord.ext import commands
from discord.ui import view
import cogs.ROLES as cfg

class Gender(discord.ui.View):
       def __init__(self):
              super().__init__(timeout= None)

       @discord.ui.button(emoji='♂️', style=discord.ButtonStyle.green, custom_id="MALE")
       async def MALE(self, button = discord.ui.Button, interaction = discord.Interaction):
              male = interaction.guild.get_role(int(cfg.MALE))
              female = interaction.guild.get_role(int(cfg.FEMALE))

              if male in interaction.user.roles:
                     await interaction.user.remove_roles(male, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {male.mention}.', ephemeral = True)

              elif female in interaction.user.roles:
                     await interaction.user.remove_roles(female, reason = "Self Roles Buttons. ")
                     await interaction.user.add_roles(male, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {female.mention} and added {male.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(male, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Added {male.mention}.', ephemeral = True)

       @discord.ui.button(label = "♀️", style= discord.ButtonStyle.green, custom_id="FEMALE")
       async def FEMALE(self, button = discord.ui.Button, interaction = discord.Interaction):
              male = interaction.guild.get_role(int(cfg.MALE))
              female = interaction.guild.get_role(int(cfg.FEMALE))

              if female in interaction.user.roles:
                     await interaction.user.remove_roles(female, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {female.mention}.', ephemeral = True)

              elif male in interaction.user.roles:
                     await interaction.user.remove_roles(male, reason = "Self Roles Buttons. ")
                     await interaction.user.add_roles(female, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {male.mention} and added {female.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(female, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Added {female.mention}.', ephemeral = True)

                     



class Main(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command()
       async def SR1(self, ctx):
              view = Gender()
              embed = discord.Embed(title = "GENDER", description = f':male_sign:  -->>  Male\n'
                                                                    f'♀️  -->>  Female.', color = discord.Color.green())
       
              await ctx.send(embed = embed, view = view)


def setup(bot):
       bot.add_cog(Main(bot))