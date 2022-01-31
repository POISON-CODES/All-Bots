import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time
import re
intents =discord.Intents.default()
intents.members = True

perfix =["!!",".."]
bot = commands.Bot(command_prefix = perfix,intents=intents)
Counter = 3
start_time =0
end_time =0
ree = " "

def time_convert(sec):
    global ree

    mins = sec // 60

    sec = sec % 60

    hours = mins // 60

    mins = mins % 60
    ree = ("**\nSLOT FULL IN```\n{0} HOURS, {1} MINUTES, {2} SECONDS\n```**".format(int(hours),int(mins),int(sec)))



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('With MTB Staff 🤟 '))
    print(f'Connected to bot: {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
#
@bot.event
async def on_message(message):
    global Counter
    if message.content.startswith("!!"):
        await bot.process_commands(message)
        await message.channel.purge(limit=2)
        return
    if message.content.startswith(".."):
        await bot.process_commands(message)
        await message.delete()
        return
    if message.author:
        if message.author.bot:
            return
        role = discord.utils.get(message.guild.roles,name = "𒁷 ━『Scrims Manager』━")
        roles = message.author.roles
        if role in roles:
            return

@bot.command(description = "it lock specific channel @everyone",brief ="lock the channel" )
# @commands.has_role('𒁷 ━『Scrims Manager』━')
async def lock(ctx):
    global end_time
    global start_time
    global ree
    # await ctx.channel.set_permissions(ctx.guild.default_role, send_messages= False)
    # await ctx.channel.set_permissions(ctx.guild.get_role(748077689411207178), send_messages=False)
    await ctx.channel.set_permissions(ctx.guild.get_role(797362104750833706), send_messages=False,view_channel = True,read_message_history = True,add_reactions= False)
    await (await ctx.send("done_locking")).delete(delay=2)
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)
    await ctx.send(f"{ree}")
#
@bot.command(description = "it unlock specific channel @everyone",brief ="unlock the channel" )
# @commands.has_role('𒁷 ━『Scrims Manager』━')
async def unlock(ctx):
    global start_time
    # await ctx.channel.set_permissions(ctx.guild.default_role, send_messages= True)
    # await ctx.channel.set_permissions(ctx.guild.get_role(748077689411207178), send_messages=True)
    await ctx.channel.set_permissions(ctx.guild.get_role(797362104750833706), send_messages=True,view_channel = True,read_message_history = True,add_reactions = False)
    await (await ctx.send("done_unlocking ")).delete(delay=2)
    await (await ctx.send("STARTED TIMINGS ")).delete(delay=2)
    start_time = time.time()
#
@bot.command(pass_context = True,description = "it will clean messages x number of time",brief = "clean the messages [x]")
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def clean(ctx, number):
    global Counter
    if ctx.author.bot:
        return
    number = int(number)
    await ctx.channel.purge(limit=number)
    await ctx.send(f"Deleted {number} Messages")
    await ctx.channel.purge(limit=1)
    Counter = 3

@bot.command(pass_context=True)
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def giverole(ctx, role: discord.Role, members: commands.Greedy[discord.Member]):
    await ctx.message.add_reaction("⏳")
    for m in members:
        await m.add_roles(role)
        time.sleep(1)
    await ctx.message.clear_reaction("⏳")
    await ctx.message.add_reaction("✅")
    await (await ctx.send("Done!")).delete(delay=2)
    role = ctx.guild.get_role(role.id)
    await (await ctx.send(f"> Successfully Added Role To {len(role.members)} Members ")).delete(delay=5)

@bot.command(pass_context=True)
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def rerole(ctx, role: discord.Role, members: commands.Greedy[discord.Member]):
    await ctx.message.add_reaction("⏳")
    for m in members:
        await m.remove_roles(role)
        time.sleep(1)
    await ctx.message.clear_reaction("⏳")
    await ctx.message.add_reaction("✅")
    await (await ctx.send("Done!")).delete(delay=2)
    role = ctx.guild.get_role(role.id)
    await (await ctx.send(f"> Successfully Added Role To {len(role.members)} Members ")).delete(delay=5)

@bot.command(pass_context=True)
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def removeroleall(ctx, role: discord.Role):
    await (await ctx.send("Removing roles...")).delete(delay=5)
    await ctx.message.add_reaction("⏳")
    for member in ctx.guild.members:
        if role in member.roles:
            await member.remove_roles(role)
            time.sleep(1)
    await ctx.message.clear_reaction("⏳")
    await ctx.message.add_reaction("✅")
    await (await ctx.send("Done!")).delete(delay=2)
    await (await ctx.send(f"> Totalrole Is {len(role.members)}.")).delete(delay=5)


@bot.command(pass_context=True)
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def removerole(ctx, role: discord.Role, members: commands.Greedy[discord.Member]):
    await ctx.message.add_reaction("⏳")
    for m in members:
        await m.remove_roles(role)
        time.sleep(1)
    await ctx.message.clear_reaction("⏳")
    await ctx.message.add_reaction("✅")
    await (await ctx.send("Done!")).delete(delay=2)
@bot.command()
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def rolec(ctx,numeber):
    remov = {'<', '@', '>'}
    res = [word for word in re.split("\W+", numeber) if word.lower() not in remov]
    ee = res[1]
    tt = int(ee)
    role = ctx.guild.get_role(tt)
    await ctx.send(f"> {len(role.members)} Members Have Above Role")

@bot.command()
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def dm( ctx, user, *, message):
    """DM any user with UserID"""
    # TY=str(message)
    remov = {'<', '@', '>'}
    res = [word for word in re.split("\W+", user) if word.lower() not in remov]
    ee = res[1]
    tt = int(ee)
    print(tt)
    user = ctx.bot.get_user(tt)
    try:
        await user.send(message)
        await ctx.send(' | Success!')
    except:
        return await ctx.send("| Could not send message!")

@bot.command()
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def load(ctx,extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.has_role('𒁷 ━『Scrims Manager』━')
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run('ODA3OTIwMDk3OTEzMDc3NzYx.YB_AOQ.LMPdSvVa2GjVffdw9KDGVt65l4g')