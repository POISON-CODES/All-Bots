from shutil import register_unpack_format
from tkinter import N
import discord
from discord.ext import commands


import asyncio
import cogs.config as cfg

class Confirmation(discord.ui.View):
        def __init__(self):
                self.value=None
                super().__init__(timeout=300)

        @discord.ui.button(label='Confirm', emoji='✅', style=discord.ButtonStyle.green)
        async def confirm_callback(self, button = discord.ui.Button, interaction = discord.Interaction):
                self.value=True
                for c in self.children:
                        c.disabled = True
                embed=interaction.message.embeds[0]
                embed.set_footer(text='Confirmed, Tag created')
                await self.message.edit(embed=embed, view=self)
                self.stop()
                 

        @discord.ui.button(label='Cancel', emoji='❎', style=discord.ButtonStyle.red)
        async def cancellation_callback(self, button = discord.ui.Button, interaction = discord.Interaction):
                self.value=False
                for c in self.children:
                        c.disabled = True
                embed=interaction.message.embeds[0]
                embed.set_footer(text='Cancelled')
                await self.message.edit(embed=embed, view=self)
                self.stop()
                return

        async def on_timeout(self):
                for c in self.children:
                        c.disabled = True
                await self.message.edit(embed=self.message.embeds[0], view=self)
                self.value=False

class Tags(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                super().__init__()

        @commands.Cog.listener()
        async def on_message(self, message):
                if not message.content.startswith(cfg.PREFIX):
                      return
                tags=self.bot.db.column('SELECT TAG_NAME FROM tags')
                content = message.content[:0] + '' + message.content  [1:]
                value=''
                if content in tags:
                        value = self.bot.db.field('SELECT TAG_VALUE FROM tags WHERE TAG_NAME=?', str(content))
                        embed=discord.Embed(title=content, description=f"""{value}""", color=self.bot.COLOR)
                        await message.reply(embed= embed)

        @commands.command(name='create')
        @commands.has_permissions(administrator=True)
        async def create_taG(self, ctx, *, name):
                embed=discord.Embed(title=name,description='Enter the value for Tag', color=self.bot.COLOR)
                bot_msg=await ctx.send(embed = embed)

                def check(message):
                        return message.author== ctx.author and message.channel == ctx.channel
                try:
                        value=await self.bot.wait_for('message', check=check, timeout=300)
                except asyncio.TimeoutError:
                        embed.description='TimeUp!. Please Try again'
                        await bot_msg.edit(embed=embed)
                view=Confirmation()
                embed.description=value.content
                view.message=await bot_msg.edit(embed = embed, view=view)
                await view.wait()
                if view.value:
                        self.bot.db.exec(f'INSERT INTO tags (AUTHOR, TAG_NAME, TAG_VALUE) VALUES (?,?,?)', ctx.author.id, str(name), str(value.content))
                        self.bot.db.commit()

        @commands.command(name='del_tag')
        @commands.has_permissions(administrator=True)
        async def del_tag(self, ctx, *,name):
                tags=self.bot.db.column('SELECT TAG_NAME FROM tags')
                embed=discord.Embed(title=name, description='No such tag exists.', color=self.bot.COLOR)
                if not name in tags:
                        await ctx.reply(embed= embed)
                        return

                self.bot.db.exec('DELETE FROM tags WHERE TAG_NAME = ?', str(name))
                self.bot.db.commit()
                embed.description=f'Tag `{name}` deleted'
                await ctx.reply(embed= embed)


        @commands.command(name='list_tags')
        async def listing_tags(self, ctx):
                tags=self.bot.db.column('SELECT TAG_NAME FROM tags')
                value=''
                for i in tags:
                        value=value+f'`{i}`, '

                vlast=value.rfind(', ')
                value = value[:vlast] + '' + value  [vlast + 1:]
                embed=discord.Embed(description=value, color=self.bot.COLOR)
                embed.set_footer(text=f'Use `{cfg.PREFIX}<tag name> to get the tag info.')
                await ctx.send(embed=embed)

        @commands.command(name='edit_tag')
        @commands.has_permissions(administrator=True)
        async def edit_tag(self, ctx, *, name):
                tags=self.bot.db.column('SELECT TAG_NAME FROM tags')
                embed=discord.Embed(description=f'No Tag with the name found.', color=self.bot.COLOR)
                if not name in tags:
                        await ctx.reply(embed= embed)
                        return

                author=self.bot.db.field('SELECT AUTHOR FROM tags WHERE TAG_NAME=?', str(name))
                if not ctx.author.id == author:
                        embed.description=f'This Tag was created by <@{author}> and can only be edited by them.'
                        await ctx.reply(embed= embed)
                        return
                        
                embed.description=f'Enter new value for the Tag.'
                old_val=self.bot.db.field('SELECT TAG_NAME FROM tags WHERE TAG_NAME=?', str(name))
                await ctx.send(embed = embed)
                def check(message):
                        return message.author== ctx.author and message.channel == ctx.channel

                try:
                        msg=self.bot.wait_for('message', check=check, timeout=600)
                except asyncio.TimeoutError:
                        embed.description=f'TimeUp!!! Try again.'
                        await ctx.send(embed = embed)
                        return

                if len(msg.content) > 4000:
                        await ctx.send('the message is too long.')
                        return

                self.bot.db.exec(f'UPDATE tags SET TAG_VALUE=? WHERE TAG_NAME=?', str(msg.content), str(name))
                self.bot.db.commit()
                embed.description=f'Tag Successfully Updated.'
                embed.add_field(name='Old Value', value=old_val, inline=False)
                embed.add_field(name='New value', value=msg.content)
                try:
                        await ctx.send(embed = embed)
                except:
                        embed.remove_field(index=0)
                        embed.remove_field(index=1)
                        embed.description='Value Updated.\n =>'+msg.content
                        await ctx.send(embed = embed)
async def setup(bot):
        await bot.add_cog(Tags(bot))