import discord
from discord.ext import commands
from cogs.Tickets import *


import cogs.config as cfg

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
    COLOUR = 0xFFFFFF

    def get_ending_note(self):
        return f'Use {cfg.PREFIX}[command] for more info on a command.'

    def get_command_signature(self, command):
        return '{0.qualified_name} {0.signature}'.format(command)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title='Bot Commands', colour=self.COLOUR)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            name = 'No Category' if cog is None else cog.qualified_name
            filtered = await self.filter_commands(commands, sort=True)
            value=''
            if filtered:
                for c in commands:
                    value=value+f'`{c.name}`, '
                vlast=value.rfind(', ')
                value = value[:vlast] + '' + value  [vlast + 1:]
                if cog and cog.description:
                    value = '{0}\n{1}'.format(cog.description, value)

                embed.add_field(name=name, value=value, inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_cog_help(self, cog):
        embed = discord.Embed(title='{0.qualified_name} Commands'.format(cog), colour=self.COLOUR)
        if cog.description:
            embed.description = cog.description

        filtered = await self.filter_commands(cog.get_commands(), sort=True)
        for command in filtered:
            embed.add_field(name=self.get_command_signature(command), value=command.short_doc or '...', inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    async def send_group_help(self, group):
        embed = discord.Embed(title=group.qualified_name, colour=self.COLOUR)
        if group.help:
            embed.description = group.help

        if isinstance(group, commands.Group):
            filtered = await self.filter_commands(group.commands, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command), value=command.short_doc or '...', inline=False)

        embed.set_footer(text=self.get_ending_note())
        await self.get_destination().send(embed=embed)

    # This makes it so it uses the function above
    # Less work for us to do since they're both similar.
    # If you want to make regular command help look different then override it
    send_command_help = send_group_help



bot= commands.Bot(owner_ids=[724283255959978057],help_command=EmbedHelpCommand(), command_prefix=commands.when_mentioned_or(str(cfg.PREFIX)), intents=discord.Intents.all())



@bot.event
async def on_ready():
        bot.add_view(TicketView())
        print(f'Logged in as {bot.user.name}')
        print(f'User id: {bot.user.id}')


initial_extensions = ['jishaku',
                        'cogs.Tickets',
                        'cogs.Welcome', 
                        'cogs.Booster']

from discord.ext import commands
import discord


@bot.event
async def on_message(message):
    if message.content.lower() == 'tag':
        await message.reply(f"""<a:L_Wing:945953879584038972> **__:Esteem Tags:__** <a:R_Wing:945953894813560832> 
<a:R_arrow:946275794009853962> ♞𝐖𝐑 么
<a:R_arrow:946275794009853962> ♘𝐖𝐑 么
<a:R_arrow:946275794009853962> ♞𝐖𝐑 マ
<a:R_arrow:946275794009853962> ♘𝐖𝐑 マ""")
    await bot.process_commands(message)


for extension in initial_extensions:
        bot.load_extension(extension)
        print(f'Loaded extension {extension}')


bot.run(cfg.TOKEN)      