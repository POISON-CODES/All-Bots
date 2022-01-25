import discord
from discord.ext import commands
import time
import cogs.config as cfg
import sys


class General(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              super().__init__()

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

def setup(bot):
       global bota
       bota=bot
       bot.help_command=MyHelpCommand()
       bot.add_cog(General(bot))

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
              
              cog=self.bot.get_cog(name=str(cog_name))
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