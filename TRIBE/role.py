import discord
from discord.ext import commands
import time

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=f".", intents=intents)


@bot.event
async def on_ready():
       print('Bot is Ready!!')
       print(f'{bot.user}')
       print(f'{bot.user.id}')

@bot.command()
async def role(ctx, role: discord.Role):
       i=0
       for members in ctx.guild.members:
              
              try:
                     await members.add_roles(role)
                     '''await ctx.send(f'Sent to {members.name}', delete_after=1)'''
                     '''time.sleep(0.1)'''
                     i+=1
                     print(i)
              except:
                     await ctx.send(f'Couldnt add to {members.name}', delete_after=1)
                     '''time.sleep(0.1)'''
                     i+=1
                     print(i)

bot.run('ODg0MDMzODYzNDE5MDM5Nzc1.YTSmsQ.XdQwYL5clI6r__vHXInvvw-zV9g')