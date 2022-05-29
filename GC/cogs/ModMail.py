import discord
from discord.ext import commands
from discord.ext.commands.errors import ExpectedClosingQuoteError
import cogs.config as cfg
import json
import asyncio


class ModMail(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.Cog.listener()
       async def on_message(self, message):
              if not message.guild == None:
                     return
              if message.author == self.bot.user:
                     return

              # with open("cogs/bans.json", "r") as f:
              #        config=json.load(f)

              # data = config['BANS']
              guild = self.bot.get_guild(int(cfg.GUILD))

              # for key in data:
              #        try:
              #               if str(message.author.id) in data[key]:
              #                      await message.channel.send("You have been banned from using this Server's Modmail.")
              #                      return 
              #        except:
              #               return

              embed = discord.Embed(title = "ModMail.", description = f"You are sending this message to **{guild.name}**.\n"
                                                                      f'React with ✅ to Confirm.\n'
                                                                      f'React with ❎ to Cancel.', color = discord.Color(0x000000))
              if not guild.icon is None:
                     embed.set_author(name = guild.name, icon_url = guild.icon.url)
                     embed.set_thumbnail(url = guild.icon)
                     embed.set_footer(text = f'{guild.name} | {guild.id}', icon_url = guild.icon.url)
              else:
                     embed.set_author(name = guild.name)
                     embed.set_footer(text = f'{guild.name} | {guild.id}')

              msg = None
              try:
                     msg = await message.channel.send(embed = embed)
              except:
                     return
              reactions = ['✅','❎']
              for reaction in reactions:
                     await msg.add_reaction(reaction)

              try:
                     def check(reaction, user):
                            return str(reaction.emoji) in reactions and user != self.bot.user

                     reaction, user = await self.bot.wait_for('reaction_add', check = check, timeout = 600)
                     if str(reaction.emoji) == '❎':
                            await msg.delete()
                            await message.channel.send('Aborted')
                            return

                     if str(reaction.emoji) == '✅':
                            channel = discord.utils.get(guild.text_channels, name=f'{str(message.author.id)}')
                            if channel == None:
                                   channel = await guild.create_text_channel(name = str(message.author.id))
                                   for role in guild.roles:
                                          if role.permissions.manage_guild == True:
                                                 overwrites = {
                                                 guild.default_role: discord.PermissionOverwrite(
                                                 view_channel=False,
                                                 ),
                                                 role: discord.PermissionOverwrite(
                                                 view_channel=True,
                                                 read_messages=True,
                                                 send_messages=True,
                                                 )
                                                 }
                                                 await channel.edit(overwrites=overwrites)
                            poison = self.bot.get_user(int(cfg.OWNER))       
                            try:
                                   poison = self.bot.get_user(int(cfg.OWNER))
                                   embed = discord.Embed(title = 'ModMail', color = discord.Color(0x00FF00))
                                   embed.timestamp = discord.utils.utcnow()
                                   embed.description=(f'{message.content}')
                                   embed.set_author(name = message.author.name, icon_url=message.author.avatar.url)
                                   if not guild.icon is None:
                                          embed.set_thumbnail(url=guild.icon)
                                   embed.set_footer(text = f'Bot Developed by {poison.name} | {poison.id}', icon_url = poison.display_avatar.url)

                                   await channel.send(embed = embed)

                                   embed = discord.Embed(title = 'Message Sent', color = discord.Color(0x00FF00))
                                   embed.description = (f'Your message was successfully sent to **{guild.name}**. Please wait for further response.')
                                   if not guild.icon is None:
                                          embed.set_author(name = f'{guild.name} | {guild.id}', icon_url = guild.icon.url)
                                   else:
                                          embed.set_author(name = f'{guild.name} | {guild.id}')
                                   embed.set_footer(text = f'Bot developed by {poison.name} | {poison.id}', icon_url = poison.display_avatar.url)
                                   embed.timestamp = discord.utils.utcnow()
                                   try:
                                          await message.channel.send(embed = embed)
                                          await msg.delete()
                                          return
                                   except:
                                          return

                            except:
                                   embed = discord.Embed(title = 'Error!!', description = f'Sending Your message Failed. Please Contant the moderators and inform <@{poison.id}> about the flaw.', color = discord.Color(0xFF1100))
                                   embed.timestamp = discord.utils.utcnow()
                                   try:
                                          await message.channel.send(embed = embed)
                                          return
                                   except:
                                          return
                            
              except asyncio.TimeoutError:
                     await msg.delete()
                     await message.channel.send('You did not choose any option')
                     return
                     
async def setup(bot):
       await bot.add_cog(ModMail(bot))