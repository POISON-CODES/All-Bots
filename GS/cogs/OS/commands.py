from http.client import HTTPException
import discord
from discord.ext import commands


from cogs.OS.Logging import Logging


from db import dbb
import time


class ClaimView(discord.ui.View):
        def __init__(self, ctx):
                self.ctx = ctx
                self.embed=discord.Embed(color=discord.Color(0x5affbb))
                super().__init__(timeout=None)


        data = dbb.column(f'SELECT STYLE FROM pricing')
        options = []
        for a in data:
                options.append(discord.SelectOption(label=str(a)))

        @discord.ui.select(placeholder='Select Design', options=options)
        async def on_select(self, interaction: discord.Interaction, select: discord.ui.Select):
                await interaction.response.defer(ephemeral=True)

                value = select.values[0]
                print(self.ctx.author.name)
                print(interaction.user.name)
                if not self.ctx.author.id is interaction.user.id:
                        self.embed.description=f'Style can only be selected by the author of the command.'

                        await interaction.followup.send(embed=self.embed, ephemeral=True)
                        await self.ctx.message.delete()
                        await interaction.message.delete()
                        return

                dbb.exec(f'UPDATE tickets SET ARTIST = ? ,CONDITION = ?, STYLE =? WHERE CHANNEL =?', interaction.user.id, 'claimed', value, interaction.channel.id)
                dbb.commit()

                client = dbb.field(f'SELECT CLIENT FROM tickets WHERE CHANNEL =?', interaction.channel.id)

                self.embed.description=f'Ticket Claimed.\nStyle: {value}\nArtist: {interaction.user.mention}\nClient: <@{client}>'
                await interaction.followup.send(embed=self.embed, ephemeral=True)

                client = interaction.guild.get_member(client)
                await client.send(embed=self.embed)
                category=discord.utils.get(interaction.guild.categories, id=942493034707312750)
                await interaction.channel.edit(category=category)
                await self.ctx.message.delete()
                await interaction.message.delete()
                await Logging().on_claim(interaction.channel)


class Ticket_Commands(commands.Cog):
        def __init__(self, bot):
                self.bot= bot
                self.embed=discord.Embed(color=discord.Color(0x5affbb))

        @commands.command()
        async def claim(self, ctx, member: discord.Member = None):
                if not member is None:
                        ctx.author = member
                val = dbb.field(f'SELECT ARTIST FROM tickets WHERE CHANNEL = ?', ctx.channel.id)

                if val != 0:
                        self.embed.description = f'This channel is already claimed by <@{val}>'
                        await ctx.send(embed=self.embed)
                        return

                self.embed.description = f'Select the Design Style'
                view=ClaimView(ctx)
                m=await ctx.send(embed=self.embed, view=view)
                view.message=m

        @commands.command()
        async def unclaim(self, ctx):
                artist = dbb.field(f'SELECT ARTIST FROM tickets WHERE CHANNEL = ?', ctx.channel.id)
                if artist == 0:
                        self.embed.description = f'This ticket has not yet been claimed.'
                        await ctx.send(embed=self.embed, delete_after=5)
                        return

                if artist != ctx.author.id:
                        self.embed.description = f'This ticket has been claimed by <@{artist}>'
                        await ctx.send(embed=self.embed, delete_after=5)
                        return

                dbb.exec('UPDATE tickets SET ARTIST = ?, CONDITION = ?, STYLE = ? WHERE CHANNEL = ?', 0, 'unoccupied', 'unoccupied', ctx.channel.id)
                dbb.commit()

                client = dbb.field(f'SELECT CLIENT FROM tickets WHERE CHANNEL =?', ctx.channel.id)
                client = discord.utils.get(ctx.guild.members, id=client)
                
                self.embed.description=f'Ticket Unclaimed.'
                await ctx.send(embed=self.embed, delete_after = 5)
                self.embed.description = f'Yout ticket in <#{ctx.channel.id}> has been unclaimed by {ctx.author.mention}.'
                await client.send(embed=self.embed)
                
                category=discord.utils.get(ctx.guild.categories, id=918104010135834674)
                await ctx.channel.edit(category=category)

                await Logging().on_unclaim(ctx)

        @commands.command()
        async def details(self, ctx):
                pass

        @commands.command()
        async def ticket_close(self, ctx):
                client = dbb.field(f'SELECT CLIENT FROM tickets WHERE CHANNEL = ?', ctx.channel.id)
                client = await ctx.guild.fetch_member(client)
                # print(client.name)

                await ctx.channel.set_permissions(client, send_messages=False)
                
                dbb.exec(f'UPDATE tickets SET CONDITION = ?, CLOSE_TIME =? WHERE CHANNEL = ?', 'closed',int(time.time()), ctx.channel.id)
                dbb.commit()

                self.embed.title = 'Ticket Closed'
                self.embed.description = f'The Ticket has been closed by {ctx.author.mention} for the ticket of {client.mention}'
                await ctx.send(embed=self.embed)
                try:
                        await client.send(embed=self.embed)
                except HTTPException:
                        pass

                
                await Logging().on_ticket_close(ctx.channel, user=ctx.author)

        @commands.command()
        async def ticket_delete(self, ctx):
                client = dbb.field(f'SELECT CLIENT FROM tickets WHERE CHANNEL =?',ctx.channel.id)
                if client is None:
                        self.embed.description = f'This channel does not appear to be a ticket channel.'
                        await ctx.send(embed=self.embed)
                        return

                dbb.exec(f'UPDATE tickets SET CONDITION = ? WHERE CHANNEL = ?', 'deleted', ctx.channel.id)
                dbb.commit()
                
                await Logging().on_ticket_delete(ctx.channel, user=ctx.author)
                await ctx.channel.delete()

        @commands.command()
        async def transcript(self, ctx):
                pass

async def setup(bot):
        await bot.add_cog(Ticket_Commands(bot))