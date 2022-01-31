import discord
import os
from discord.ext import commands
import asyncio
import datetime




description = '''An example bot to showcase the discord.ext.commands extension module.There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='+', description=description ,intents=intents)

flag = True

async def check_commands(ctx:commands.Context):
  if ctx.author.id == 724283255959978057:
    if str(ctx.command) == "switch":
        return True
    return flag
  else:
    await ctx.send('you do not have permission to use this command')
   

bot.add_check(check_commands)

@bot.command()
async def switch(ctx):
    global flag
    flag = not flag
    if flag == True:
      await ctx.send('bot will work')
    else:
      await ctx.send('bot will stop')

@bot.event
async def on_ready():
  print(f'logged in as {bot.user} (ID:{bot.user.id})')

hui = ["hui","HUI","Hui"]

@bot.command()
async def hello(ctx):
  await ctx.message.delete()
  await ctx.send('hello')

@bot.command()
async def purge(ctx, num: int):
   await ctx.channel.purge(limit=(num + 1))
@bot.command()
async def ign(ctx):
  embed=discord.Embed(title="Tile", description="Desc", color=0x00ff00)
  embed.add_field(name="Fiel1", value="hi", inline=False)
  embed.add_field(name="Field2", value="hi2", inline=False)
  await ctx.send(embed=embed)

meme = 'maa ki gaadi baap ka road'
alliance = ["alliance", "partnership"]
tryout = ["tryout", "tryouts"]
hui = ["hui", "CUI", "AMAN"]
emoji = ["-_-", ";-;", ":-:"]


@bot.event
async def on_message(message):
  msg = message.content.lower()
  if message.author == bot.user:
    return


  if any(word in msg for word in hui):
    await message.channel.send('HUI KE BACHHE BUI')


  if any(word in msg for word in emoji):
    if message.author.id != 724283255959978057 and message.author.id !=781575052133924885:
      if message.author.id != 508547372612321280:
        await message.channel.send(f'{message.author.mention} yeh dekho emojii ayaa emoji ')


  if message.content == (meme):
    await message.channel.send("samne aaya uda duga")


  if any(word in msg for word in alliance):
    ID = message.author.id
    if ID != 724283255959978057:
      await message.channel.send(f"{message.author.mention} please DM <@!676481744890888241> for alliance or partnership")


  if any(word in message.content for word in tryout):
    if message.author.id != 724283255959978057:
      channel = bot.get_channel(843710461580279809)
      await message.channel.send(f'for tryouts go to {channel.mention} and check the pinned msgs for tryouts form and after filling the form dm @Ć4D丶Pôïsöñ#0057 for further information', delete_after = 25)

  if message.content.startswith('$thumb'):
      channel = message.channel
      tembed = discord.Embed(title = "THUMB TRIGGER", description = "**give me that 👍**",footer  = "**YOU HAVE 5 seconds to do so.**")
      rle = message.author.guild.get_role(816651551829524482)
      await message.channel.send(f'{rle.mention}',embed = tembed)

      def check(reaction, user):
          return user == message.author and str(reaction.emoji) == '👍'

      try:
          reaction, user = await bot.wait_for('reaction_add', timeout=5.0, check=check)
      except asyncio.TimeoutError:
          await channel.send('👎')
      else:
          await channel.send('👍')

  if message.content.lower().startswith('team name:'):
    if message.channel.id == rid:
      if len(message.mentions) >= 2:
        name = message.content.split('\n')[0]
        manager = message.author
        await message.channel.send(f'{manager.mention}YOUR REGISTRATION WAS SUCCESSFUL FOR YOUR TEAM : {name}. YOUR TEAM WILL BE MENTIONED IN {slotlist.name} {slotlist.mention}. FURTHER INFO WILL BE GIVEN TO YOU BY OUR MODS.')
        #await message.author.add_roles(Bot.get_role('852837699731193886'))
        await message.author.add_roles(discord.utils.get(message.guild.roles, name = "QUALIFIERS"))
        await slotlist.send(f'{manager.mention} {name}')
      else:
        await message.channel.send(f'{message.author.mention} you need 5 mentions for a successful registration whereas you only have {len(message.mentions)}')
  await bot.process_commands(message)

@bot.command() 
async def announce(ctx, channel: discord.TextChannel, *, args):
  """this is for announcemet"""
  print(str(channel.id))
  await channel.send(args)

@bot.command()
async def rolemem(ctx, role: discord.Role):
  content = ""
  num = 0
  for member in role.members:
    content += f" | `     {member.name}#{member.discriminator}     `"
    num = num + 1
    if not content:
      content = "0 members have that role" 
    
  await ctx.send(embed=discord.Embed(title=f"{num}Members having the role", description=content))

@bot.command()
async def dm(ctx, member: discord.Member , *, args):
    await ctx.message.delete()
    await member.send(args)


@bot.command()
async def dmrole(ctx, role: discord.Role , *, args):
  for members in role.members:
    try :
      await members.send(args)
      await ctx.send(f'message sent to {members.mention}')
    except discord.Forbidden:
      await ctx.send(f'message not sent to{members.mention}')

regi_channel = ' '
slotlist = ' '
@bot.command()
async def regi(ctx, channel: discord.TextChannel):
  global regi_channel 
  regi_channel = channel
  global rid
  rid = regi_channel.id
  await ctx.send(f'regi channel registered as {regi_channel.mention}')



@bot.command()
async def ticket(ctx):
    guild = ctx.guild
    embed = discord.Embed(title = '**Ticket system**',description = '**React :envelope_with_arrow: to make a ticket.**',color = 0)
    embed.set_footer(text=f"**REACT WITHIN 10 SECONDS**")
    msg = await ctx.send(embed = embed)
    tkt = await msg.add_reaction('📩')
    try:  
      def check(reaction, user):
        return str(reaction.emoji) == '📩' and user != bot.user
      reaction, user = await bot.wait_for('reaction_add', check = check, timeout = 10)
      await ctx.send('**TICKET CHANNEL WILL BE CREATED**')
      channel = await guild.create_text_channel(name = f"{ctx.author}")
      embed2 = discord.Embed(title = f"TICKET {ctx.author}", description = "Help will be with you shortly")
      await channel.send(f'<@&811883563090706433>\n {ctx.author.mention}', embed = embed2)
    except asyncio.TimeoutError:
      embed = discord.Embed(title = 'Ticket cancelled',description = 'Reaction not receieved',color = 0)
      embed.set_footer(text="React `+ticket` to create another ticker")
      await ctx.send(embed = embed)


bot.run('ODY4ODAxMDczMTIzNTkwMjA1.YP08DQ.xTDV21p7chYTF5w2dLZ0SS6lvQ4')