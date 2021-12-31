import discord
from discord.ext import commands
from cogs.buttons import *
import json
import cogs.config as cfg

class ORDERBUTTON(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label='Place an Order', style=discord.ButtonStyle.grey, custom_id='Place:grey')
       async def ORDER(self, button = discord.ui.Button, interaction = discord.Interaction):
              channel = await interaction.guild.create_text_channel(name = f'Unclaimed-{interaction.user.name}')
              artists = interaction.guild.get_role(int(cfg.ARTISTS))
              overwrites = {
                     interaction.user: discord.PermissionOverwrite(
                            send_messages=True,
                            view_channel=True,
                            manage_messages=False,
                            manage_channels=False,
                            manage_permissions=False
                     ),
                     artists: discord.PermissionOverwrite(
                            send_messages=True,
                            view_channel=True,
                            manage_messages=False,
                            manage_channels=False,
                            manage_permissions=False
                     ),
                     interaction.guild.default_role: discord.PermissionOverwrite(
                            send_messages=False,
                            view_channel=False,
                            manage_messages=False,
                            manage_channels=False,
                            manage_permissions=False
                     )

              }
              await channel.edit(overwrites=overwrites)

              #####################################################################
              with open('cogs/orders.json', 'r') as f:
                     data = json.load(f)

              data['CHANNELS'][str(channel.id)] = str(interaction.user.id)

              with open('cogs/orders.json','w') as f:
                     json.dump(data, f, indent = 4)
              ####################################################################


              embed = discord.Embed(title=f'Place Your Order', description=f'Place an order here.\nType `!procedure` to know the Procedure.\n`!price` to know basic price chart.\n`!category` to know different types of categories.\n`!form` to fill the form for our artists to understand your idea.', color = discord.Color(0x2C2F33))
              embed.set_footer(text = f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
              embed.set_thumbnail(url=interaction.guild.icon)
              embed.timestamp = discord.utils.utcnow()
              view=BUTTON1()
              await channel.send(embed = embed, view = view)
              await interaction.response.send_message(f'Your Ticket has been opened. {channel.mention}',ephemeral=True)

class ORDER(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command(hidden = True)
       @commands.has_permissions(administrator = True)
       async def ORDER(self, ctx):
              embed = discord.Embed(title = 'Place an Order', description='Click on the button to create a Ticket and Place an order.', color = discord.Color(0x2C2F33))
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}', icon_url = ctx.guild.icon.url)
              embed.set_thumbnail(url=ctx.guild.icon.url)
              view = ORDERBUTTON()
              await ctx.send(embed = embed, view= view)

def setup(bot):
       bot.add_cog(ORDER(bot))