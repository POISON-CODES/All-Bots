import discord
import os
from discord import channel
from discord import colour
from discord.ext import commands
import asyncio
from discord.ext.commands.core import bot_has_permissions
import time
import math
import sys
import json
import distutils
from distutils import util


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = 't' ,intents=intents)

token = "OTI0NTE2MDk4OTU3NzgzMDUx.Ycfstg.2EE7VA89jQgDiPLS1MRxDJo8fr0"
no_bots = 1
log_id = 924517352450687007
index_counter = 0
ones_inc = int(index_counter) + 1
print_bool = True
max_members = 50

if print_bool == True:
    pass
else:
    bot.help_command = None

'''token = "ODkwNjk0NjcwNzA1ODkzNDE3.YUziDQ.d872ZdfHFcXKfQlsCwK4i2uUihM"
no_bots = int(10)
log_id = int(891715335902875660)
index_counter = int(1)
ones_inc = int(index_counter) + 1
print_bool = bool(distutils.util.strtobool('False'))
max_members = int(800)'''




'''
with open(config_file, "r") as f:
     data = json.load(f)
'''


@bot.event
async def on_ready():
    print('test')
    print(f'logged in as {bot.user}')   
    print(f'ID:{bot.user.id}')
    global log_ch
    log_ch = bot.get_channel(log_id)

bot.running = False

@bot.command()
@commands.has_permissions(administrator = True)
async def massdm(ctx, role:discord.Role = None , *, args = None):
    # print(f'{print_bool} print_bool')



     if bot.running ==  True:
     #     print(f'bot running')
          if print_bool == True:
      #         print(f'{print_bool} if print_bool')
               await ctx.send("A command is already running.\nPlease wait")
               return
          else:
               pass
     
     elif role == None and args == None:
          if print_bool == True:
               await ctx.send('You did not Provide ``ROLE`` and ``MESSAGE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
               return
          else:
               pass

     elif role == None:
          if print_bool == True:
               await ctx.send('You did not Provide ``ROLE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
               return
          else:
               pass
     
     elif args == None:
          if print_bool == True:
               await ctx.send('You did not Provide ``MESSAGE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
          else:
               pass
     

     elif len(role.members) > int(max_members):
          if print_bool == True:
               await ctx.send(f'The role has more than {max_members} members')
               return
          else:
               pass
     
     else:
          
          bot.running = True

          rlmembers = role.members
          
          mems = len(rlmembers)
     
          if bool(print_bool) == True:
     
               await ctx.send(f'The role has {mems} members.')

          else:
               
              pass
      
          j = int(index_counter)

          uss = 0

          if mems%int(no_bots) >= int(ones_inc):

               uss = math.floor(mems/10) + 1
          
          else:

               uss = math.floor(mems/10)
          
          for i in range (uss):
               
               log_ch = ctx.guild.get_channel(int(log_id))
               
               poison = bot.get_user(id = 724283255959978057)
               
               try:
                    log_ch = ctx.guild.get_channel(int(log_id))
               
                    await rlmembers[j].send(args)
                    
                    await log_ch.send(f'SENT TO {rlmembers[j].mention}')

                    time.sleep(20)
               
                    j = j + int(no_bots)
          
               except:
               
                    try:
               
                         log_ch = ctx.guild.get_channel(int(log_id))
               
                         await log_ch.send(f"{rlmembers[j].mention}'s DM is closed I cannot DM them.")
                    
                         time.sleep(20)
               
                         j = j + int(no_bots)
               
                    except IndexError:
               
                         pass
               
          bot.running = False
          
          if bool(print_bool) == True:
     
               await ctx.send(f"Sent to {mems} members.")
          else:
               
              pass

@bot.command()
@commands.has_permissions(administrator = True)
async def embeddm(ctx, role:discord.Role = None , *, args = None):
     print(f'{print_bool} print_bool')

     if bot.running ==  True:
          print(f'bot running')
          if print_bool == True:
               print(f'{print_bool} if print_bool')
               await ctx.send("A command is already running.\nPlease wait")
               return
          else:
               pass
     
     elif role == None and args == None:
          if print_bool == True:
               await ctx.send('You did not Provide ``ROLE`` and ``MESSAGE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
               return
          else:
               pass

     elif role == None:
          if print_bool == True:
               await ctx.send('You did not Provide ``ROLE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
               return
          else:
               pass
     
     elif args == None:
          if print_bool == True:
               await ctx.send('You did not Provide ``MESSAGE`` argument\n'
                        'Correct Usage : ``tmassdm <ROLE> <MESSAGE>``\n'
                        'Do not include the "<>"', delete_after = 10)
          else:
               pass
     

     elif len(role.members) > int(max_members):
          if print_bool == True:
               await ctx.send(f'The role has more than {max_members} members')
               return
          else:
               pass
     
     else:
          
          bot.running = True

          rlmembers = role.members
          
          mems = len(rlmembers)
     
          if bool(print_bool) == True:
     
               await ctx.send(f'The role has {mems} members.')

          else:
               
              pass
      
          j = int(index_counter)

          uss = 0

          if mems%int(no_bots) >= int(ones_inc):

               uss = math.floor(mems/10) + 1
          
          else:

               uss = math.floor(mems/10)
          
          for i in range (uss):
               
               log_ch = ctx.guild.get_channel(int(log_id))
               
               poison = bot.get_user(id = 724283255959978057)

               
               
               try:
                    log_ch = ctx.guild.get_channel(int(log_id))

                    embed = discord.Embed(description = args)
               
                    await rlmembers[j].send(embed = embed)
                    
                    await log_ch.send(f'SENT TO {rlmembers[j].mention}')

                    time.sleep(20)
               
                    j = j + int(no_bots)
          
               except:
               
                    try:
               
                         log_ch = ctx.guild.get_channel(int(log_id))
               
                         await log_ch.send(f"{rlmembers[j].mention}'s DM is closed I cannot DM them.")
                    
                         time.sleep(20)
               
                         j = j + int(no_bots)
               
                    except IndexError:
               
                         pass
               
          bot.running = False
          
          if bool(print_bool) == True:
     
               await ctx.send(f"Sent to {mems} members.")
          else:
               
              pass

          

bot.run(token)
