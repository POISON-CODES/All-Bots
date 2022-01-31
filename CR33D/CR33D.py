import discord
from discord.ext import commands


description = '''An example bot to showcase the discord.ext.commands extension module.There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='--', description=description ,intents=intents)

@bot.event
async def on_ready():
  print(f'logged in as {bot.user},{bot.user.id}')

@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send('my default prefix is `--`')
    await bot.process_commands(message)


@bot.command() 
async def announce(ctx, channel: discord.TextChannel, *, args):
  """--announce 'mention channel'  'announcement'"""
  print(str(channel.id))
  await channel.send(args)

@bot.command()
async def dm(ctx, member: discord.Member , *, args):
  """--dm `user mention' 'message'"""
  await ctx.message.delete()
  await member.send(args)

@bot.command()
async def purge(ctx, num: int):
   await ctx.channel.purge(limit=(num + 1))


bot.run('ODM5NTU5OTc5NjQ4Mjg2ODAw.YJLbKQ.6Turs0rbUJbcjZbZOW6PnCA31FI')