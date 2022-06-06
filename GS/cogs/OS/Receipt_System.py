import discord
from discord.ext import commands

import time
import asyncio
import re

from db import dbb

class Confirmation(discord.ui.View):
        def __init__(self):
                self.value= None
                super().__init__(timeout=None)

        @discord.ui.button(label='Yes', style=discord.ButtonStyle.green)
        async def confrmation(self, button = discord.ui.Button, interaction = discord.Interaction):
                print('TRUE')
                self.value=True
                self.stop()

        @discord.ui.button(label='No', style=discord.ButtonStyle.red)
        async def deny(self, button = discord.ui.Button, interaction = discord.Interaction):
                print('FALSE')
                self.value=False
                self.stop()

        async def on_timeout(self):
                self.value=False
                self.stop()


class SelectView(discord.ui.Select):
        def __init__(self, options):
                super().__init__(placeholder = 'Select a channnel to make receipt.', options = options)

        async def callback(self, interaction: discord.Interaction):
                await interaction.response.defer(ephemeral=True)

                channel = discord.utils.get(interaction.guild.channels, name = self.values[0])
                data = dbb.record(f"SELECT * FROM tickets WHERE CHANNEL = ?", channel.id)
                embed = discord.Embed(color = discord.Color(0x5affbb))
                embed.title = f'Receipt #{data[1]}'
                embed.description = f"""Channel : {channel.name}
Ticket Number: {data[1]}
Client : <@{data[2]}>
Artist : {interaction.user.mention}
Open Time : <t:{data[5]}:F>
Close Time : <t:{int(time.time())}:F>
Style : {data[7]}"""

                await interaction.followup.send(content = 'Enter the link for the Design.',embed=embed, ephemeral=True)

                def check(msg):
                        return msg.author == interaction.user and msg.channel == interaction.channel
                try:
                        m = await interaction.client.wait_for('message',check=check , timeout=10)
                        print(m.id)

                except asyncio.TimeoutError:
                        embed.description='Timeout'
                        await interaction.followup.send(embed=embed, ephemeral=True)
                        return

                if not m.content.startswith('http'):
                        embed.description=f'only `http` and `https` link format is allowed. Please Try again.'
                        await interaction.followup.send(embed=embed, ephemeral=True)
                        await m.delete()
                        return
                
                embed.set_image(url=m.content)
                await m.delete()
                view=Confirmation()
                view.value=None

                await interaction.followup.send(embed=embed, ephemeral=True, view=view)
                await view.wait()
                print(view.value)
                if view.value is False:
                        embed.description='Timeout'
                        embed.set_image(url='')
                        await interaction.followup.send(embed=embed, ephemeral=True)
                        return
                print('1')
                channel = discord.utils.get(interaction.guild.channels, id = 918104039181414451)
                print('2')
                await channel.send(embed=embed)
                print('3')
                await interaction.followup.send(content = f'Done', ephemeral=True)

class SecondView(discord.ui.View):
        def __init__(self, options):
                super().__init__(timeout=None)

                self.add_item(SelectView(options))

class MainReceiptPanelClass(discord.ui.View):
        def __init__(self):
                self.embed=discord.Embed(color = discord.Color(0x5affbb))
                super().__init__(timeout=None)

        @discord.ui.button(label='Make Receipt', style=discord.ButtonStyle.green, custom_id='receipt')
        async def main_Receipt_button(self, interaction: discord.Interaction, button: discord.ui.Button):
                data = dbb.records(f'SELECT CHANNEL, CLIENT FROM tickets WHERE ARTIST = ?', interaction.user.id)
                print(data)
                if len(data) is 0:
                        self.embed.description = f"I could not find any channels for the artist."
                        await interaction.response.send_message(embed=self.embed,ephemeral=True)
                        return
                
                options = []
                print(data)
                for channels, clients in data:
                        print(channels)
                        print(clients)
                        channels = discord.utils.get(interaction.guild.channels, id=channels)
                        if channels is None:
                                return

                        clients = discord.utils.get(interaction.guild.members, id=clients)
                        options.append(discord.SelectOption(label = f'{channels.name}', description = f"client - {clients.display_name}"))

                view = SecondView(options)
                self.embed.description = "Choose the channel/Client for the receipt"
                await interaction.response.send_message(embed=self.embed, view = view, ephemeral=True)


class RceptPanel(commands.Cog):
        def __init__(self, bot):
                self.bot = bot

        @commands.command()
        async def callr(self, ctx):
                view = MainReceiptPanelClass()
                await ctx.send(content='sfbdbd', view = view)


async def setup(bot):
        await bot.add_cog(RceptPanel(bot))