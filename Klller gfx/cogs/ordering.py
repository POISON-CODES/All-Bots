from io import BytesIO
import discord
from discord.ext import commands

from db import db
import cogs.config as cfg
import asyncio


class Confirm(discord.ui.View):
       def __init__(self):
              self.value=None
              super().__init__(timeout=None)

       @discord.ui.button(label = 'Yes', style=discord.ButtonStyle.green, custom_id='Yes')
       async def affirm(self, button = discord.ui.Button, interaction = discord.Interaction):
              self.value=True
              self.stop()


       @discord.ui.button(label='No', style=discord.ButtonStyle.red, custom_id='Red:No')
       async def effirm(self, button = discord.ui.Button, interaction = discord.Interaction):
              self.value=False
              self.stop()



class Buttons(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       @discord.ui.button(label = 'GFX', style=discord.ButtonStyle.gray, custom_id='Gray:GFX')
       async def GFX_button(self, button = discord.ui.Button, interaction = discord.Interaction):
              await interaction.response.send_message('Opening Your Ticket. Please wait a few seconds...', ephemeral = True)
              
              artists=interaction.guild.get_role(cfg.ARTISTS)
              ticket_supp=interaction.guild.get_role(cfg.SUPPORT)
              client_role=interaction.guild.get_role(cfg.CLIENT)
              community=interaction.guild.get_role(cfg.COMMUNITY)
              
              client=interaction.user
              categ= discord.utils.get(interaction.guild.categories, id=cfg.ORDER_TICK)
              channel=await categ.create_text_channel(name=f'GFX-{client.name}')
              await channel.edit(overwrites={})
              await channel.set_permissions(interaction.guild.default_role, view_channel=False)
              await channel.set_permissions(interaction.user, view_channel=True, send_messages=True)
              await channel.set_permissions(ticket_supp, view_channel=True, send_messages=True)
              await channel.set_permissions(artists, view_channel=True, send_messages=True)
              await channel.set_permissions(client_role, view_channel=False)
              await channel.set_permissions(community, view_channel=False)

              embed=discord.Embed(title = 'GFX Ticket', description=f'Ticket Opened by {client.mention}\nHelp will be with you shortly.\nCheck pricing and other information by using `{cfg.PREFIX}procedure`, `{cfg.PREFIX}price`, `{cfg.PREFIX}form`.', color=discord.Color(0x2F3136))
              embed.timestamp = discord.utils.utcnow()
              await channel.send(content=f'{client.mention} | {artists.mention}', embed= embed)

              await interaction.edit_original_message(content=f'Your Ticket has been Opened. Please move on to {channel.mention}')
              db.exec(f'INSERT INTO orders (CHANNEL, CLIENT, ARTIST) VALUES (?, ?, ?)', channel.id, client.id, 0)
              db.commit()
              db.commit()
              db.commit()
              await channel.send(f'This Channel is set registered for {client.mention}', delete_after = 5)

       @discord.ui.button(label = 'VFX', style=discord.ButtonStyle.gray, custom_id='Gray:VFX')
       async def VFX_button(self, button = discord.ui.Button, interaction = discord.Interaction):
              await interaction.response.send_message('Opening Your Ticket. Please wait a few seconds...', ephemeral = True)
              
              artists=interaction.guild.get_role(cfg.ARTISTS)
              ticket_supp=interaction.guild.get_role(cfg.SUPPORT)
              client_role=interaction.guild.get_role(cfg.CLIENT)
              community=interaction.guild.get_role(cfg.COMMUNITY)
              
              client=interaction.user
              categ= discord.utils.get(interaction.guild.categories, id=cfg.ORDER_TICK)
              channel=await categ.create_text_channel(name=f'VFX-{client.name}')
              await channel.edit(overwrites={})
              await channel.set_permissions(interaction.guild.default_role, view_channel=False)
              await channel.set_permissions(client, view_channel=True, send_messages=True)
              await channel.set_permissions(ticket_supp, view_channel=True, send_messages=True)
              await channel.set_permissions(artists, view_channel=True, send_messages=True)
              await channel.set_permissions(client_role, view_channel=False)
              await channel.set_permissions(community, view_channel=False)

              embed=discord.Embed(title = 'GFX Ticket', description=f'Ticket Opened by {client.mention}\nHelp will be with you shortly.\nCheck pricing and other information by using `{cfg.PREFIX}procedure`, `{cfg.PREFIX}price`, `{cfg.PREFIX}form`.', color=discord.Color(0x2F3136))
              embed.timestamp = discord.utils.utcnow()
              await channel.send(content=f'{client.mention} | {artists.mention}', embed= embed)

              await interaction.edit_original_message(content=f'Your Ticket has been Opened. Please move on to {channel.mention}')
              db.exec(f'INSERT INTO orders (CHANNEL, CLIENT, ARTIST) VALUES (?, ?, ?)', channel.id, client.id, 0)
              db.commit()
              db.commit()
              db.commit()
              db.commit()
              await channel.send(f'This Channel is set registered for {client.mention}', delete_after = 5)


class Orders(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
                
                
       @commands.command(help='```Gives all of the message in the current channel in a text file.```', aliases=['ts'])
       @commands.has_permissions(kick_members = True)
       async def transcript(self, ctx):
              messages=await ctx.channel.history(oldest_first=True, limit=999999).flatten()
              cont=''
              for i in range(len(messages)):
                     if messages[i].author.bot==True:
                            continue
                     cont=cont+f'{messages[i].author.name} : {messages[i].content}\n'

              file=open('transcript.txt', 'w')
              file.write(cont)
              file.close()
              buffer=BytesIO(cont.encode('utf-8'))
              file = discord.File(buffer, filename='transcript.txt')
              await ctx.send(file=file)       

       @commands.command(name='OrderButton', hidden = True)
       @commands.has_permissions(administrator=True)
       async def order_button(self, ctx):
              """Sends Order Button."""
              embed=discord.Embed(title ='Place Order', description=f'Select Your order Type from buttons below to place an order')
              embed.timestamp = discord.utils.utcnow()

              view=Buttons()

              await ctx.send(embed = embed, view=view)

       @commands.command(name='claim')
       async def claim_command(self, ctx):
              """```Claims an order. Only works in Ticket Channels.
              Can only be claimed by users having ╠═・GFX ARTIST・═╣.
              To override this command, administrator can user `assign` command to assign the project to another artist.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     pass
              else:
                     await ctx.send('This is not a ticket in my records.')
                     return

              artist=db.field('SELECT ARTIST FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              if artist==0:
                     pass
              else:
                     await ctx.send(f'This order was already claimed by <@{artist}>', delete_after = 10)
                     return

              artists=ctx.guild.get_role(cfg.ARTISTS)
              ticket_supp=ctx.guild.get_role(cfg.SUPPORT)
              client_role=ctx.guild.get_role(cfg.CLIENT)
              community=ctx.guild.get_role(cfg.COMMUNITY)

              if not artists in ctx.author.roles:
                     await ctx.send('You are not an artist you cannot claim this order.')
                     return
              
              embed=discord.Embed(title = 'Order Claimed.', description=f'Your order in <#{ctx.channel.id}> was claimed by {ctx.author.mention}.', color=0x00FF00)
              embed.timestamp = discord.utils.utcnow()
              client_id=db.field('SELECT CLIENT FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              client=ctx.guild.get_member(client_id)
              try:
                     await client.send(embed = embed)
              except:
                     pass
              
              await ctx.channel.set_permissions(ctx.author, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(artists, view_channel=False)
              await ctx.channel.set_permissions(ticket_supp, view_channel=False)

              db.exec(f'UPDATE orders SET ARTIST = ? WHERE CHANNEL = ? AND CLIENT = ?', ctx.author.id, ctx.channel.id, client_id)
              db.commit()

              await ctx.send(f'Successfully Claimed')

       @commands.command(name='unclaim')
       async def unclaim_ticket(self,ctx):
              """```Unclaims an order. Only works in Ticket Channels.
              Can only be unclaimed by the artist who claimed the ticket.
              To override the command, administrators can user `revoke` command to remove an artist from a project and assign another artist in case of unavailability of the artist.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     pass
              else:
                     await ctx.send('This is not a ticket in my records.')
                     return


              artists=ctx.guild.get_role(cfg.ARTISTS)
              ticket_supp=ctx.guild.get_role(cfg.SUPPORT)
              client_role=ctx.guild.get_role(cfg.CLIENT)
              community=ctx.guild.get_role(cfg.COMMUNITY)

              artist_id=db.field('SELECT ARTIST FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              if artist_id==0:
                     await ctx.send('This order was never claimed.', delete_after = 10)
                     return
              
              if not ctx.author.id == artist_id:
                     await ctx.send('Only the Artist who claimed the Order can Unclaim it.', delete_after = 10)
                     return

              
              db.exec(f'UPDATE orders SET ARTIST = ? WHERE CHANNEL = ?', 0, ctx.channel.id)
              db.commit()

              embed=discord.Embed(title = 'Order Unclaimed.', description=f'You successfully unclaimed this order, a new artist may now be assigned.', color= discord.Color(0x2F3136))
              embed.timestamp = discord.utils.utcnow()

              client_id=db.field('SELECT CLIENT FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              client=ctx.guild.get_member(client_id)

              await ctx.send(embed=embed)
              await ctx.channel.edit(overwrites={})
              await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
              await ctx.channel.set_permissions(client, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(ticket_supp, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(artists, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(client_role, view_channel=False)
              await ctx.channel.set_permissions(community, view_channel=False)

              await ctx.channel.send(content=f'{ticket_supp.mention} Please Assign another artist to **{client.name}**.')

       @commands.command(name='receipt', aliases=['reciept', 'complete'])
       async def complete_command(self, ctx):
              """```Complete an order and print the receipt for the same.
              **Note:** You will only have 300 seconds to submit the order details.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     pass
              else:
                     await ctx.send('This is not a ticket in my records.')
                     return

              client_id, artist_id = db.record('SELECT CLIENT, ARTIST FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              if artist_id==None or 0:
                     await ctx.send(f'In my records, this Order was never claimed. Claim this order by `{ctx.prefix}claim`.')
                     return

              if not artist_id==ctx.author.id:
                     await ctx.send(f'This Order was claimed by <@{artist_id}>. Only they can complete it.')
                     return

              artist=ctx.guild.get_member(artist_id)
              client= ctx.guild.get_member(client_id)

              embed=discord.Embed(title='Order Receipt', description=f'This is receipt of GFX/VFX order placed by <@{client_id}> and completed by <@{artist_id}>.', color= discord.Color(0x00FF00))
              embed.add_field(name ='ORDER DETAILS', value="""```Enter Order Details below this embed.
Example: 
Order Type : [The order type]
Order Style : [The Order Style]
Payment Method : [Example: invites, gpay, etc...]
Amount : [Example 2 invites/100 Rs./ etc...]```""", inline=False)
              embed.set_footer(text=f'{ctx.author.name} | {ctx.author.id}', icon_url=ctx.author.avatar.url if ctx.author.avatar is not None else (ctx.guild.icon.url if ctx.guild.icon else ctx.author.avatar.url))
              em=await ctx.send(embed = embed)
              await ctx.send('Enter Order details within (300 seconds).')
              def check(msg):
                     return msg.author.id == ctx.author.id and msg.channel == ctx.channel

              try:
                     details=await self.bot.wait_for('message', check=check, timeout=300)
                     embed.set_field_at(0, name='ORDER DETAILS', value=f'**ARTIST**: <@{artist_id}>\n**CLIENT:** <@{client_id}>\n{details.content}.', inline=False)
                     await em.edit(embed = embed)
                     await ctx.send(f'Enter **LINK** the design. `[Videos are currently under development.]`')
                     link= await self.bot.wait_for('message', check=check, timeout=300)
                     if link.content.startswith('http'):
                            pass
                     else:
                            await ctx.send('Link Support is only available for links with `http` of `https` standards. Please Try again.')
                            return
              except asyncio.TimeoutError:
                     await em.delete()
                     await ctx.send('Timedout. Try again.')
                     return

              embed.set_image(url=link.content)
              view=Confirm()
              await em.delete()
              final=await ctx.send(embed = embed, view=view)
              await view.wait()
              if view.value==None:
                     await ctx.send('No input recieved. Try Again')
                     return
              elif view.value == True:
                     channel=ctx.guild.get_channel(cfg.COMPLETED)
                     await final.delete()
                     await ctx.send(embed=embed)
                     await channel.send(embed=embed)
                     return
              else:
                     await final.delete()
                     await ctx.send('Cancelled....')
                     return


       @commands.command(name='delete')
       async def close_channel(self, ctx):
              """```Deletes a Ticket Channel.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     pass
              else:
                     await ctx.send('This is not a ticket in my records.')
                     return

              db.exec('DELETE FROM orders WHERE CHANNEL=?',ctx.channel.id)
              db.commit()
              await ctx.send('Deleting channel in 10 seconds.')
              await asyncio.sleep(10)
              await ctx.channel.delete()
       
       @commands.command(name='assign')
       @commands.has_permissions(administrator=True)
       async def assign_artist(self, ctx, artist: discord.Member):
              """```Assigns a Ticket to an artist.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     pass
              else:
                     await ctx.send(f'This is not a ticket in my records. First run `{ctx.prefix}addc <client>` to add this channel as a ticket.')
                     return

              already=db.field('SELECT ARTIST FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              if already==0:
                     pass
              else:
                     await ctx.send(f'This channel is already assigned to **<@{already}>**. First run `{ctx.prefix}revoke` to revoke this ticket from the artist.')
                     return

              artists=ctx.guild.get_role(cfg.ARTISTS)
              if not artists in artist.roles:
                     await ctx.send('This user is not an artist')
                     return

              db.exec('UPDATE orders SET ARTIST = ? WHERE CHANNEL = ?', artist.id, ctx.channel.id)
              db.commit()

              ticket_supp=ctx.guild.get_role(cfg.SUPPORT)

              await ctx.channel.set_permissions(artist, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(artists, view_channel=False)
              await ctx.channel.set_permissions(ticket_supp, view_channel=False)

              await ctx.send(f'Successfully assigned this order to {artist.mention}') 


       @commands.command(name='revoke')
       @commands.has_permissions(administrator=True)
       async def revoke_ticket(self, ctx):
              """```Take away an order from an artist.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     pass
              else:
                     await ctx.send('This is not a ticket in my records.')
                     return

              artist=db.field('SELECT ARTIST FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              if artist==0:
                     await ctx.send('This Ticket was never claimed.')
                     return

              db.exec('UPDATE orders SET ARTIST = ? WHERE CHANNEL = ?', 0, ctx.channel.id)
              db.commit()

              client=db.field('SELECT CLIENT FROM orders WHERE CHANNEL = ?', ctx.channel.id)
              client=ctx.guild.get_member(client)

              artists=ctx.guild.get_role(cfg.ARTISTS)
              ticket_supp=ctx.guild.get_role(cfg.SUPPORT)
              client_role=ctx.guild.get_role(cfg.CLIENT)
              community=ctx.guild.get_role(cfg.COMMUNITY)


              await ctx.channel.edit(overwrites={})
              await ctx.channel.set_permissions(ctx.guild.default_role, view_channel=False)
              await ctx.channel.set_permissions(client, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(ticket_supp, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(artists, view_channel=True, send_messages=True)
              await ctx.channel.set_permissions(client_role, view_channel=False)
              await ctx.channel.set_permissions(community, view_channel=False)

              await ctx.send(f'Successfully revoked from <@{artist}>')

       @commands.command(name='addc')
       async def add_channel_to_db(self, ctx, client: discord.Member):
              """```Adds a non-ticket/non-registered channel as a ticket.```"""
              channels=db.column('SELECT CHANNEL FROM orders')
              if ctx.channel.id in channels:
                     await ctx.send('This channel is alrady a Ticket.')
                     return
              else:
                     pass

              artists=ctx.guild.get_role(cfg.ARTISTS)
              if not artists in ctx.author.roles:
                     await ctx.send('You are not an artist, you cannot execute this comamnd.')
                     return

              db.exec('INSERT INTO orders (CLIENT, CHANNEL) VALUES (?, ?)', client.id, ctx.channel.id)
              db.commit()
              await ctx.send(f'Channel Successfully added as Ticket with client marked as **{client.name}**.')

       @commands.command()
       async def procedure(self, ctx):
              """```Displays the procedure to place an order.```"""
              description = (f'Step 1: Open a ticket from <#{int(cfg.ORDER)}>\n'
                            f'In the ticket channel explain your order to the artist in the format given in `{cfg.PREFIX}form`.\n'
                            f'Wait for an artist to claim your Order. Once an artist claims your order, you will be notified in your DMs.\n'
                            f'After an artist has claimed your order, he/she will complete your order and notify you.\n'
                            f'In order to cancel your order, you can click **[Cancel]** Button at any point in time and the artists will be notified.\n'
                            f'In case the artist is unable to Complete your order, he/she will **[Unclaim]** your order and you need to wait till another artist accepts your request.\n'
                            f'In case of incompatibiliy, the artists may **[Reject]** your order and the ticket will be closed.')
              embed = discord.Embed(title = 'Procedure',description=description ,color = discord.Color(0x2F3136))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'Requested by {ctx.author.name} | {ctx.author.id}')
              await ctx.send(embed = embed)

       @commands.command()
       async def price(self, ctx):
              """```Displays the rough pricing for varity of work styles.```"""
              embed = discord.Embed(title = 'Pricing', description = f'Pricing for GFX/VFX\n'
                                                                      f'Note: These pricings may vary depending on your order.', color = discord.Color(0x2F3136))
              embed.add_field(name ='GFX', value = """1. PFP(ANYTYPE) - ₹50/6 INVITES
2.NON-POPOUT AVI - ₹30/4 INVITES
3. POPOUT AVI - ₹40/6 INVITES
4. DRIP / CHROME AVI - ₹60/8 INVITES
5.BANNER- ₹100/12 INVITES
6. HEADER- ₹100/12 INVITES
7.ROSTER - ₹80/14 INVITES
8. THUMBNAIL(ANY) - ₹60/10 INVITES
9.CONCEPT LOGO - ₹125/18 INVITES
10.MASCOT LOGO - ₹100/15 INVITES
11.POSTER - ₹50/10INVITES
12.STATIC OVERLAY- ₹140/20 INVITES
13. LINEUP PFPS (PACKS OF 8)- ₹200/20 INVITES

**VFX:**
1. INTRO/OUTRO- ₹150/17 INVITES
2. ANIMATED OVERLAY- ₹200/25 INVITES
3. ANIMATED LOGO - ₹150/17 INVITES
4. MONTAGE EDITING (60SECS) - ₹200

#HcOnTop""", inline = False)
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}')
              embed.timestamp= discord.utils.utcnow()
              embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url if ctx.guild.icon else ctx.author.avatar.url)
              await ctx.send(embed = embed)

       @commands.command()
       async def form(self, ctx):
              """```Displays the form for placing an order.```"""
              embed = discord.Embed(title = 'Order Form', description="""FORM:
1) what are u ordering?
2) payement method
3) example of what ur ordering""", color = discord.Color(0x2F3136))
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}')
              embed.timestamp= discord.utils.utcnow()
              embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url if ctx.guild.icon else ctx.author.avatar.url)
              await ctx.send(embed = embed)



def setup(bot):
       bot.add_cog(Orders(bot))