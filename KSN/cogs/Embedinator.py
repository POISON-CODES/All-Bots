import discord
from discord.ext import commands
from discord.ext.commands import Cog, command
from discord import TextChannel, Embed, ButtonStyle


import time

class Embedinator_view(discord.ui.View):
        def __init__(self, bot):
                self.bot = bot
                super().__init__(timeout=None)

        @discord.ui.button(label='Title', style=discord.ButtonStyle.grey, custom_id='Embedinator:title')
        async def embedinator_title(self, button = discord.ui.Button, interaction = discord.Interaction):
                embed=interaction.message.embeds[0]
                msg=interaction.message

                await msg.channel.send('Enter the `Title` of the Embed.')
                def check(message):
                        message.channel==msg.channel and msg.author == message.author

                teetle=await self.bot.wait_for('message', check=check, timeout=300)



        @discord.ui.button(label='Description', style=discord.ButtonStyle.grey, custom_id='Embedinator:desc')
        async def embedinator_desc(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Color', style=discord.ButtonStyle.grey, custom_id='Embedinator:color')
        async def embedinator_color(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Footer', style=discord.ButtonStyle.grey, custom_id='Embedinator:footer')
        async def embedinator_footer(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='image', style=discord.ButtonStyle.grey, custom_id='Embedinator:image')
        async def embedinator_image(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Add Field', style=discord.ButtonStyle.grey, custom_id='Embedinator:add_field')
        async def embedinator_field_add(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Remove Field', style=discord.ButtonStyle.grey, custom_id='Embedinator:rem_field')
        async def embedinator_field_rem(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Field Title', style=discord.ButtonStyle.grey, custom_id='Embedinator:field_name')
        async def embedinator_field_name(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Field Description', style=discord.ButtonStyle.grey, custom_id='Embedinator:field_val')
        async def embedinator_Field_desc(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='TimeStamp', style=discord.ButtonStyle.green, custom_id='Embedinator:timeStamp')
        async def embedinator_timestamp_toggle(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Send Embed', style=discord.ButtonStyle.green, custom_id='Embedinator:send')
        async def embedinator_send(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass

        @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red, custom_id='Embedinator:Cancel')
        async def embedinator_cancel(self, button = discord.ui.Button, interaction = discord.Interaction):
                pass


        async def on_timeout(self):
                embed=self.message.embeds[0]
                embed.set_footer(text='This Embedinator Timed Out.')
                self.message.edit(embed=embed)
                return

class Embedinator(Cog):
        def __init__(self, bot):
                self.bot=bot

        @command(name='embed', brief='Create an embed')
        async def create_embed(self, ctx, channel: TextChannel):
                embed=Embed(title='Title', description='DESCRIPTION', color=0x2F3136)
                embed.set_footer(text='FOOTER')
                view = Embedinator_view(self.bot)
                await ctx.send(embed=embed, view=view)


        

def setup(bot):
        bot.add_cog(Embedinator(bot))