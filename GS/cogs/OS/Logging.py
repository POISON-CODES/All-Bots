import discord
from discord.ext import commands


from db import db


class Logging(commands.Cog):
        def __init__(self):
                self.embed=discord.Embed(color=discord.Color(0x5affbb))

        async def on_ticket_open(self, channel: discord.TextChannel):
                self.logging_ch=discord.utils.get(channel.guild.channels, id=977631651913924688)
                self.embed.title=f'Ticket Opened.'
                
                data=db.records(f'SELECT CLIENT, OPEN_TIME, PANEL FROM tickets WHERE CHANNEL=?', channel.id)
                data=data[0]
                
                self.embed.description=f"""Client: <@{data[0]}>
Channel: {channel.mention}
Open Time: <t:{int(data[1])}:F>
Ticket Type: {data[2].upper()}"""
                self.embed.timestamp =discord.utils.utcnow()
                await self.logging_ch.send(embed=self.embed)

        async def on_ticket_close(self, channel: discord.TextChannel):
                self.logging_ch=discord.utils.get(channel.guild.channels, id=977631651913924688)
                pass

        async def on_claim(self, channel: discord.TextChannel):
                self.logging_ch=discord.utils.get(channel.guild.channels, id=977631651913924688)
                data = db.record(f'SELECT * FROM tickets WHERE CHANNEL = ?', channel.id)
                self.embed.title='Ticket Claimed'
                self.embed.description = f"""Client: <@{data[2]}>
Artist: <@{data[3]}>
Channel: <#{data[0]}>
Style: {data[7]}
Opened at: <t:{int(data[5])}:F>
Condition: {data[4]}"""
                self.embed.timestamp =discord.utils.utcnow()
                await self.logging_ch.send(embed=self.embed)

        async def on_unclaim(self, ctx: commands.Context):
                self.logging_ch=discord.utils.get(ctx.guild.channels, id=977631651913924688)
                data = db.record(f'SELECT * FROM tickets WHERE CHANNEL = ?', ctx.channel.id)
                self.embed.title='Ticket Unclaimed'
                self.embed.description = f"""Client: <@{ctx.author.id}>
Artist: <@{data[3]}>
Channel: {ctx.channel.mention}
Opened at: <t:{int(data[5])}:F>
Condition: {data[4]}"""
                self.embed.timestamp =discord.utils.utcnow()
                await self.logging_ch.send(embed=self.embed)
                
        
        async def on_ticket_delete(self, channel: discord.TextChannel):
                self.logging_ch=discord.utils.get(channel.guild.channels, id=977631651913924688)
                pass