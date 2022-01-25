import discord
from discord.ext import commands
import time
import cogs.config as cfg
import json
from cogs.ticket import *
from cogs.order import *
from cogs.buttons import *

class EmbedHelpCommand(commands.HelpCommand):
    """This is an example of a HelpCommand that utilizes embeds.
    It's pretty basic but it lacks some nuances that people might expect.
    1. It breaks if you have more than 25 cogs or more than 25 subcommands. (Most people don't reach this)
    2. It doesn't DM users. To do this, you have to override `get_destination`. It's simple.
    Other than those two things this is a basic skeleton to get you started. It should
    be simple to modify if you desire some other behaviour.
    
    To use this, pass it to the bot constructor e.g.:
       
    bot = commands.Bot(help_command=EmbedHelpCommand())
    """
    # Set the embed colour here
    COLOUR = discord.Colour(0x00f064)

    def get_ending_note(self):
        return 'Use {0}{1} [command] for more info on a command.'.format('%', self.invoked_with)

    def get_command_signature(self, command):
        return '{0.qualified_name} {0.signature}'.format(command)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='Bot Commands', colour=self.COLOUR)
        description = "Bot Help"
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            name = 'No Category' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            if filtered:
                value=f'\u2002'.join(f'`{c.name}`' for c in commands if c.hidden==False)
                
                embed.add_field(name=name, value=value, inline = False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR)
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name = f'`{self.get_command_signature(command)}`', value=command.description or None, inline = True)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name, colour=self.COLOUR)
        if group.help:
            embed.description = group.help

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                if command.hidden==False:
                    embed.add_field(name=f'`{self.get_command_signature(command)}`', value=command.short_doc or '...', inline=True)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    # This makes it so it uses the function above
    # Less work for us to do since they're both similar.
    # If you want to make regular command help look different then override it
    send_command_help = send_group_help

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or('%'), intents=intents, help_command=EmbedHelpCommand())
bot.case_insensitive = True


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print(f'{bot.user.id}')
    bot.add_view(TICKET())
    bot.add_view(CLOSE())
    bot.add_view(ORDERBUTTON(bot))
    bot.add_view(BUTTON2(bot))
    bot.add_view(BUTTON1(bot))


@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send(f'my default prefix is `%` or <@!{bot.user.id}>')
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))

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
                            new=f'🎟️ {command.name}  --> '
                            value=value+new
                            new=f'{command.help}\n\n' or '``No description Yet.``\n'
                            value=value+new+f'``aliases={command.aliases}``\n\n'
                            value=value.replace('\'', '')
              embed= discord.Embed(description=f'{cog.qualified_name}\n'+value, color=discord.Color(0xFFFFFF))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text=f'Requested by {classer.context.author.name}')
              embed.set_thumbnail(url=self.bot.user.avatar.url)

              await interaction.message.edit(embed = embed)



@bot.event
async def on_guild_join(guild):
    data = {}
    for member in guild.members:
        data[str(member.id)] = 0

    with open('cogs/values.json', 'r') as f:
        datajson = json.load(f)

    datajson[str(guild.id)] = data

    with open("cogs/values.json", "w") as f:
        json.dump(datajson, f, indent=4)


initial_extensions = ['jishaku',
                      f'cogs.ModMail',
                      f'cogs.ModMailcmds',
                      f'cogs.ticket',
                      f'cogs.order',
                      f'cogs.welcome']

for extension in initial_extensions:
    try:
        bot.load_extension(extension)
        print(f'Loaded {extension}')
    except:
        print(f"Couldn't load {extension}")

# for extension in initial_extensions:
#        bot.load_extension(extension)


bot.run(str(cfg.TOKEN))
