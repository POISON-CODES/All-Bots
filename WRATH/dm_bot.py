from time import time
import discord
from discord.ext import commands
import time

bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'), intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('test')
    print(f'logged in as {bot.user}')   
    print(f'ID:{bot.user.id}')

@bot.command()
@commands.has_role('BOT-ADMIN')
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

bot.run('OTI0NTE2MDk4OTU3NzgzMDUx.Ycfstg.2EE7VA89jQgDiPLS1MRxDJo8fr0')