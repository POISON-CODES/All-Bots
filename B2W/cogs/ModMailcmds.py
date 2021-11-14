import discord
from discord.ext import commands
import cogs.config as cfg
import time

class ModMailCommands(commands.Cog):
       def __init__(self, bot):
              self.bot = bot


       @commands.command()
       async def reply(self, ctx, reason):
              guild = self.bot.get_guild(int(cfg.GUILD))
              if len(reason) > 1000:
                     await ctx.send('Message is too long!\nTry again with a shorter message.')
                     return
    
              embed = discord.Embed(title = f'Mod Mail', color = discord.Color(0x000000))
              embed.description = (f'{reason}')
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{guild.name} | {guild.id}', icon_url = guild.icon.url)
              embed.set_thumbnail(url=guild.icon.url)
              embed.set_author(name = f'{ctx.author.name} | {ctx.author.id}', icon_url=ctx.author.display_avatar.url)

              user = self.bot.get_user(int(ctx.channel.name))

              if user == None:
                     await ctx.reply('The user is not present in the Server, this Channel will now be deleted.')
                     time.sleep(60)
                     await ctx.channel.delete()

              try:
                     await user.send(embed = embed)
                     embed = discord.Embed(title = 'Successful.', description = f'Your message was successfully sent to <@{user.id}>.', color = discord.Color(0x00FF00))
                     embed.timestamp = discord.utils.utcnow()
                     await ctx.send(embed = embed)
                     await ctx.message.delete()
                     return

              except:
                     embed = discord.Embed(description='Your message could not be delivered. This was because the User has their DMs Closed.', color = discord.Color(0xFF1100))
                     embed.timestamp = discord.utils.utcnow()

                     await ctx.send(embed=embed)
                     await ctx.message.delete()
                     return


                     
       @reply.error
       async def noarg(self, ctx, error):
              if isinstance(error, commands.MissingRequiredArgument):
                     await ctx.send('No message given.')
                     return

       @commands.command()
       async def close(self, ctx, reason=None):
              guild = self.bot.get_guild(int(cfg.GUILD))
              if reason == None:
                     reason = 'No reason was given.'

              if len(reason) > 1000:
                     await ctx.send('Message is too long!\nTry again with a shorter message.')
                     return              

              embed = discord.Embed(title = f'Ticket Closed', color = discord.Color(0x000000))
              embed.description = (f'{reason}')
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'{guild.name} | {guild.id}', icon_url = guild.icon.url)
              embed.set_thumbnail(url=guild.icon.url)
              embed.set_author(name = f'{ctx.author.name} | {ctx.author.id}', icon_url=ctx.author.display_avatar.url)

              user = self.bot.get_user(int(ctx.channel.name))

              if user == None:
                     await ctx.reply('The user is not present in the Server, this Channel will now be deleted.')
                     time.sleep(60)
                     await ctx.channel.delete()

              try:
                     await user.send(embed = embed)
                     embed = discord.Embed(title = 'Successful.', description = f'Ticket was successfully closed for <@{user.id}>.', color = discord.Color(0x00FF00))
                     embed.timestamp = discord.utils.utcnow()
                     await ctx.send(embed = embed)
                     await ctx.message.delete()
                     time.sleep(15)
                     await ctx.channel.delete()

              except:
                     embed = discord.Embed(description='Your message could not be delivered. This was because the User has their DMs Closed.', color = discord.Color(0xFF1100))
                     embed.timestamp = discord.utils.utcnow()

                     await ctx.send(embed=embed)
                     await ctx.message.delete()
                     time.sleep(15)
                     await ctx.channel.delete()
                     return


def setup(bot):
       bot.add_cog(ModMailCommands(bot))