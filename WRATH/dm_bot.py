from time import time
import discord
from discord.ext import commands
import time
from discord.ext.commands import Greedy

bot = commands.Bot(command_prefix = commands.when_mentioned_or(','), intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('test')
    print(f'logged in as {bot.user}')   
    print(f'ID:{bot.user.id}')

@bot.command()
@commands.has_role('DM-BOT-ADMIN')
async def massdm(ctx, role:discord.Role= None , *, args = None):
       log = bot.get_channel(924517352450687007)
       if role == None and args == None:
              await ctx.send('You did not Provide ``ROLE`` and ``MESSAGE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
              return
       if len(role.members)>50:
              await ctx.send('Too many members.')
              return
       if role == None:
              await ctx.send('No role mentioned')
              return

       if args==None:
              await ctx.send('You forgot the message to send.')
              return
       sent = 0
       cant = 0
       for members in role.members:
              try:
                     await members.send(args)
                     await log.send(f'Sent to {members.mention}')
                     sent += 1
                     time.sleep(10)
              except:
                     await log.send(f'Couldnt send to {members.mention}')
                     cant += 1 

       await log.send(f'Sent to {sent} members.\nCouldnt send to {cant} members')

@bot.command()
@commands.has_role('DM-BOT-ADMIN')
async def dm(ctx, member: Greedy[discord.Member] = None, *, args = None):
    poisont = discord.utils.get(ctx.guild.members, id = 724283255959978057)
    """--dm `user mention' 'message'"""
    if member == None and args == None:
      embed = discord.Embed(title = 'Invalid members and Message', description = 'You missed the ``members`` and ``Message`` argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention users here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by {{poisont.name}}')
      await ctx.send(embed = embed)
    elif member == None and args != None:
      embed = discord.Embed(title = 'Invalid members', description = 'You missed the ``members``argument', color = discord.Color.red())
      embed.set_footer(text = f'Bot created and developed by {{poisont.name}}')
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention users here> <your message here>\nDo not include "<>".```', inline = False)
      await ctx.send(embed = embed)
    elif member != None and args == None:
      embed = discord.Embed(title = 'Invalid Message', description = 'You missed the ``Message``argument', color = discord.Color.red())
      embed.add_field(name = 'Try:', value = f'```{ctx.prefix}dm <mention users here> <your message here>\nDo not include "<>".```', inline = False)
      embed.set_footer(text = f'Bot created and developed by {{poisont.name}}')
      await ctx.send(embed = embed)
    else:
        x = 0
        for mem0 in member:
          x = x+1
        deletable = await ctx.send(f'{x} users mentioned')

        #await ctx.message.delete()
        embed = discord.Embed(title = f'Announcement by {ctx.author.name}', description = f'{args}', color = discord.Color.random())
        embed.set_footer(text = f'Bot created and developed by {{poisont.name}}')
        for mem in member:
          try:
            await mem.send(embed = embed)
            time.sleep(2)
          except: 
            ctx.send(f'Member {mem.mention} not recieved', delete_after = 5)
        await deletable.edit(content = 'Message sent to members', delete_after = 10)


bot.run('OTI0NTE2MDk4OTU3NzgzMDUx.Ycfstg.2EE7VA89jQgDiPLS1MRxDJo8fr0')