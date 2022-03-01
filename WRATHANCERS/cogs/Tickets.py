from io import BytesIO
import discord
from discord.ext import commands

import cogs.config as cfg


class TicketView(discord.ui.View):
        def __init__(self):
                super().__init__(timeout=None)

        options=[discord.SelectOption(emoji='<a:R_arrow:946275794009853962>', label='𝐑𝐄𝐂𝐑𝐔𝐈𝐓𝐌𝐄𝐍𝐓', description='Open Ticket for Recruitment.'),
                discord.SelectOption(emoji='<a:R_arrow:946275794009853962>', label='𝐀𝐋𝐋𝐈𝐀𝐍𝐂𝐄', description='Open Ticket for Alliance.'),
                discord.SelectOption(emoji='<a:R_arrow:946275794009853962>', label='𝐒𝐏𝐎𝐍𝐒𝐎𝐑𝐒𝐇𝐈𝐏', description='Open Ticket for Sponsor.'),
                discord.SelectOption(emoji='<a:R_arrow:946275794009853962>', label='𝐄𝐕𝐄𝐍𝐓', description='Open Ticket for Event.'),
                discord.SelectOption(emoji='<a:R_arrow:946275794009853962>', label='𝐆𝐈𝐕𝐄𝐀𝐖𝐀𝐘', description='Open Ticket for Giveaway claim.'),
                discord.SelectOption(emoji='⚠️', label='𝐑𝐄𝐏𝐎𝐑𝐓', description='Open Ticket to Report an issue/member.')]

        @discord.ui.select(placeholder='Choose Ticket Topic..', custom_id='Tickets', options=options)
        async def callback(self, select: discord.ui.Select, interaction:discord.Interaction):
                ########## DECLARATION ##########

                option=interaction.data['values'][0]
                user=interaction.user
                poison= discord.utils.get(interaction.guild.members, id=int(cfg.OWNER))
                #role1=zvxbxvbx
                #role2=zxbvzxcf

                ########## DECLARATION ##########

                perm_role_list=[]
                ping_role_list=[]
                title=''
                categ=interaction.channel.category if interaction.channel.category is not None else None

                ########## IF OPTION IS ___________ ##########

                if str(option)=='𝐑𝐄𝐂𝐑𝐔𝐈𝐓𝐌𝐄𝐍𝐓':
                        title='Recruitment Ticket'
                        perm_role_list.append(poison)
                        perm_role_list.append(user)
                        ping_role_list.append(user) 
                elif str(option)=='𝐀𝐋𝐋𝐈𝐀𝐍𝐂𝐄':
                        title='Alliance Ticket'
                        perm_role_list.append(poison)
                        perm_role_list.append(user)
                        ping_role_list.append(user)
                elif str(option)=='𝐒𝐏𝐎𝐍𝐒𝐎𝐑𝐒𝐇𝐈𝐏':
                        title='Sponsor Ticket'
                        perm_role_list.append(poison)
                        perm_role_list.append(user)
                        ping_role_list.append(user)
                elif str(option)=='𝐄𝐕𝐄𝐍𝐓':
                        title='Event Ticket'
                        perm_role_list.append(poison)
                        perm_role_list.append(user)
                        ping_role_list.append(user)
                elif str(option)=='𝐆𝐈𝐕𝐄𝐀𝐖𝐀𝐘':
                        title='Giveaway Ticket'
                        perm_role_list.append(poison)
                        perm_role_list.append(user)
                        ping_role_list.append(user)
                elif str(option)=='𝐑𝐄𝐏𝐎𝐑𝐓':
                        title='Report Ticket'
                        perm_role_list.append(poison)
                        perm_role_list.append(user)
                        ping_role_list.append(user)

                ########## IF OPTION IS ___________ ##########
                
                ########## Channel work ##########

                await interaction.response.send_message(f'Creating your **{title}** Ticket. Please wait a few moments....', ephemeral = True)

                tick_chan=None
                if categ==None:
                        tick_chan=await interaction.guild.create_text_channel(name=f'{title}')
                else:
                        tick_chan=await categ.create_text_channel(name=f'{title}')
                await tick_chan.set_permissions(interaction.guild.default_role, view_channel=False)
                for a in perm_role_list:
                        await tick_chan.set_permissions(a, view_channel=True, send_messages=True)


                string_printing=f'<@{interaction.user.id}>'
                
                for b in ping_role_list:
                        if b is interaction.user: 
                                continue
                        else:
                                string_printing=string_printing+f' | {b.mention}'

                
                description = f"""Ticket Details:

Opened by:
》 {interaction.user.mention}

Open Case:
》 {title}

Description: 
》 This Ticker is opened by {interaction.user.mention} for {option} purpose. """

                embed=discord.Embed(title=title, description=description, color=0x2F3136)
                embed.timestamp = discord.utils.utcnow()
                embed.set_author(name = interaction.user.name, icon_url=interaction.user.display_avatar.url)
                await tick_chan.send(content=string_printing, embed=embed)
                await interaction.edit_original_message(content=f'Your Ticket has been opened. Please move to {tick_chan.mention}')

                ########## Channel Work ##########

class TicketInterface(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
        @commands.has_permissions(administrator=True)
        @commands.command(name='TicketSystem')
        async def ticketsystemworking(self, ctx):
                embed=discord.Embed(title = 'Support System', description= f"""WELCOME TO THE •○ ♞ 𝐖𝐑 么 𝐊𝐍𝐈𝐆𝐇𝐓 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ○• 
HOW CAN WE ASSIST YOU""", color=0x2F3136)
                embed.timestamp = discord.utils.utcnow()
                embed.set_author(name = ctx.guild.name, icon_url=ctx.guild.icon.url)
                view=TicketView()
                await ctx.send(embed = embed, view = view)
                await ctx.message.delete()

        @commands.command(aliases=['ts'])
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



        


def setup(bot):
        bot.add_cog(TicketInterface(bot))