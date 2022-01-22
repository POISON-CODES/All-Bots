import discord
from discord.ext import commands
import cogs.config as cfg
from utils.embeds import PBEmbeds as em

bot=commands.Bot(command_prefix=commands.when_mentioned_or(cfg.PREFIX), intents=discord.Intents.all())
bot.description=f'This bot was created by <@{cfg.OWNER}> for Managing Tickets.'

class MyHelpCommand(commands.HelpCommand):
       
       async def send_bot_help(self, mapping):
              color= discord.Color(0xFFFFFF)
              embed= discord.Embed(title='Help Menu', description=bot.description, color=color)
              embed.add_field(name ='Commands Help', value='Get help with command categories by selecting options in the menu below.')
              embed.timestamp = discord.utils.utcnow()
              options=[]
              self.bot=self.context.bot   
              for cog, commands in mapping.items():
                     options.append(discord.SelectOption(label='No Category' if cog is None else cog.qualified_name))
              view=HelpView(ctx=self.context,options= options)
              await self.get_destination().send(embed = embed, view = view)


       async def get_filtered(self, cog):
              filtered_commands=await self.filter_commands(cog.get_commands, sort=True)
              return filtered_commands

bot.help_command=MyHelpCommand()

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
              super().__init__(placeholder='Please Select Help Category', options=options)

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
              for command in filtered:
                     new=f'<a:795277872482222130:854054770854330399> {command.name} == '
                     value=value+new
                     new=command.help or '``No description Yet.``\n\n'
                     value=value+new
              embed= discord.Embed(description=f'```{cog.qualified_name}```\n'+value, color=discord.Color(0xFFFFFF))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text=f'Requested by {classer.context.author.name}')
              embed.set_thumbnail(url=self.bot.user.avatar.url)

              await interaction.message.edit(embed = embed)

@bot.event
async def on_command_error(ctx, error):
       if hasattr(ctx.command, 'on_error'):
            return

       cog = ctx.cog
       if cog:
            if cog._get_overridden_method(cog.cog_command_error) is not None:
                return

       if isinstance(error, commands.CommandNotFound):
              embed=em.DescE(desc=f'Command ``{ctx.command.name}`` Not Found.')
              await ctx.send(embed= embed)

       error = getattr(error, 'original', error)
       if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')

       if isinstance(error, commands.NoPrivateMessage):
              try:
                     await ctx.send(f'Command cannot be used in DMs')
              except discord.HTTPException:
                     return
       
       if isinstance(error, commands.MissingRequiredArgument):
              embed=em.DescE(desc=f'{ctx.command.name} was used incorrectly and required arguments were missing.\nCorrect Usage: ``{ctx.command.name} {ctx.command.signature}``')
              await ctx.send(embed = embed)

       if isinstance(error, commands.MissingPermissions):
              embed=em.DescE(desc=f'``Oops! You dont have the permission to use this command.``')
              await ctx.send(embed = embed)
       
       

@bot.event
async def on_ready():
       print(f'Logged in as {bot.user.name}')
       print(f'{bot.user.id}')

initial_extensions = cfg.INITIAL_EXTENSIONS
for extension in initial_extensions:
       try:
              bot.load_extension(extension)
              print(f'Loaded {extension}')
       except Exception as e:
              print(f'Couldnt load {extension} cz of error {str(e)}') 

bot.run(cfg.TOKEN)