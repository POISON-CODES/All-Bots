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

       @discord.ui.button(emoji = "♀️", style= discord.ButtonStyle.green, custom_id="FEMALE")
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

                     
class Age(discord.ui.View):
       def __init__(self):
              super().__init__(timeout = None)
       
       @discord.ui.button(emoji="<a:18plus:861193130283368448>", style = discord.ButtonStyle.danger, custom_id="18plus")
       async def ELDER(self, button = discord.ui.Button, interaction = discord.Interaction):
              elder = interaction.guild.get_role(int(cfg.ELDER))
              kids = interaction.guild.get_role(int(cfg.KIDS))

              if elder in interaction.user.roles:
                     await interaction.user.remove_roles(elder, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {elder.mention}.', ephemeral = True)

              elif kids in interaction.user.roles:
                     await interaction.user.remove_roles(kids, reason = "Self Roles Buttons. ")
                     await interaction.user.add_roles(elder, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {kids.mention} and added {elder.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(elder, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Added {elder.mention}.', ephemeral = True)

       @discord.ui.button(emoji="<a:18minus:861193130421780480>", style = discord.ButtonStyle.green, custom_id="18minus")
       async def KID(self, button = discord.ui.Button, interaction = discord.Interaction):
              elder = interaction.guild.get_role(int(cfg.KIDS))
              kids = interaction.guild.get_role(int(cfg.ELDER))

              if elder in interaction.user.roles:
                     await interaction.user.remove_roles(elder, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {elder.mention}.', ephemeral = True)

              elif kids in interaction.user.roles:
                     await interaction.user.remove_roles(kids, reason = "Self Roles Buttons. ")
                     await interaction.user.add_roles(elder, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Removed {kids.mention} and added {elder.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(elder, reason = "Self Roles Buttons. ")
                     await interaction.response.send_message(f'Added {elder.mention}.', ephemeral = True)

       



class Main(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command()
       async def SR1(self, ctx):
              view = Gender()
              embed = discord.Embed(title = "YOUR GENDER", description = f':male_sign:  -->>  Male\n'
                                                                    f'♀️  -->>  Female.', color = discord.Color.green())
       
              await ctx.send(embed = embed, view = view)

              view = Age()
              embed = discord.Embed(title = 'YOUR AGE', description=f"<a:18plus:861193130283368448> - 18+,\n"
              f'<a:18minus:861193130421780480> - 18-', color=discord.Color.green())

              await ctx.send(embed=embed, view = view)





def setup(bot):
       bot.add_cog(Main(bot))