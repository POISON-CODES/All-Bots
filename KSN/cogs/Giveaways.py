import discord
from discord.ext import commands
from discord.ext import tasks

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger


import datetime
import random
import time
import asyncio


from db import db


class Giveaway_buttons(discord.ui.View):
        def __init__(self):
                super().__init__(timeout=None)

        @discord.ui.button(label='Participate : 0', emoji='🖐️', style=discord.ButtonStyle.green, custom_id='1')
        async def participate_button(self, button: discord.ui.Button, interaction: discord.Interaction):
                embed=discord.Embed(color=0xFFE100)
                
                lists=db.field(f'SELECT PARTICIPANTS FROM giveaway WHERE ID=?', interaction.message.id)

                if lists == 'abc':
                        lists=f'{str(interaction.user.id)}'
                        db.exec('UPDATE giveaway SET PARTICIPANTS=? WHERE ID=?',lists, interaction.message.id)
                        db.commit()
                        embed.description=f'Participation Successfull. Participation ID: 1'
                        button.label=f'Participate : 1'
                        await interaction.message.edit(embed=interaction.message.embeds[0], view=self)
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return
                listss=lists.split(',')
                if str(interaction.user.id) in listss:
                        i=listss.index(str(interaction.user.id))
                        embed.description=f'You have already Participated in this Giveaway `ID: {i+1}`. Double Entried are not allowed.'
                        await interaction.response.send_message(embed=embed, ephemeral=True)
                        return

                lists=lists+f',{interaction.user.id}'
                db.exec('UPDATE giveaway SET PARTICIPANTS=? WHERE ID=?',lists, interaction.message.id)
                db.commit()
                embed.description=f'Participation Successfull. Participation ID: {len(listss)+1}'

                await interaction.response.send_message(embed=embed, ephemeral=True)
                button.label=f'Participate : {len(listss)+1}'
                await interaction.message.edit(embed=interaction.message.embeds[0], view=self)

        # @discord.ui.button(label='Withdraw', emoji='<:PepeExit:949012063475347546>', style=discord.ButtonStyle.red, custom_id='2')
        # async def withdraw(self, button: discord.ui.Button, interaction: discord.Interaction):
        #         embed=discord.Embed(color=0xFFE100)
        #         if button.label=='Participate : 0':
        #                 embed.description=f'There are still no participants.'
        #                 await interaction.response.send_message(embed=embed, ephemeral=True)

        #         participants=db.field(f'SELECT PARTICIPANTS FROM giveaway WHERE ID=?', interaction.message.id)
        #         participantsl=participants.split(',')
        #         if str(interaction.user.id) in participantsl:
        #                 participantsl.pop(str(interaction.user.id))

        #         if len(participants)==1:
        #                 participants='abc'
        #                 db.exec(f'UPDATE giveaway SET PARTICIPANTS=? WHERE ID=?', participants, interaction.message.id)
        #                 db.commit()
        #                 embed.description=f'Successfull.'
        #                 await interaction.response.send_message(embed=embed, ephemeral=True)
        #                 return

        #         if participantsl[0]==str(interaction.user.id) and len(participants)>1:
        #                 participants.replace(f'{str(interaction.user.id)},', '')
        #                 db.exec(f'UPDATE giveaway SET PARTICIPANTS=? WHERE ID=?', participants, interaction.message.id)
        #                 db.commit()
        #                 embed.description=f'Successfull.'
        #                 await interaction.response.send_message(embed=embed, ephemeral=True)
        #                 return

        #         participants=participants.replace(f',{str(interaction.user.id)}', '')
        #         db.exec(f'UPDATE giveaway SET PARTICIPANTS=? WHERE ID=?', participants, interaction.message.id)
        #         db.commit()
        #         embed.description=f'Successfull.'
        #         await interaction.response.send_message(embed=embed, ephemeral=True)


        # @discord.ui.button(label='List', emoji='<:moderators:933232926601134100>', style=discord.ButtonStyle.blurple, custom_id='3')
        # async def list_participants(self, button: discord.ui.Button, interaction: discord.Interaction):
        #         pass

class Confirmation(discord.ui.View):
        def __init__(self):
                self.value=None
                super().__init__(timeout=300)

        @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
        async def confirmation_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.value = True
                embed=interaction.message.embeds[0]
                for item in self.children:
                        item.disabled = True
                await interaction.message.edit(embed=embed, view=self)
                self.stop()
                return

        @discord.ui.button(label='Cancel', style=discord.ButtonStyle.danger)
        async def cancellation_callback(self, button: discord.ui.Button, interaction: discord.Interaction):
                self.value = False
                embed=interaction.message.embeds[0]
                for item in self.children:
                        item.disabled = True
                await interaction.message.edit(embed=embed, view=self)
                self.stop()
                return

        async def on_timeout(self):
                self.value=False
                embed=self.message.embeds[0]
                for item in self.children:
                        item.disabled = True
                await self.message.edit(embed=embed, view=self)
                return


class Giveaways(commands.Cog):
        def __init__(self, bot):
                self.bot=bot
                self.sched=self.bot.scheduler
                
        @commands.Cog.listener()
        async def on_ready(self):
                print('Giveaway Cog ready')
                self.bot.add_view(Giveaway_buttons())
                self.check_giv_end.start()
                
        @tasks.loop(seconds=30.0)
        async def check_giv_end(self):
                # print('checking')
                t=datetime.datetime.now().strftime('%d:%m,%H:%M')
                # print(t)
                id=self.bot.db.field(f'SELECT ID FROM giveaway WHERE ENDING=?',str(t))
                # print(f'id={id}')
                if not id:
                        return
                channel=self.bot.db.field(f'SELECT CHANNEL FROM giveaway WHERE ENDING=?',str(t))
                # print(channel)
                channel=self.bot.get_channel(channel)
                msg=await channel.fetch_message(id)
                if not msg:
                        self.bot.db.exec(f'DELETE FROM giveaway WHERE ID=?', id)
                        self.bot.db.commit()
                        return

                participants=self.bot.db.field(f'SELECT PARTICIPANTS FROM giveaway WHERE ID=?',id)
                participants=participants.split(',')

                new_p=[]
                for i in range(int(len(participants)/2)):
                       new_p.append(random.choice(participants))

                winner=random.choice(new_p) 

                author=self.bot.db.field('SELECT AUTHOR FROM giveaway WHERE ID=?', id)
                prize=self.bot.db.field('SELECT ITEM FROM giveaway WHERE ID=?', id)

                await msg.reply(f'**Giveaway ended.** \n<@{winner}> is the winner of the gievaway. Please contact <@{author}> to claim your reward of {prize}.\nTotal Participants: **{len(participants)}**')
                await msg.edit(embed=msg.embeds[0], view=None)

                self.bot.db.exec(f'DELETE FROM giveaway WHERE ID=?', id)
                self.bot.db.commit()

                

                        


        @commands.command(name='giveaway')
        @commands.has_permissions(administrator=True)
        async def start_giv(self, ctx, channel4: discord.TextChannel):
                starting=int(round(time.time(),0))
                embed=discord.Embed(title='Giveaway!', description=f"""Giveaway started by {ctx.author.mention} at <t:{starting}:R>/<t:{starting}:f>. Ending at `Enter ending time.`
Ending time should be in the format `DD:MM,HH:MM`
Seperate by `,` and `:`.""", color=0xFFE100)
                embed.timestamp=discord.utils.utcnow()

                e1=await ctx.send(embed=embed)
                await ctx.send('Enter End time in the given format.')
                def check(msg):
                        return msg.author==ctx.author and msg.channel==ctx.channel

                try:
                        time_msg=await self.bot.wait_for('message', check=check, timeout = 300)
                except asyncio.TimeoutError:
                        await ctx.send('Too late. Good bye.')
                        return
                time_details=[]
                
                time_details=time_msg.content.split(',')
                if not len(time_details)==2: 
                        await ctx.send('Wrong Format.')
                        return

                date=time_details[0].split(':')
                time_=time_details[1].split(':')

                if int(date[0])>31 or int(date[0])<1:
                        await ctx.send('Incorrect date.')
                        return

                if int(date[1])>12 or int(date[1])<1:
                        await ctx.send('Incorrect month')
                        return

                if int(time_[0])>24 or int(date[0])<0:
                        await ctx.send('Wrong hour format.')
                        return

                if int(time_[1])>60 or int(date[0])<0:
                        await ctx.send('Wrong hour format.')
                        return

                e=int(time.mktime(datetime.datetime.strptime(f'2022 {date[1]} {date[0]} {time_[0]}:{time_[1]}',"%Y %m %d %H:%M").timetuple()))

                embed.description=f"""Giveaway started by {ctx.author.mention} at <t:{starting}:R>/<t:{starting}:f>. Ending at <t:{e}:R>/<t:{e}:f>. Click on button below to participate."""
                e2=await e1.edit(embed=embed)
                await ctx.send('Enter Giveaway Item.')

                try:
                        message2=await self.bot.wait_for('message', check=check, timeout=300)
                except asyncio.TimeoutError:
                        await ctx.send('Too Slow.')
                        return

                view=Confirmation()

                await ctx.send(content=f'Giving Away {message2.content}.',embed=embed, view=view)
                await view.wait()

                if view.value:
                        view=Giveaway_buttons()
                        c=await channel4.send(embed=embed, view=view)
                        self.bot.db.exec(f'INSERT INTO giveaway (CHANNEL, ID, PARTICIPANTS, ENDING, ITEM, AUTHOR) VALUES (?,?,?,?,?,?)',
                                        int(channel4.id), c.id, 'abc', time_msg.content, message2.content, ctx.author.id)
                        self.bot.db.commit()
                        
                        
                        return

                if view.value is False:
                        await e2.edit(content='Cancelled.', embed=None)
                        return




async def setup(bot):
        await bot.add_cog(Giveaways(bot))