import discord
from discord.ext import commands
import time
import asyncio
import cogs.config as cfg


class TICKET(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label = 'Ticket', style=discord.ButtonStyle.green, custom_id = 'Ticket:green')
       async def ticketopen(self, button = discord.ui.Button, interaction = discord.Interaction):
              ticket = await interaction.guild.create_text_channel(name = f'ticket-{interaction.user.name}')
              overwrites = {
              interaction.guild.default_role: discord.PermissionOverwrite(
              read_messages=False,
              view_channel=False,
              ),
              interaction.user: discord.PermissionOverwrite(
                     read_messages=True,
                     send_messages=True,
              )}
              await ticket.edit(overwrites=overwrites)

              await interaction.response.send_message(f'Your Ticket has been opened. Please move to {ticket.mention}', ephemeral = True)
              await ticket.send(f'{interaction.user.mention} Help will be with you shortly.')
              embed = discord.Embed(title = f'{interaction.user.name}', description = f'This ticket is opened by {interaction.user.mention}.', color = discord.Color(0x2C2F33))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
              view=CLOSE()
              await ticket.send(embed= embed, view = view)


class Ticket(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command(hidden = True)
       @commands.has_permissions(administrator = True)
       async def TICK(self, ctx):
              embed = discord.Embed(title = 'TICKET', description = f'PRESS THE BUTTON TO OPEN A TICKET', color = discord.Color(0x2C2F33))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}', icon_url = ctx.guild.icon.url)
              view= TICKET()
              await ctx.send(embed = embed, view = view)

class CLOSE(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label =  'CLOSE', style=discord.ButtonStyle.danger, custom_id = 'CLOSE:RED')
       async def closeticket(self, button = discord.ui.Button, interaction = discord.Interaction):
              await interaction.channel.send(f'This ticket was closed by {interaction.user.mention}')
              time.sleep(10)
              await interaction.channel.delete()

def setup(bot):
       bot.add_cog(Ticket(bot))