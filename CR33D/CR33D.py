import discord
import os
from discord import embeds
from discord.ext import commands
from discord.ext.commands import Greedy
import time
from discord import ui
from discord.ext import menus


description = '''An example bot to showcase the discord.ext.commands extension module.There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='--', description=description ,intents=intents)
bot._help_command = MyMenuPages()

@bot.event
async def on_ready():
    print(f'logged in as {bot.user},{bot.user.id}')
   # update_log = bot.get_channel(878491111805583391)
    #embed = discord.Embed(title = '```BOT UPDATE```', description = 'Bot is updating please wait 60 seconds.', color = discord.Color.green())
    #x = 60
    ##y = 1
    #embed.add_field(name = f'Time remaining', value = f'```{x}...```', inline = False)
    #editable = await update_log.send(embed = embed)
    #for i in range(x):
    #  try:
    ##    x = x - 1
     #   embed = discord.Embed(title = '```BOT UPDATE```', description = 'Bot is updating please wait 60 seconds.', color = discord.Color.green())
     #   embed.add_field(name = f'Time remaining', value = f'```{x}...```', inline = False)
     #   #deletable = await update_log.send(embed = embed)
     #   time.sleep(1)
      #  await editable.edit(embed = embed)

     # except: 
        #pass
    
    #await update_log.send('Bot has been Updated as per new API Version of Discord.py')


@bot.command()
async def updates(ctx):
    embed = discord.Embed(title = 'BOT UPDATES', color = discord.Color.random())
    embed.add_field(name = 'HELP', value = '```UPDATED HELP COMMAND```', inline = False)
    embed.add_field(name = 'UPDATE', value = "```ADDED 'UPDATE' COMMAND THAT SHOWS ALL THE LATEST UPADTE TO THE BOT's CODE```", inline = False)
    embed.add_field(name = 'ANNOUNCE', value = '```ANNOUNCEMENTS WILL NOW BE IN EMBED```', inline = False)
    embed.add_field(name = 'DM', value = '```BOT CAN NOW DM MULTIPLE USERS ON A SINGLE COMMAND\nNEW SYNTAX : \n"--dm" "mention multiple users" "message to send"```', inline = False)
    embed.add_field(name = 'USABILITY', value = '```COMMANDS CAN NOW ONLY BE USED BY USERS HAVING THE ROLE \n"BOT-Admins"```', inline = False)
    embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
    await ctx.send(embed = embed)

@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send('my default prefix is `--`')
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))    

    
@bot.command()
@commands.has_role('BOT-Admins') 
async def announce(ctx, channel: discord.TextChannel = None, *, args = None):
    """--announce 'mention channel'  'announcement'"""
    if channel == None and args == None:
      embed = discord.Embed(title = 'Invalid channel and Message', description = 'You missed the ``Channel`` and ``Message`` argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}announce <mention channel here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
      await ctx.send(embed = embed)
    elif channel == None and args != None:
      embed = discord.Embed(title = 'Invalid Channel', description = 'You missed the ``Channel``argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention Channel here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
      await ctx.send(embed = embed)
    elif channel != None and args == None:
      embed = discord.Embed(title = 'Invalid Message', description = 'You missed the ``Message``argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention Channel here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
      await ctx.send(embed = embed)
    else:
        embed = discord.Embed(title = 'ANNOUNCEMENT', description = f'{args}', color = discord.Color.random())
        embed.set_thumbnail(url = ctx.guild.banner_url)
        embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
        await channel.send(embed = embed)
        '''if args.member.mentions > 0:
          for i in args.mentions:
            await ctx.send(i, delete_after = 2)
          await channel.send(args)'''

@bot.command()
@commands.has_role('BOT-Admins')
async def dm(ctx, member: Greedy[discord.Member] = None, *, args = None):
    """--dm `user mention' 'message'"""
    if member == None and args == None:
      embed = discord.Embed(title = 'Invalid members and Message', description = 'You missed the ``members`` and ``Message`` argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention users here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
      await ctx.send(embed = embed)
    elif member == None and args != None:
      embed = discord.Embed(title = 'Invalid members', description = 'You missed the ``members``argument', color = discord.Color.red())
      embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention users here> <your message here>\nDo not include "<>".```', inline = False)
      await ctx.send(embed = embed)
    elif member != None and args == None:
      embed = discord.Embed(title = 'Invalid Message', description = 'You missed the ``Message``argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention users here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
      await ctx.send(embed = embed)
    else:
        x = 0
        for mem0 in member:
          x = x+1
        deletable = await ctx.send(f'{x} users mentioned')

        #await ctx.message.delete()
        embed = discord.Embed(title = f'Announcement by {ctx.author.name}', description = f'{args}', color = discord.Color.random())
        embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
        for mem in member:
          try:
            await mem.send(embed = embed)
            time.sleep(2)
          except: 
            ctx.send(f'Member {mem.mention} not recieved', delete_after = 5)
        await deletable.edit(content = 'Message sent to members', delete_after = 10)


@bot.command()
@commands.has_role('BOT-Admins')
async def purge(ctx, num: int = None):
  if num != None:
    await ctx.channel.purge(limit=(num + 1))
    embed = discord.Embed(title = f'```{num} Messages deleted```')
    await ctx.send(embed = embed, delete_after = 1)
  else:
    embed = discord.Embed(title = 'OOPSS!!', description = 'You forgot the number argument.\n```{ctx.prefix}purge <number of messages to delete>\nDo not include "<>".```', color = discord.Color.red())
    embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
    await ctx.send(embed = embed)
'''
@bot.command()
async def help(ctx):
    embed = discord.Embed(title = 'HELP!', color = discord.Color.green())
    embed.add_field(name = 'help', value = f'```SHOWS THIS MESSAGE```', inline = False)
    embed.add_field(name = 'updates', value = f'```GIVES THE LATEST UPDATES IN THE BOTS CODE AND FEATURES.```', inline = False)
    embed.add_field(name = 'dm', value = f'```DMs SINGLE OR MULTIPLE MENTIONED USERS.```', inline = False)
    embed.add_field(name = 'purge', value = f'```DELETES A NUMBER OF MESSAGES.```', inline = False)
    embed.add_field(name = 'announce', value = f'```GIVES THE LATEST UPDATES IN THE BOTS CODE AND FEATURES.```', inline = False)
    embed.set_footer(text = f'Bot created and developed by Ć4丶Pôïsöñ#0057')
    embed.add_field(name = f'Try:', value = f'```{ctx.prefix}<command> for more help on a particular command..```', inline = False)
    await ctx.send(embed = embed)


@bot.event
async def on_message_delete(message):
  if message.author == bot.user:
    return
  else:
    if len(message.mentions) > 0:
      x = 0
      for men in message.mentions:
        if x == 0 :
          msg = f'{message.author.mention} GHOST PINGED {men.mention}'

          x = x + 1
        else:
          msg = msg + f'{men.mention}' 
          x = x + 1
      if x > 0:
        await message.channel.send(msg)
    elif len(message.role_mentions) > 0:
      x = 0
      for menr in message.role_mentions:
        if x == 0 :
          ms1g = f'{message.author.mention} GHOST PINGED {menr.name}'

          x = x + 1
        else:
          ms1g = ms1g + f'{menr.name}'
          x = x + 1
      if x > 0:
        await message.channel.send(ms1g)
    await bot.process_commands(message)'''




class MyMenuPages(ui.View, menus.MenuPages):
    def __init__(self, source, *, delete_message_after=False):
        super().__init__(timeout=60)
        self._source = source
        self.current_page = 0
        self.ctx = None
        self.message = None
        self.delete_message_after = delete_message_after

    async def start(self, ctx, *, channel=None, wait=False):
        # We wont be using wait/channel, you can implement them yourself. This is to match the MenuPages signature.
        await self._source._prepare_once()
        self.ctx = ctx
        self.message = await self.send_initial_message(ctx, ctx.channel)

    async def _get_kwargs_from_page(self, page):
        """This method calls ListPageSource.format_page class"""
        value = await super()._get_kwargs_from_page(page)
        if 'view' not in value:
            value.update({'view': self})
        return value

    async def interaction_check(self, interaction):
        """Only allow the author that invoke the command to be able to use the interaction"""
        return interaction.user == self.ctx.author

    @ui.button(emoji='<:before_fast_check:754948796139569224>', style=discord.ButtonStyle.blurple)
    async def first_page(self, button, interaction):
        await self.show_page(0)

    @ui.button(emoji='<:before_check:754948796487565332>', style=discord.ButtonStyle.blurple)
    async def before_page(self, button, interaction):
        await self.show_checked_page(self.current_page - 1)

    @ui.button(emoji='<:stop_check:754948796365930517>', style=discord.ButtonStyle.blurple)
    async def stop_page(self, button, interaction):
        self.stop()
        if self.delete_message_after:
            await self.message.delete(delay=0)

    @ui.button(emoji='<:next_check:754948796361736213>', style=discord.ButtonStyle.blurple)
    async def next_page(self, button, interaction):
        await self.show_checked_page(self.current_page + 1)

    @ui.button(emoji='<:next_fast_check:754948796391227442>', style=discord.ButtonStyle.blurple)
    async def last_page(self, button, interaction):
        await self.show_page(self._source.get_max_pages() - 1)



bot.run('ODM5NTU5OTc5NjQ4Mjg2ODAw.YJLbKQ.6Turs0rbUJbcjZbZOW6PnCA31FI')
