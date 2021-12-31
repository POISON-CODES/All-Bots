import discord
from discord.ext import commands
import cogs.config as cfg
import json 

class BUTTON1(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label = 'Claim', style=discord.ButtonStyle.green, custom_id = 'Claim:green')
       async def Claim(self, button = discord.ui.Button, interaction = discord.Interaction):
              artists = interaction.guild.get_role(int(cfg.ARTISTS))
              if artists in interaction.user.roles:
                     pass
              else:
                     await interaction.response.send_message(f'You are not a valid artist in this server.\nOnly artists are allowed to claim an order.', ephemeral = True) 
                     return

              with open('cogs/orders.json', 'r') as f:
                     data = json.load(f)

              client = interaction.guild.get_member(int(data["CHANNELS"][str(interaction.channel.id)]))

              embed = discord.Embed(title ='ORDER CLAIMED', description = f'{client.mention} your order was accepted by our artist - {interaction.user.mention}.', color = discord.Color(0x2C2F33))
              embed.timestamp = discord.utils.utcnow()
              embed.set_author(name =interaction.user.name, icon_url=interaction.user.avatar.url)
              
              async for message in interaction.channel.history():
                     if message.author.id == int(cfg.BOT):
                            await message.delete()
              view=BUTTON2()
              msg = await interaction.channel.send(embed = embed, view = view)

              data["CURRENT"][str(client.id)] = interaction.user.id

              with open('cogs/orders.json', 'w') as f:
                     json.dump(data, f, indent = 4)

              embed.set_thumbnail(url=interaction.guild.icon)
              embed.color = discord.Color(0x00FF00)
              embed.add_field(name = 'Link',value = f'[You can view the message here]({msg.jump_url})')

              await client.send(embed=embed)
              await interaction.channel.edit(name=f'claimed-{client.name}')
              return

       @discord.ui.button(label='Reject', style=discord.ButtonStyle.blurple, custom_id = 'reject1:blurple')
       async def reject(self, button = discord.ui.Button, interaction = discord.Interaction):
              artists = interaction.guild.get_role(int(cfg.ARTISTS))
              if artists in interaction.user.roles:
                     pass
              else:
                     await interaction.response.send_message(f'Oops you dont have the permissions to reject an order.', ephemeral = True)


              embed = discord.Embed(title = 'Order Rejected', description = f'Your Order in **{interaction.guild.name}** was cancelled by **{interaction.user.name}**', color=discord.Color(0xFF1100))
              embed.timestamp = discord.utils.utcnow()
              embed.set_thumbnail(url=interaction.guild.icon)
              embed.set_footer(text = f'{interaction.guild.name} | {interaction.guild.id}')

              with open('cogs/orders.json', 'r') as f:
                     data = json.load(f)

              client = interaction.guild.get_member(int(data["CHANNELS"][str(interaction.channel.id)]))
              await client.send(embed = embed)
              await interaction.channel.delete()
              
              data['CHANNELS'].pop(str(interaction.channel.id))

              with open('cogs/orders.json', 'w')as f:
                     json.dump(data, f, indent = 4)

              return


       @discord.ui.button(label='Cancel', style=discord.ButtonStyle.danger, custom_id='cancel1:red')
       async def cancel(self, button = discord.ui.Button, interaction = discord.Interaction):
              with open('cogs/orders.json', 'r') as f:
                     data= json.load(f)
              artists = interaction.guild.get_role(int(cfg.ARTISTS))

              if interaction.user.id == int(data['CHANNELS'][str(interaction.channel.id)]):
                     pass
              else:
                     if artists in interaction.user.roles:
                            pass 
                     else:
                            await interaction.response.send_message(f'You did not open this ticket and neither are an artist.\nPlease ask the owner of the ticket or any moderator to close the ticket instead.', ephemeral = True)
                            return
              await interaction.response.send_message(f'This ticket was cancelled.')
              await interaction.channel.delete(delay=10)

              data['CHANNELS'].pop(str(interaction.channel.id))
              with open('cogs/orders.json', 'w') as f:
                     json.dump(data, f, indent = 4)


class BUTTON2(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label = 'Complete', style=discord.ButtonStyle.green, custom_id = 'complete:green')
       async def complete(self, button = discord.ui.Button, interaction = discord.Interaction):
              pass

       @discord.ui.button(label='Unclaim', style=discord.ButtonStyle.blurple, custom_id='unclaim:blurple')
       async def claim(self, button = discord.ui.Button, interaction = discord.Interaction):
              pass

       @discord.ui.button(label='Reject', style=discord.ButtonStyle.blurple, custom_id = 'reject2:blurple')
       async def reject(self, button = discord.ui.Button, interaction = discord.Interaction):
              pass
              
       @discord.ui.button(label='Cancel', style=discord.ButtonStyle.danger, custom_id='cancel2:red')
       async def cancel(self, button = discord.ui.Button, interaction = discord.Interaction):
              pass