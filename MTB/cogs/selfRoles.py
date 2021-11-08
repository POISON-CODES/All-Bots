from datetime import time
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

class Game(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(emoji="<a:FREEFIRELOGO:861196262191398923>", style=discord.ButtonStyle.green, custom_id="FreeFire")
       async def FF(self, button = discord.ui.Button, interaction = discord.Interaction):
              FF = interaction.guild.get_role(int(cfg.FF))
              if FF in interaction.user.roles:
                     await interaction.user.remove_roles(FF, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {FF.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(FF, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {FF.mention}.', ephemeral = True)

       @discord.ui.button(emoji="<a:CODMLOGO:861196266583490601>", style=discord.ButtonStyle.green, custom_id="CODM")
       async def CODM(self, button = discord.ui.Button, interaction = discord.Interaction):
              FF = interaction.guild.get_role(int(cfg.CODM))
              if FF in interaction.user.roles:
                     await interaction.user.remove_roles(FF, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {FF.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(FF, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {FF.mention}.', ephemeral = True)

       @discord.ui.button(emoji="<a:PUBGPAN:861196264120385576>", style=discord.ButtonStyle.green, custom_id="BGMI")
       async def BGMI(self, button = discord.ui.Button, interaction = discord.Interaction):
              FF = interaction.guild.get_role(int(cfg.BGMI))
              if FF in interaction.user.roles:
                     await interaction.user.remove_roles(FF, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {FF.mention}.', ephemeral = True)
              else:
                     await interaction.user.add_roles(FF, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {FF.mention}.', ephemeral = True)
       
class Pings(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(emoji = '🎉', style = discord.ButtonStyle.green, custom_id = "GIVEAWAY")
       async def GIVEAWAY(self, button = discord.ui.Button, interaction = discord.Interaction):
              GA = interaction.guild.get_role(int(cfg.GIVEAWAY))
              if GA in interaction.user.roles:
                     await interaction.user.remove_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {GA.mention}', ephemeral = True)
              else:
                     await interaction.user.add_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {GA.mention}.', ephemeral = True)

       @discord.ui.button(emoji = '<a:CROSS:816546045210263592>', style = discord.ButtonStyle.green, custom_id = "ALLIANCE")
       async def ALLIANCE(self, button = discord.ui.Button, interaction = discord.Interaction):
              GA = interaction.guild.get_role(int(cfg.ALLIANCE))
              if GA in interaction.user.roles:
                     await interaction.user.remove_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {GA.mention}', ephemeral = True)
              else:
                     await interaction.user.add_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {GA.mention}.', ephemeral = True)

       @discord.ui.button(emoji = '<a:MTBLOGO:861300241797087312>', style = discord.ButtonStyle.green, custom_id = "STAFF")
       async def STAFF(self, button = discord.ui.Button, interaction = discord.Interaction):
              GA = interaction.guild.get_role(int(cfg.STAFF))
              if GA in interaction.user.roles:
                     await interaction.user.remove_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {GA.mention}', ephemeral = True)
              else:
                     await interaction.user.add_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {GA.mention}.', ephemeral = True)

       @discord.ui.button(emoji = '<a:aa5:760424510846795778>', style = discord.ButtonStyle.green, custom_id = "CLAN")
       async def CLAN(self, button = discord.ui.Button, interaction = discord.Interaction):
              GA = interaction.guild.get_role(int(cfg.CLAN))
              if GA in interaction.user.roles:
                     await interaction.user.remove_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Removed {GA.mention}', ephemeral = True)
              else:
                     await interaction.user.add_roles(GA, reason = "Self Roles.")
                     await interaction.response.send_message(f'Added {GA.mention}.', ephemeral = True)

       

              



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
              embed = discord.Embed(title = 'YOUR AGE', description=f"18<:9195_upvote:733231877376311336> - 18+\n"
                                                                      f'18<:2140_downvote:733231877087035473> - 18-', color=discord.Color.green())

              await ctx.send(embed=embed, view = view)

              view = Game()
              embed = discord.Embed(title = "YOUR GAME", description=f"FREE FIRE\n"
                                                                      f"<:CODM:797373006107901952> - CODM\n"
                                                                      f"<:groza:792846214335954975> - BGMI", color = discord.Color.green())

              await ctx.send(embed=embed, view = view)

              view = Pings()
              embed = discord.Embed(title = "PINGS", description=f":tada: - Giveaway Ping.\n"
                                                               f'<a:CROSS:816546045210263592> - No Alliance Ping.\n'
                                                               f'<:MTB:792844123945566238> - Staff Recruitment Ping.\n'
                                                               f'<a:aa5:760424510846795778> - Clan Recruitment Ping.', color = discord.Color.green())

              await ctx.send(embed=embed, view=view)



def setup(bot):
       bot.add_cog(Main(bot))