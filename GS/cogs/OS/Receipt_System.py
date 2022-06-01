import discord
from discord.ext import commands


import time


from db import db

class SelectView(discord.ui.Select):
        def __init__(self, options):
                super().__init__(placeholder = 'Select a channnel to make receipt.', options = options)

        async def callback(self, interaction: discord.Interaction):
                channel = discord.utils.get(interaction.guild.channels, name = self.values[0])
                data = db.record(f"SELECT * FROM tickets WHERE CHANNEL = ?", channel.id)
                embed = discord.Embed(color = discord.Color(0x5affbb))
                embed.title = f'Receipt #{data[1]}'
                embed.description = f"""Channel : {channel.name}
Ticket Number: {data[1]}
Client : <@{data[2]}>
Artist : {interaction.author.mention}
Open Time : <t:{data[5]}:F>
Close Time : <t:{int(time.time())}:F>
Style : {data[7]}"""

                data2 = db.record(f'SELECT * FROM pricing WHERE STYLE =?', data[7])
                embed.description=embed.description + f"""
Price : {data2[1]} INR / {data2[2]} USD / {data2[3]} Invites"""

                await interaction.response.send_message(content = 'Enter the link for the Design.',embed=embed, ephemeral=True)

                try:
                        m = await 
                                



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
                data = db.records(f'SELECT CHANNELS, CLIENTS FROM tickets WHERE ARTIST = ?', interaction.user.id)
                if data is None:
                        self.embed.description = f"I could not find any channels for the artist."
                        await interaction.response.send_message(embed=self.embed,ephemeral=True)
                        return
                
                options = []

                for channels, clients in data:
                        channels = discord.utils.get(interaction.guild.channels, channels)
                        if channels is None:
                                return

                        clients = discord.utils.get(interaction.guild.members, clients)
                        options.append(discord.SelectOption(label = f'{channels.name}', description = f"client - {clients.display_name}"))

                view = SecondView(options)
                self.embed.description = "Choose the channel/Client for the receipt"
                await interaction.response.send_message(embed=self.embed, view = view, ephemeral=True)
