from http.client import HTTPException
import discord
from discord.ext import commands
import time
import config as cfg
import asyncio

from discord.app_commands import AppCommandError

from discord import app_commands
from typing import Optional

class PartnerView(discord.ui.View):
       def __init__(self, link):
              self.link = link
              super().__init__(timeout=None)

              self.add_item(discord.ui.Button(label= 'Join Server',style=discord.ButtonStyle.link, url=link))


class General(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              super().__init__()

       @app_commands.command(name='say')
       async def say_command(self, interaction: discord.Interaction, text: str):
              role=discord.utils.get(interaction.guild.roles, id=967948574354735125)
              await interaction.response.defer()
              embed=discord.Embed(color=discord.Color(0xFFE100))
              if not role in interaction.user.roles:
                     embed=discord.Embed(color=discord.Color(0xFFE100))
                     embed.description=f'You do not have {role.mention} role to use this command.'
                     msg=await interaction.followup.send(embed = embed)
                     time.sleep(5)
                     await msg.delete()
                     return

              await interaction.channel.send(content=text)
              msg=await interaction.followup.send(content=f'done')
              await msg.delete()

       @app_commands.command(name='ccpromo')
       @app_commands.checks.has_role(869810456330645514)
       @app_commands.describe(link='Link to the Post.')
       async def cc_promo(self,
              interaction: discord.Interaction,
              link: str):
              channel = interaction.guild.get_channel(968450241080745984)
              await channel.send(content=f'<@&873071213419831316> Check out new post from {interaction.user.mention}\n{link}')

       @app_commands.command(name='partnership')
       @app_commands.checks.has_role(894810051401875466)
       async def partnership(self,
              interaction: discord.Interaction,
              name: str,
              link: str,
              affiliation_image: Optional[str]=None,
              description: Optional[str] = None,):
              embed= discord.Embed(color = discord.Color(0xffd800))
              embed.title=f'{interaction.guild.name} has Partnered with {name}!'
              if not description is None:
                     embed.description=description

              embed.color=0xffd800
              
              if not affiliation_image is None:
                     if not affiliation_image.startswith('http'):
                            await interaction.response.send_message(content='Image Link needs to start with `http`.', ephemeral=True)
                            return
                     embed.set_image(url=affiliation_image)

              channel = interaction.guild.get_channel(975988555623067678)
              await channel.send(content=f'<@&896683204961005620>', 
                     embed=embed,
                     view = PartnerView(link=link))


       @app_commands.command(name='embed')
       @app_commands.describe(body='The Body of the Embed')
       @app_commands.describe(color='Color of Embed. Needs to start with `0x`, ex: `0x000000`')
       @app_commands.describe(image='Image displated at the bottom.')
       @app_commands.describe(footer='Footer of the embed. Timestamp is added by default')
       @app_commands.describe(thumbnail='Thumbnail of the Embed.')
       @app_commands.describe(title='Title of the Embed')
       @app_commands.describe(date_time='Yes to apply, ignore to remove')
       async def embed_command(self, 
              interaction: discord.Interaction, 
              body: str,
              color: str,
              image: Optional[str],
              footer: Optional[str],
              thumbnail: Optional[str],
              title: Optional[str],
              date_time: Optional[str]=None,
              ):
              role=discord.utils.get(interaction.guild.roles, id=967948574354735125)
              await interaction.response.defer(ephemeral=True)
              embed=discord.Embed(color=discord.Color(0xFFE100))
              if not role in interaction.user.roles:
                     embed=discord.Embed(color=discord.Color(0xFFE100))
                     embed.description=f'You do not have {role.mention} role to use this command.'
                     msg=await interaction.followup.send(embed = embed)
                     time.sleep(5)
                     await msg.delete()
                     return

              if not color.startswith('0x'):
                     embed.description='The color needs to start with `0x` example: `0x000000`'
                     msg=await interaction.followup.send(embed = embed)
                     time.sleep(5)
                     await msg.delete()
                     return
              
              color = await commands.ColorConverter().convert(interaction, str(color))

              try:
                     embed.color=color
              except:
                     embed.description=f'Couldnt set color.'
                     msg=await interaction.followup.send(embed = embed)
                     time.sleep(5)
                     await msg.delete()
                     return
                     
              embed.description=body
              if not image is None:
                     if not image.startswith('http'):
                            await interaction.followup.send('Thumbnail link can only start with `http` or `https`')
                            return
                     embed.set_image(url=image)

              if not footer is None:
                     embed.set_footer(text=footer)
              if not date_time is None:
                     embed.timestamp= discord.utils.utcnow()
              if not thumbnail is None:
                     if not thumbnail.startswith('http'):
                            await interaction.followup.send('Thumbnail link can only start with `http` or `https`')
                            return
                     embed.set_thumbnail(url=thumbnail)

              if not title is None:
                     embed.title = title

              await interaction.channel.send(embed = embed)
              msg=await interaction.followup.send(content=f'done')


       @commands.command(name='dm')
       @commands.has_guild_permissions(administrator=True)       
       async def dm_command(self ,
              ctx: commands.Context,
              user: discord.User, 
              *, message: str
              ):
              try:
                     await user.send(message)
                     await ctx.reply(f'Sent to {user.mention}', delete_after=5)
              except:
                     await ctx.reply(f"Couldnt send to {user.mention} as they have their DM's closed", delete_after=5)


       @commands.command(aliases=['latency', 'delay', 'rtt'])
       async def ping(self, ctx):

              typing_start = time.monotonic()
              await ctx.trigger_typing()
              typing_end = time.monotonic()
              typing_ms = (typing_end - typing_start) * 1000

              start = time.perf_counter()
              message = await ctx.send("🏓 pong!")
              end = time.perf_counter()
              message_ms = (end - start) * 1000

              latency_ms = self.bot.latency * 1000
              
              embed=discord.Embed(color=discord.Color(0xFFE100))
              embed.add_field(name ='Websocket ', value=f"{round(latency_ms, 3)}ms{' ' * (9 - len(str(round(latency_ms, 3))))}", inline=True)
              embed.add_field(name ='Message', value=f"{round(message_ms, 3)}ms{' ' * (9 - len(str(round(message_ms, 3))))}", inline = True)
              embed.add_field(name ='Typing ', value=f"{round(typing_ms, 3)}ms{' ' * (9 - len(str(round(typing_ms, 3))))}", inline=True)
              await message.edit(content=None, embed = embed)

       @commands.command(aliases=['bi', 'abb', 'aboutbot'])
       async def botinfo(self, ctx):
              embed= discord.Embed(title ='About BOT', description=f'{self.bot.description}', color=discord.Color(0xFFE100))
              embed.add_field(name='API VERSION', value=f"{discord.__version__}", inline=True)
              embed.add_field(name='\u200b', value='\u200b', inline=True)
              embed.add_field(name='BOT VERSION', value=f'v1.0.0', inline=True)
              embed.add_field(name='Servers', value=f'{len(self.bot.guilds)}', inline=True)
              embed.add_field(name='\u200b', value='\u200b', inline=True)
              embed.add_field(name='Members', value=f'{len(self.bot.users)}', inline=True)
              embed.add_field(name='Developer', value=f'<@724283255959978057>', inline=True)
              embed.add_field(name='\u200b', value='\u200b', inline=True)
              embed.add_field(name='Commands', value=f'{len(self.bot.commands)}', inline=True)
              embed.add_field(name='Cogs', value=f'{len(self.bot.cogs)}', inline=True)
              embed.add_field(name='\u200b', value='\u200b', inline=True)
              owner=self.bot.get_user(724283255959978057)
              embed.add_field(name='UPTIME', value=f'<t:{self.bot.startup_time}:R>')
              embed.set_author(name = f'{owner.name}', icon_url=f'{owner.avatar.url}')
              embed.set_footer(text = f'{self.bot.user.name} | {self.bot.user.id}', icon_url=self.bot.user.avatar.url)
              embed.set_thumbnail(url=ctx.guild.icon)
              embed.timestamp = discord.utils.utcnow()
              await ctx.send(embed = embed)

       @commands.command(aliases=['si','aboutserver'])
       async def serverinfo(self, ctx):
              desc=''
              embed=discord.Embed(title ='About Server', description=desc, color=discord.Color(0xFFE100))
              embed.add_field(name ='Owner', value=ctx.guild.owner.mention, inline=False)
              # embed.add_field(name='\u200b', value='\u200b', inline=True)
              embed.add_field(name='Members', value=len(ctx.guild.members), inline=True)
              embed.add_field(name='\u200b', value='\u200b', inline=True)
              embed.add_field(name='Bots', value=sum(i.bot for i in ctx.guild.members), inline=True)
              # embed.add_field(name='\u200b', value='\u200b', inline=True)
              tlocked=0
              for channel in ctx.guild.text_channels:
                     if channel.permissions_for(ctx.author).view_channel==True:
                            continue
                     else:
                            tlocked+=1
              vlocked=0       
              for channel in ctx.guild.voice_channels: 
                     if channel.permissions_for(ctx.author).connect==True:
                            continue
                     else:
                            vlocked+=1
              embed.add_field(name='Channels', value=f'Text Channels: {len(ctx.guild.text_channels)} ({tlocked} locked)\nVoice Channels: {len(ctx.guild.voice_channels)} ({vlocked} locked.)', inline=True)
              embed.set_footer(text = f'{self.bot.user.name} | {self.bot.user.id}', icon_url=self.bot.user.avatar.url)
              embed.set_thumbnail(url=ctx.guild.icon)
              embed.timestamp = discord.utils.utcnow()
              await ctx.send(embed = embed)

       @commands.command(name='sync')
       @commands.is_owner()
       async def syncing(self, ctx):
              await self.bot.tree.sync(guild=discord.Object(id=770627092298596353))
              await ctx.send(f'Synced.', delete_after=10)

async def setup(bot):
       global bota
       bota=bot
       bot.help_command=MyHelpCommand()
       await bot.add_cog(General(bot), guilds=[discord.Object(id=770627092298596353)])

class MyHelpCommand(commands.HelpCommand):
       
       async def send_bot_help(self, mapping):
              color= discord.Color(0xFFFFFF)
              embed= discord.Embed(title='Help Menu', description=self.context.bot.description, color=color)
              embed.add_field(name ='Commands Help', value='Get help with command categories by selecting options in the menu below.')
              embed.timestamp = discord.utils.utcnow()
              options=[]
              self.bot=self.context.bot   
              for cog, commands in mapping.items():
                     if cog is None or cog.qualified_name=='Jishaku' or len(cog.get_commands())==0: continue
                     else:
                            options.append(discord.SelectOption(label='No Category' if cog is None else cog.qualified_name))
              view=HelpView(ctx=self.context,options= options)
              await self.get_destination().send(embed = embed, view = view)


       async def get_filtered(self, cog):
              filtered_commands=await self.filter_commands(cog.get_commands, sort=True)
              return filtered_commands


async def custom_filter(commands):
       filtered=[]
       for command in commands:
              if command.hidden==True:
                     continue
              else:
                     filtered.append(command)

       return filtered

class HelpView(discord.ui.View):
       def __init__(self, ctx, options):
              self.ctx=ctx
              self.options=options
              super().__init__()

              self.add_item(Nothing(self.ctx, self.options))


class Nothing(discord.ui.Select):
       def __init__(self, ctx, options):
              self.ctx = ctx
              self.bot=self.ctx.bot
              super().__init__(placeholder='Please Select Help Category...', options=options)

       async def callback(self, interaction: discord.Interaction):
              # print(0)
              cog_name=interaction.data['values'][0]
              
              cog=self.bot.get_cog(str(cog_name))
              commands_list=cog.get_commands()
              
              classer=self.bot.help_command
              classer.context=self.ctx
              commands_list = await classer.filter_commands(commands=commands_list, sort=True)
              filtered=await custom_filter(commands=commands_list)
              value=''
              self.bot=self.ctx.bot
              if len(filtered)==0:
                     value='```You cannot use any commands in this category.```'
              else: 
                     for command in filtered:
                            new=f'<a:redstar:900703292986912788> {command.name}  --> '
                            value=value+new
                            new=f'{command.help}\n\n' or '``No description Yet.``\n'
                            value=value+new+f'``aliases={command.aliases}``\n\n'
                            value=value.replace('\'', '')
              embed= discord.Embed(description=f'{cog.qualified_name}\n'+value, color=discord.Color(0xFFFFFF))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text=f'Requested by {classer.context.author.name}')
              embed.set_thumbnail(url=self.bot.user.avatar.url)

              await interaction.message.edit(embed = embed)