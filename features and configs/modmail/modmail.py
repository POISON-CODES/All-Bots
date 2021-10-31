from datetime import datetime
import discord
import sys
from discord import embeds
from discord.ext import commands
from discord.ext.commands import Greedy
import time
import json
import asyncio
from discord.role import Role


class ModMail(commands.Cog):

       def __init__(self, bot):
              self.bot = bot

       
       @commands.Cog.listener()
       async def on_message(self, message):

              ######################     JSON      #################
              with open("config.json", "r") as f:
                     config=json.load(f)

              server_id = config['GUILD']['GUILD_ID']
              server = self.bot.get_guild(int(server_id))
              Role1 = server.get_role(int(config['MODMAIL']['MOD_ROLE']))
              ping_bool=server.get_role(str(config['MODMAIL']['PING_BOOL']))

              ######################      JSON      #################


              if message.guild == None:
                     pass
              else:
                     return

              if message.author==self.bot.user:
                     return

              if len(message.content) > 1000:
                     await message.author.send('Your message is too long.')

              embed = discord.Embed(title = f"{server.name} ModMail", description=f"Do you want to send the following message to {server}?", color=discord.Color.yellow())
              embed.add_field(name = 'Your Message', value=message.content)
              
              if server.banner != None:
                     
                     embed.set_thumbnail(url=f"{server.banner.url}")
                     embed.set_author(name=server.name,
                            icon_url=server.banner.url)

              else:

                     embed.set_author(name=server.name)
                     
              embed.set_footer(text = f'{server.name} | {server.id}')
             

              global msg1

              try:
                     
                     msg1 = await message.author.send(embed=embed)
                     
              except: 
                     pass
              
              reactions=['✅', '❎']
              for r in reactions:
                     await msg1.add_reaction(r)

              try:
                     def check(reaction, user):
                            return str(reaction.emoji) == '✅' or str(reaction.emoji) == '❎' and user == message.author

                     reaction, user = await self.bot.wait_for('reaction_add',check=check , timeout=10)

                     if str(reaction.emoji)=='✅':
                            if user==self.bot.user:
                                   return
                            
                            already= discord.utils.get(server.text_channels, name=str(message.author.id))

                            if already==None:
                                   mail = await server.create_text_channel(name=message.author.id)

                                   overwrites = {
                                          server.default_role: discord.PermissionOverwrite(
                                          view_channel=False,
                                          ),
                                          Role1: discord.PermissionOverwrite(
                                          view_channel=True,
                                          read_messages=True,
                                          send_messages=True,
                                          )
                                          }
                                   await mail.edit(overwrites=overwrites)

                                   if str(ping_bool)=='true':
                                          await mail.send(f'{Role1.mention}')
                                   embed = discord.Embed(description=message.content)
                                   embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                                   await mail.send(embed=embed)
                            else:
                                   if str(ping_bool)=='true':
                                          await already.send(f'{Role1.mention}')
                                   
                                   embed = discord.Embed(description=message.content, color=discord.Color.green())
                                   embed.set_author(name=message.author.name, icon_url=message.author.avatar.url)
                                   await already.send(embed=embed)

                            await message.author.send('Message Sent.')


                     if str(reaction.emoji)=='❎':
                            try:
                                   await message.author.send('Aborted.')
                                   await msg1.remove_reaction(emoji='✅', member=self.bot.user)
                                   await msg1.remove_reaction(emoji='❎', member=self.bot.user)
                                   return
                            except:
                                   return

              except asyncio.TimeoutError:
                     try:
                            await message.author.send('Aborted.')
                            await msg1.remove_reaction(emoji='✅', member=self.bot.user)
                            await msg1.remove_reaction(emoji='❎', member=self.bot.user)
                            return
                     except:
                            return

def setup(bot):
       bot.add_cog(ModMail(bot))