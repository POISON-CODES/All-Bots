import discord
from discord.ext import commands
from discord.commands import Cog, command
from discord import TextChannel, Embed, ButtonStyle
from discord.ui import View, Button, button, Interaction
from discord.ButtonStyle import red, green, blurple, grey

import asyncio
from asyncio import TimeoutError


class Embedinator_view(View):
        def __init__(self):
                super().__init__(Timeout=600)

        @button(label='Title', style=grey, custom_id='Embedinator:title')
        async def embedinator_title(self, button = Button, interaction = Interaction):
                pass

        @button(label='Description', style=grey, custom_id='Embedinator:desc')
        async def embedinator_desc(self, button = Button, interaction = Interaction):
                pass

        @button(label='Color', style=grey, custom_id='Embedinator:color')
        async def embedinator_color(self, button = Button, interaction = Interaction):
                pass

        @button(label='Footer', style=grey, custom_id='Embedinator:footer')
        async def embedinator_footer(self, button = Button, interaction = Interaction):
                pass

        @button(label='image', style=grey, custom_id='Embedinator:image')
        async def embedinator_image(self, button = Button, interaction = Interaction):
                pass

        @button(label='Add Field', style=grey, custom_id='Embedinator:add_field')
        async def embedinator_field_add(self, button = Button, interaction = Interaction):
                pass

        @button(label='Field Title', style=grey, custom_id='Embedinator:field_name')
        async def embedinator_field_name(self, button = Button, interaction = Interaction):
                pass

        @button(label='Field Description', style=grey, custom_id='Embedinator:field_val')
        async def embedinator_Field_desc(self, button = Button, interaction = Interaction):
                pass

        @button(label='Send Embed', style=green, custom_id='Embedinator:send')
        async def embedinator_send(self, button = Button, interaction = Interaction):
                pass

        @button(label='Cancel', style=red, custom_id='Embedinator:Cancel')
        async def embedinator_cancel(self, button = Button, interaction = Interaction):
                pass




class Embedinator(Cog):
        def __init__(self, bot):
                self.bot=bot

        @command(name='embed', brief='Create an embed')
        async def create_embed(self, ctx, channel: TextChannel):
                embed=Embed(title='Title', description='DESCRIPTION', color=0x2F3136)
                embed.set_footer(text='FOOTER')
                view = 1
                await ctx.send(embed=embed, view=view)



def setup(bot):
        bot.add_cog(Embedinator(bot))