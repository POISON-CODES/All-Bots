import discord
from discord.ext import commands

from cogs.OS.Logging import *

from db import dbb

import time

class FXPanel(discord.ui.View):
        def __init__(self):
                self.style='FX'
                super().__init__(timeout=None)
        
        @discord.ui.button(label='Paid Ticket', style=discord.ButtonStyle.grey, custom_id='PaidFX')
        async def Paid_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=932506029323866243)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                
                
                tc = await category.create_text_channel(name='Paid-Ticket-')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'fx')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)
                


        @discord.ui.button(label='Invite Ticket', style=discord.ButtonStyle.grey, custom_id='InvitesFX')
        async def Invites_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=918104010135834674)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                designer=discord.utils.get(interaction.guild.roles, id=977630895378939976)
                
                tc = await category.create_text_channel(name='Invite-Ticket-')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'fx')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

        @discord.ui.button(label='Booster Ticket', style=discord.ButtonStyle.grey, custom_id='BoosterFX')
        async def Booster_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=918104010135834674)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                designer=discord.utils.get(interaction.guild.roles, id=977630895378939976)
                
                tc = await category.create_text_channel(name='Booster-Ticket-')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'fx')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

        # @discord.ui.button(label='Giveaway Ticket', style=discord.ButtonStyle.grey, custom_id='GiveawayFX')
        # async def Give_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
        #         await interaction.response.send_message('svf', ephemeral=True)

class ApplicationPanel(discord.ui.View):
        def __init__(self):
                self.style='App'
                super().__init__(timeout=None)
        
        @discord.ui.button(label='Server Support Application', style=discord.ButtonStyle.grey, custom_id='PaidFX')
        async def Pai2d_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=977631102208450660)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                designer=discord.utils.get(interaction.guild.roles, id=977630854211854387)
                
                tc = await category.create_text_channel(name='Server Support Application')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'app')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

        @discord.ui.button(label='Designer Application', style=discord.ButtonStyle.grey, custom_id='InvitesFX')
        async def Invit4es_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=977631102208450660)
                support=discord.utils.get(interaction.guild.roles, id=977630891704721458)
                # designer=discord.utils.get(interaction.guild.roles, id=977630854211854387)
                
                tc = await category.create_text_channel(name='Designer Application')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'app')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                # await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

class ProgramPanel(discord.ui.View):
        def __init__(self):
                self.style='Prog'
                super().__init__(timeout=None)
        
        @discord.ui.button(label='Affiliation Program', style=discord.ButtonStyle.grey, custom_id='InvitesFX')
        async def Invittes_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=977631106515992637)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                # designer=discord.utils.get(interaction.guild.roles, id=977630854211854387)
                
                tc = await category.create_text_channel(name='Affiliation Program')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'prog')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                # await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

        @discord.ui.button(label='Developer Program', style=discord.ButtonStyle.grey, custom_id='BoosterFX')
        async def Boostesr_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=977631106515992637)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                # designer=discord.utils.get(interaction.guild.roles, id=977630854211854387)
                
                tc = await category.create_text_channel(name='Developer Program')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'prog')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                # await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

        @discord.ui.button(label='Content Creator Program', style=discord.ButtonStyle.grey, custom_id='GiveawayFX')
        async def Give_bfx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=977631106515992637)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                # designer=discord.utils.get(interaction.guild.roles, id=977630854211854387)
                
                tc = await category.create_text_channel(name='Content Creator Program')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'prog')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                # await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc)

class BotPanel(discord.ui.View):
        def __init__(self):
                self.style='Supp'
                super().__init__(timeout=None)
        
        @discord.ui.button(label='Order Bot', style=discord.ButtonStyle.grey, custom_id='GiveawayFX')
        async def Giv342e_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=932506029323866243)
                support=discord.utils.get(interaction.guild.roles, id=977630852433465364)
                designer=discord.utils.get(interaction.guild.roles, id=977630882749878282)
                
                tc = await category.create_text_channel(name='Bot Order')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'bot')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc) 

class SupportPanel(discord.ui.View):
        def __init__(self):
                self.style='Supp'
                super().__init__(timeout=None)
        
        @discord.ui.button(label='Server Support', style=discord.ButtonStyle.grey, custom_id='GiveawayFX')
        async def Giv36e_fx(self, interaction: discord.Interaction, button: discord.ui.Button):
                await interaction.response.defer(ephemeral=True)

                category=discord.utils.get(interaction.guild.categories, id=977631106515992637)
                support=discord.utils.get(interaction.guild.roles, id=977630887908888606)
                # designer=discord.utils.get(interaction.guild.roles, id=977630882749878282)
                
                tc = await category.create_text_channel(name='Bot')


                dbb.exec(f'INSERT INTO tickets (CHANNEL, CLIENT, OPEN_TIME, PANEL) VALUES (?, ?, ?, ?)', tc.id, interaction.user.id, time.time(), 'bot')
                dbb.commit()
                tno=dbb.field(f'SELECT TNO FROM tickets WHERE CHANNEL=?', tc.id)


                await tc.edit(name=tc.name+' '+str(tno), overwrites={})
                await tc.set_permissions(interaction.guild.default_role, view_channel=False)
                await tc.set_permissions(interaction.user, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True)
                await tc.set_permissions(support, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)
                # await tc.set_permissions(designer, view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True, mention_everyone=True)


                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description=f"""A ticket opened by **{interaction.user.name}**
Support will be with you soon!
Thanks for choosing Graphics Studio!
Please use /order_paid command.
This is a slash command , make sure all details are entered properly
Image references should be given seperately

This Ticket will be terminated if response is given in 15 minutes"""
                await tc.send(content=f'{interaction.user.mention}', embed=embed)

                embed.description=f'Your Ticket has been Opened. {tc.mention}'
                await interaction.followup.send(embed=embed, ephemeral=True)


                await Logging().on_ticket_open(tc) 

class MainPanel(discord.ui.View):
        def __init__(self):
                super().__init__(timeout=None)

        @discord.ui.button(label='Order FX', style=discord.ButtonStyle.green, custom_id='MainPanelFX')
        async def fx_main(self, interaction: discord.Interaction, button: discord.ui.Button):
                ch= dbb.field(f'SELECT CHANNEL FROM tickets WHERE CLIENT = ? AND PANEL = ?', interaction.user.id, 'fx')
                if not ch is None:
                        embed=discord.Embed(color = discord.Color(0x5affbb))
                        embed.description=f"You already have a ticket open for the Selected Category, <#{ch}>.\nYou cannot have more than one tickets for a Category.\nFor any issues, Open a Help Ticket."
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return
                
                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description="""**Order Placement**

> **To place an order , create a ticket. If youre unsure which method suits you , visit **<#918104035238760458> **for more information**

<:TicketGold:948473587130585118> **Paid Ticket**

> **Open a Paid Ticket if you wish to pay through online payment**

<:TicketBlue:948486028803596338>  **Invites Ticket**

> **Open a Invites Ticket if you wish to pay with invites , to check invites use £invites in** <#918104069372014632> 

<:TicketPink:948485958272159744> **Booster Ticket**

> **Open a Booster Ticket if you are a server booster and want to access the Booster Perks**

<:TicketDarkPink:948486274761773078> **Giveaway Ticket**

> **Open a Giveaway Ticket if you have won a giveaway**"""
                embed.set_footer(text='We have the right to terminate any ticket due to uncivil behaviour')
                embed.set_image(url='https://images-ext-2.discordapp.net/external/D-6_OutM5VwNqIQeI9XQMUZrMXZzBJ0kwfB4LXkze7o/https/media.discordapp.net/attachments/951808374582939729/952090187138203688/Untitled170_20220312115108.png')
                view=FXPanel()
                await interaction.response.send_message(embed=embed,view=view, ephemeral=True)

        
        @discord.ui.button(label='Applications', style=discord.ButtonStyle.green, custom_id='MainPanelApp')
        async def App_main(self, interaction: discord.Interaction, button: discord.ui.Button):
                ch= dbb.field(f'SELECT CHANNEL FROM tickets WHERE CLIENT = ? AND PANEL = ?', interaction.user.id, 'app')
                if not ch is None:
                        embed=discord.Embed(color = discord.Color(0x5affbb))
                        embed.description=f"You already have a ticket open for the Selected Category, <#{ch}>.\nYou cannot have more than one tickets for a Category.\nFor any issues, Open a Help Ticket."
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return
                
                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description="""**Applications**

> **Open a ticket to apply for the following positions**

<:TicketDarkBlue:948486321406627850> **Designer Application**

> **Open a ticket here to apply for designer position**

<:TicketSeaGreen:948486159506481202> **Server Support Application**

> **Open a ticket here to apply for Server Support position** 
"""
                embed.set_footer(text='We have the right to terminate any ticket due to uncivil behaviour')
                embed.set_image(url='https://media.discordapp.net/attachments/951808374582939729/952090187998068766/Untitled170_20220312114848.png')
                view=ApplicationPanel()
                await interaction.response.send_message(embed=embed,view=view, ephemeral=True)
                

        @discord.ui.button(label='Programs', style=discord.ButtonStyle.green, custom_id='MainPanelProg')
        async def Prog_main(self, interaction: discord.Interaction, button: discord.ui.Button):
                ch= dbb.field(f'SELECT CHANNEL FROM tickets WHERE CLIENT = ? AND PANEL = ?', interaction.user.id, 'prog')
                if not ch is None:
                        embed=discord.Embed(color = discord.Color(0x5affbb))
                        embed.description=f"You already have a ticket open for the Selected Category, <#{ch}>.\nYou cannot have more than one tickets for a Category.\nFor any issues, Open a Help Ticket."
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return
                
                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description="""Programs Test Description"""
                embed.set_footer(text='We have the right to terminate any ticket due to uncivil behaviour')
                embed.set_image(url='https://media.discordapp.net/attachments/951808374582939729/972755886785302558/Untitled253_20220508123419.png')
                view=ProgramPanel()
                await interaction.response.send_message(embed=embed,view=view, ephemeral=True)

        @discord.ui.button(label='Order Bots', style=discord.ButtonStyle.green, custom_id='MainPanelBot')
        async def Bot_main(self, interaction: discord.Interaction, button: discord.ui.Button):
                ch= dbb.field(f'SELECT CHANNEL FROM tickets WHERE CLIENT = ? AND PANEL = ?', interaction.user.id, 'bot')
                if not ch is None:
                        embed=discord.Embed(color = discord.Color(0x5affbb))
                        embed.description=f"You already have a ticket open for the Selected Category, <#{ch}>.\nYou cannot have more than one tickets for a Category.\nFor any issues, Open a Help Ticket."
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return
                
                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description="""<:TicketYellow:948502653363703818> **Bot Services Ticket**
     
**__Standard Commands - $3__**
```
help, avatar, ping, serverinfo, userinfo, channelinfo, roleinfo, userid, roleid, channelid, categoryid```

**__Moderation Commands - $5__**
```
warn, removewarn, kick, ban, unban, mute, unmute, setnick, clearnick, purge, giverole, removerole, snipe , delete catagory```

**__Misc Commands - $5__**
```
suggestions, suggest, afk, unafk, embed, echo,quote,1 Ticket System + CustomBotStatus```

**Bots can be only purchased through online payment.
Payment will be taken before the bot is provided
The coding fees and hosting fees will be seperate
For pricing of features required are not listed above , open a ticket**"""
                embed.set_footer(text='We have the right to terminate any ticket due to uncivil behaviour')
                embed.set_image(url='https://media.discordapp.net/attachments/951808374582939729/952090187805122590/Untitled170_20220312114941.png')
                view=BotPanel()
                await interaction.response.send_message(embed=embed,view=view, ephemeral=True)

        @discord.ui.button(label='Support/Help', style=discord.ButtonStyle.green, custom_id='MainPanelSupp')
        async def Supp_main(self, interaction: discord.Interaction, button: discord.ui.Button):
                ch= dbb.field(f'SELECT CHANNEL FROM tickets WHERE CLIENT = ? AND PANEL = ?', interaction.user.id, 'supp')
                if not ch is None:
                        embed=discord.Embed(color = discord.Color(0x5affbb))
                        embed.description=f"You already have a ticket open for the Selected Category, <#{ch}>.\nYou cannot have more than one tickets for a Category.\nFor any issues, Open a Help Ticket."
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return
                
                embed=discord.Embed(color = discord.Color(0x5affbb))
                embed.description="""Help Description for auto help, server support and apply affiliation"""
                embed.set_footer(text='We have the right to terminate any ticket due to uncivil behaviour')
                embed.set_image(url='https://media.discordapp.net/attachments/951808374582939729/952090187805122590/Untitled170_20220312114941.png')
                view=BotPanel()
                await interaction.response.send_message(embed=embed,view=view, ephemeral=True)

class Main(commands.Cog):
        def __init__(self, bot):
                self.bot=bot

        @commands.command()
        async def callpanel(self, ctx):
                view=MainPanel()
                await ctx.send(content='cvbvb', view=view)


async def setup(bot):
        await bot.add_cog(Main(bot))