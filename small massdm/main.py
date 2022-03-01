import discord
from discord.errors import HTTPException
from discord.ext import commands
import sys
import distutils
from distutils import util
import time
from discord.ext.commands.cooldowns import BucketType

#########################################################################

token = sys.argv[1]
no_bots = int(sys.argv[2])
log_id = int(sys.argv[3])
prefix = str(sys.argv[4])
print_bool = bool(distutils.util.strtobool(sys.argv[5]))
max_members = int(sys.argv[6])
bot_number=int(sys.argv[7])

#########################################################################

bot=commands.Bot(command_prefix=commands.when_mentioned_or(f'{str(prefix)}'), intents=discord.Intents.all(), help_command=None)


@bot.event
async def on_ready():
       print(f'{bot.user.name}')
       print(f'{bot.user.id}')


@bot.command(hidden=True)
@commands.max_concurrency(1, BucketType.default, wait=False)
@commands.has_permissions(administrator = True)
async def massdm(ctx, role:discord.Role = None , *, args = None):
       if len(role.members)>max_members:
              if print_bool is True:
                     await ctx.send(f'Members more than {max_members} have the role. Process aborted.')
                     return
       else:
              if print_bool == True:
                     await ctx.send(f'This role has {len(role.members)} members. Started my work.')

       log =  ctx.guild.get_channel(int(log_id))        
       counter=bot_number
       array=[]
       for mem in role.members:
              array.append(mem)
       flag = 0
       for i in range(len(array)):
              try:
                     member=array[counter]
                     await member.send(args)
                     counter=counter+no_bots
                     flag+=1
                     time.sleep(20)
                     if log==None:
                            continue
                     else:
                            await log.send(f'Sent to {member.mention}')
                            continue
              except HTTPException:
                     counter=counter+no_bots
                     if log==None:
                            continue
                     else:
                            await log.send(f'{member.mention} has their dm closed.')
                            continue
              except IndexError:
                     if print_bool == True:
                            await ctx.send(f'Task completed. Sent to {flag} members.')
                            return

@massdm.error
async def error(ctx, error):
       if isinstance(error, commands.MaxConcurrencyReached):
              await ctx.send(f'The bot is busy and currently running this command. Please wait before you can use this command again.')
              return
       
initial_extension=['jishaku']
for extension in initial_extension:
       bot.load_extension(extension)


bot.run(str(token))