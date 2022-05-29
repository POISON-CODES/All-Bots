import discord
from discord.ext import commands
import config as cfg
import time
from io import BytesIO
from typing import Union

class Confirmation(discord.ui.View):
       def __init__(self):
              self.value= None
              super().__init__(timeout=None)

       @discord.ui.button(label='Yes', style=discord.ButtonStyle.green)
       async def confrmation(self, button = discord.ui.Button, interaction = discord.Interaction):
              self.value=True
              return self.value
       @discord.ui.button(label='No', style=discord.ButtonStyle.red)
       async def deny(self, button = discord.ui.Button, interaction = discord.Interaction):
              self.value=False
              return self.value

class Tickets(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              super().__init__()

       @commands.command(hidden = True)
       @commands.has_permissions(administrator = True)
       async def TICK(self, ctx):
              embed = discord.Embed(title = 'Tickets', description= f'Select the tickets Options below to Open a Ticket', color=discord.Color(0xFFE100))
              # embed.set_thumbnail(url=ctx.guild.icon.url)
              embed.set_author(name =f'{ctx.guild.name}', icon_url=ctx.guild.icon.url)
              embed.set_image(url='https://cdn.discordapp.com/attachments/868880669437227038/976801053855064134/tickets.png')
              # embed.set_footer(text=f'{ctx.guild.name} | {ctx.guild.id}', icon_url = ctx.guild.icon.url)
              # embed.timestamp = discord.utils.utcnow()
              view=DropDown()
              await ctx.send(embed = embed, view=view)

       @commands.command(help=f'Deletes the Ticket Channel.')
       @commands.has_permissions(kick_members = True)
       async def close(self, ctx):
              embed=discord.Embed(title=f'Closed', description=f'Ticket Closed By {ctx.author.mention}', color=discord.Color(0xFFE100))
              embed.set_footer(text = f'Deleting channel in 15 seconds.')
              await ctx.channel.send(embed = embed)
              time.sleep(15)
              await ctx.channel.delete()  

       @commands.command(help=f'Adds a user to the Channel.', aliases=['adduser'])
       @commands.has_permissions(kick_members = True)
       async def add(self, ctx, user: Union[discord.Member, discord.Role]):
              await ctx.channel.set_permissions(user, view_channel=True, send_messages=True)
              embed=discord.Embed(description=f'```**{user.name}** was added to this channel```', color=discord.Color(0xFFE100))
              embed.set_footer(text = f'{ctx.author.name}', icon_url=ctx.author.avatar.url if ctx.author.avatar is not None else ctx.guild.icon.url)
              await ctx.send(embed = embed)

       @commands.command(help='Removes a user from the channel.', aliases=['removeuser'])
       @commands.has_permissions(kick_members = True)
       async def remove(self, ctx, user:Union[discord.Member, discord.Role]):
              await ctx.channel.set_permissions(user, view_channel=False, send_messages=False)
              embed=discord.Embed(description=f'```**{user.name}** was removed from this channel```', color=discord.Color(0xFFE100))
              embed.set_footer(text = f'{ctx.author.name}', icon_url=ctx.author.avatar.url if ctx.author.avatar is not None else ctx.guild.icon.url)
              await ctx.send(embed = embed)

       @commands.command(help='Renames the channel', aliases=['rn'])
       @commands.has_permissions(kick_members = True)
       async def rename(self, ctx, *, name):
              await ctx.channel.edit(name=name)
              embed=discord.Embed(description=f'```Channels name was edited to {name}```', color=discord.Color(0xFFE100))
              embed.set_footer(text = f'{ctx.author.name}', icon_url=ctx.author.avatar.url if ctx.author.avatar is not None else ctx.guild.icon.url)
              await ctx.send(embed = embed)

       @commands.command(help='Gives all of the message in the current channel in a text file.', aliases=['ts'])
       @commands.has_permissions(kick_members = True)
       async def transcript(self, ctx):
              messages= [message async for message in ctx.channel.history(oldest_first=True, limit=999999)]
              cont=''
              for i in range(len(messages)):
                     if messages[i].author.bot==True:
                            continue
                     cont=cont+f'{messages[i].author.name} : {messages[i].content}\n'

              buffer=BytesIO(cont.encode('utf-8'))
              file = discord.File(buffer, filename=f'transcript-{ctx.channel.name}.txt')
              if "mod" in ctx.channel.name.lower():
                     channel = ctx.guild.get_channel(907521799246467072)
                     await channel.send(file=file)

              if "owner" in ctx.channel.name.lower():
                     channel = ctx.guild.get_channel(907521839562125312)
                     await channel.send(file=file)

              if "partnership" in ctx.channel.name.lower():
                     channel = ctx.guild.get_channel(907521799246467072)
                     await channel.send(file=file)

              if "cc" in ctx.channel.name.lower():
                     channel = ctx.guild.get_channel(907521757727043594)
                     await channel.send(file=file)

              messages= [message async for message in ctx.channel.history(oldest_first=True, limit=999999)]
              cont=''
              for i in range(len(messages)):
                     if messages[i].author.bot==True:
                            continue
                     cont=cont+f'{messages[i].author.name} : {messages[i].content}\n'

              buffer=BytesIO(cont.encode('utf-8'))
              file = discord.File(buffer, filename=f'transcript-{ctx.channel.name}.txt')

              await ctx.send(file=file)

class  DropDown(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=None)

       # options=[discord.SelectOption(label='Mod Ticket', emoji=f'<:moderators:933232926601134100>', description=f'Open Ticket to talk to Moderators.'),
       #        discord.SelectOption(label='Owner Ticket', emoji=f'<a:diamond:900668875992096818>', description=f'Open Ticket to talk to Owner of Kinsman Esports.'),
       #        discord.SelectOption(label=f'Partnership', emoji=f'<:partners:933232877934620752>', description=f'Open Ticket for Partnership'),
       #        discord.SelectOption(label=f'Content Creator', emoji='<:content_creator:933232854064848936>', description=f'Open Ticket for Content Creator Application.')]

       options=[discord.SelectOption(label='Mod Ticket', description=f'Open Ticket to talk to Moderators.'),
              discord.SelectOption(label='Owner Ticket', description=f'Open Ticket to talk to Owner of Kinsman Esports.'),
              discord.SelectOption(label=f'Partnership', description=f'Open Ticket for Partnership'),
              discord.SelectOption(label=f'Content Creator', description=f'Open Ticket for Content Creator Application.')]




       @discord.ui.select(placeholder=f'Select Ticket Type...', custom_id=f'TicketDrop', options=options)
       async def callback(self, interaction:discord.Interaction       , select: discord.ui.Select):
              selected=interaction.data['values'][0]
              staff=discord.utils.get(interaction.guild.roles, id=cfg.STAFF)
              mod=discord.utils.get(interaction.guild.roles, id=cfg.MOD)
              leader=discord.utils.get(interaction.guild.roles, id=cfg.LEADER)
              co_leader=discord.utils.get(interaction.guild.roles, id=cfg.CO_LEADER)
              owner=discord.utils.get(interaction.guild.roles, id=cfg.OWNER)
              admin=discord.utils.get(interaction.guild.roles, id=cfg.OWNER)
              head_mod=discord.utils.get(interaction.guild.roles, id=cfg.HEAD_MOD)
              if str(selected)=='Mod Ticket':
                     try:
                            msg=await interaction.response.send_message(f'<a:A_Loading:933264770621120552> Opening your ticket', ephemeral = True)
                            try:
                                   category=discord.utils.get(interaction.guild.categories, id=974345629755138098)
                                   chan=await category.create_text_channel(name=f'〢🎫│Moderators-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            except AttributeError:
                                   chan=await interaction.guild.create_text_channel(name=f'〢🎫│Moderator-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            
                            
                            await chan.edit(overwrites={})
                            await chan.set_permissions(interaction.guild.default_role, view_channel=False)
                            await chan.set_permissions(interaction.user, view_channel=True, send_messages=True)
                            await chan.set_permissions(mod, view_channel=True, send_messages=True)
                            await chan.set_permissions(head_mod, view_channel=True, send_messages=True)
                            await chan.set_permissions(admin, view_channel=True, send_messages=True)
                            
                            
                            embed=discord.Embed(title=f'Mod Ticket', description=f'This Ticket has been opened by {interaction.user.mention} for Moderator queries.', color=discord.Color(0xFFE100))
                            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar.url else None)
                            embed.set_footer(text=f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
                            embed.timestamp = discord.utils.utcnow()
                            embed.set_thumbnail(url=interaction.guild.icon.url)
                            await chan.send(f'{interaction.user.mention} | {mod.mention} | {head_mod.mention} | {admin.mention}',embed= embed)
                            await interaction.edit_original_message(content=f'<a:KSN_Verified:864195922219892768> Your Ticket has been opened, Please move to {chan.mention}')
                     except Exception as e:
                            print(e)
              elif str(selected)=='Owner Ticket':
                     try:
                            msg=await interaction.response.send_message(f'<a:A_Loading:933264770621120552> Opening your ticket', ephemeral = True)
                            try:
                                   category=discord.utils.get(interaction.guild.categories, id=974345561639641188)
                                   chan=await category.create_text_channel(name=f'〢🎫│Owner-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            except AttributeError:
                                   chan=await interaction.guild.create_text_channel(name=f'〢🎫│Owner-ticket-{interaction.user.name}')

                            await chan.edit(overwrites={})
                            await chan.set_permissions(interaction.guild.default_role, view_channel=False)
                            await chan.set_permissions(interaction.user, view_channel=True, send_messages=True)
                            await chan.set_permissions(admin, view_channel=True, send_messages=True)
                            
                            embed=discord.Embed(title=f'Owner Ticket', description=f'This Ticket has been opened by {interaction.user.mention} for Talking to Owner.', color=discord.Color(0xFFE100))
                            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar.url else None)
                            embed.set_footer(text=f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
                            embed.timestamp = discord.utils.utcnow()
                            embed.set_thumbnail(url=interaction.guild.icon.url)
                            
                            await chan.send(f'{interaction.user.mention} | {admin.mention}',embed= embed)
                            await interaction.edit_original_message(content=f'<a:KSN_Verified:864195922219892768> Your Ticket has been opened, Please move to {chan.mention}')
                     
                     except Exception as e:
                            print(e)
              elif str(selected)=='Partnership':
                     try:
                            msg=await interaction.response.send_message(f'<a:A_Loading:933264770621120552> Opening your ticket', ephemeral = True)
                            try:
                                   category=discord.utils.get(interaction.guild.categories, id=974345882831056967)
                                   chan=await category.create_text_channel(name=f'〢🎫│Partnership-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            except AttributeError:
                                   chan=await interaction.guild.create_text_channel(name=f'〢🎫│Partnership-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            await chan.edit(overwrites={})
                            await chan.set_permissions(interaction.guild.default_role, view_channel=False)
                            await chan.set_permissions(interaction.user, view_channel=True, send_messages=True)
                            await chan.set_permissions(staff, view_channel=True, send_messages=True)
                            embed=discord.Embed(title=f'Partnership', description=f'This Ticket has been opened by {interaction.user.mention} for Partnersip queries.', color=discord.Color(0xFFE100))
                            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar.url else None)
                            embed.set_footer(text=f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
                            embed.timestamp = discord.utils.utcnow()
                            embed.set_thumbnail(url=interaction.guild.icon.url)
                            await chan.send(f'{interaction.user.mention} | {staff.mention}',embed= embed)
                            await interaction.edit_original_message(content=f'<a:KSN_Verified:864195922219892768> Your Ticket has been opened, Please move to {chan.mention}')
                     except Exception as e:
                            print(e)
              elif str(selected)=='Content Creator':
                     try:
                            msg=await interaction.response.send_message(f'<a:A_Loading:933264770621120552> Opening your ticket', ephemeral = True)
                            try:
                                   category=discord.utils.get(interaction.guild.categories, id=974345696931098654)
                                   chan=await category.create_text_channel(name=f'〢🎫│CC-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            except AttributeError:
                                   chan=await interaction.guild.create_text_channel(name=f'〢🎫│CC-ticket-{interaction.user.name}')
                                   await chan.edit(topic=f'{interaction.user.id}')
                            await chan.edit(overwrites={})
                            await chan.set_permissions(interaction.guild.default_role, view_channel=False)
                            await chan.set_permissions(interaction.user, view_channel=True, send_messages=True)
                            await chan.set_permissions(head_mod, view_channel=True, send_messages=True)
                            await chan.set_permissions(admin, view_channel=True, send_messages=True)
                            await chan.set_permissions(leader, view_channel=True, send_messages=True)
                            embed=discord.Embed(title=f'CC Ticket', description=f'This Ticket has been opened by {interaction.user.mention} for Content Creator Application', color=discord.Color(0xFFE100))
                            embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url if interaction.user.avatar.url else None)
                            embed.set_footer(text=f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
                            embed.timestamp = discord.utils.utcnow()
                            embed.set_thumbnail(url=interaction.guild.icon.url)
                            await chan.send(f'{interaction.user.mention} | {head_mod.mention} | {admin.mention} | {leader.mention}',embed= embed)
                            await interaction.edit_original_message(content=f'<a:KSN_Verified:864195922219892768> Your Ticket has been opened, Please move to {chan.mention}')
                     except Exception as e:
                            print(e)
              
async def setup(bot):
       await bot.add_cog(Tickets(bot))