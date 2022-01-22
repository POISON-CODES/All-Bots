import discord
from discord.ext import commands
import utils.colors as c

class PBEmbeds():
       def __init__(self, bot):
              self.bot = bot

       async def BE(self, title, desc) -> discord.Embed:
              embed= discord.Embed(title=title, description=desc)
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.white()
              return embed

       async def UE(self, user, title, desc) -> discord.Embed:
              embed= discord.Embed(title=title, description=desc)
              # embed.set_footer(text = f'{user.name}', icon_url=user.avatar.url if user.avatar else None)
              embed.timestamp = discord.utils.utcnow()
              embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
              embed.color = c.white()
              return embed

       async def DescE(self, desc) -> discord.Embed:
              embed= discord.Embed(description=desc)
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.white()
              return embed

       async def Succ(self) -> discord.Embed:
              embed= discord.Embed(title="Success", description="Task was successfully completed")
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.green()
              return embed

       async def Err(self) -> discord.Embed:
              embed= discord.Embed(title="Error", description="An error occured during execution and the task was incomplete")
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.red()
              return embed

       async def MisBotPerm(self, perm) -> discord.Embed:
              embed= discord.Embed(title='Missing Permission', description=f'The bot requires {perm} permissions to complete task.')
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.orange()
              return embed

       async def MisUserPerm(self, perm) -> discord.Embed:
              embed= discord.Embed(title='Missing Permission', description=f'You do not have {perm} permissions to complete task.')
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.red()
              return embed

       async def MisChanPerm(self, perm, channel) -> discord.Embed:
              embed= discord.Embed(title='Missing Permission', description=f'The bot requires {perm} permissions in {channel.mention} to complete task.')
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.orange()
              return embed

       async def TimeOUT(self) -> discord.Embed:
              embed= discord.Embed(title='Timeout!', description=f'You Timed out! Please retry')
              # embed.set_footer(text = f'{self.bot.name}', icon_url=self.bot.avatar.url)
              embed.timestamp = discord.utils.utcnow()
              embed.color = c.red()
              return embed

       async def TicketEmbed(self, title=None, desc=None) -> discord.Embed:
              embed=discord.Embed(title=title if title is not None else f'TITLE', description=desc if desc is not None else f'DESCRIPTION')
              embed.timestamp = discord.utils.utcnow()
              embed.color= c.bg()
              return embed