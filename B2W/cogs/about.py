import discord
import cogs.config as cfg
from discord.ext import commands
from datetime import datetime
import sys

class POISONDM(discord.ui.View):
       def __init__(self):
              super().__init__(timeout=600)

       @discord.ui.button(label = 'Ask for Bot.', style = discord.ButtonStyle.green, custom_id = "Get_a_bot:green")
       async def BOT(self, button = discord.ui.Button, interaction = discord.Interaction):
              try:
                     poison = interaction.guild.get_member(int(cfg.OWNER))
                     await poison.send(f'<@{interaction.user.id}> Custom Bot {interaction.guild.name}')
                     await interaction.response.send_message('Your request has been sent. Kindly wait for response.', ephemeral = True)

              except:
                     await interaction.response.send_message(f'Your request could not be sent. Please DM {poison.mention}.', ephemeral = True)



class Main(commands.Cog):
       def __init__(self, bot):
              self.bot = bot


       @commands.command()
       async def about(self, ctx):
              embed = discord.Embed(title = 'About MiND', description = "**Team MîND** is an Asian/Indian based Esports Team..We started of as a team of 5 people, who are enthusiastic, creative and have a great learning attitude. We're currently centred around Call Of Duty Mobile, however, in the future, we'll be diversifying.\n"
                                   f'We affirm to fabricate an environment which encourages everyone to reap the benefits of one of the superlative gaming experiences.\n\n'
                                   f"Hope you will have an amazing time with us and we are really glad that you’ve joined us.\n\n"
                                   f'[Follow Our Instagram Handle](https://www.instagram.com/teammindftw.gg/)\n\n'
                                   f'[Twitter](https://twitter.com/Mnd1Team?t=QJB2NT8wROFvXB7ZQgcW9w&s=08)\n\n'
                                   f'[Server Link](https://discord.gg/73HdmTXrnT)\n\n'
                                   f'[Logo/Banner Link](https://media.discordapp.net/attachments/905093639225638952/906430753481560084/IMG_20210804_091026_644.jpg)'
                                   f'```yaml\nMîND Business Email : aesportscommunity@gmail.com```', color = discord.Color.green())
              embed.set_thumbnail(url=ctx.guild.icon)
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}', icon_url=ctx.guild.icon.url)
              embed.timestamp = discord.utils.utcnow()

              await ctx.send(embed = embed)


       @commands.command()
       async def serverinfo(self, ctx):
              poison = ctx.guild.get_member(int(cfg.OWNER))
              BoT = self.bot.get_user(int(cfg.BOT))
              embed = discord.Embed(title = f'About Server')
              bots = sum(i.bot for i in ctx.guild.members)
              create = ctx.guild.created_at
              final_time = create.strftime('%m/%d/%Y, %H:%M:%S')
              embed.description = (f'```yaml\n'
                                   f'Server Name       : {ctx.guild.name}\n'
                                   f'Server Owner      : {ctx.guild.owner.name}\n'
                                   f'Server Created On : {final_time}\n'
                                   f'Roles             : {len(ctx.guild.roles)}\n'
                                   f'Members           : {len(ctx.guild.members)}\n'
                                   f'Bots              : {bots}\n'
                                   f'Official Bot      : {BoT.name}\n'
                                   f'Bot Developer     : {poison.name}#{poison.discriminator}```\n'
                                   f'Server Owner      : {ctx.guild.owner.mention}\n'
                                   f'Official Bot      : {BoT.mention}\n'
                                   f'Bot Developer     : {poison.mention}')
              embed.color = discord.Color.green()
              if not ctx.guild.icon == None:
                     embed.set_footer(text=f'{ctx.guild.name} | {ctx.guild.id}', icon_url = ctx.guild.icon.url)
              embed.set_thumbnail(url=ctx.guild.icon)

              await ctx.send(embed = embed)


       @commands.command()
       async def botinfo(self, ctx):
              poison = ctx.guild.get_member(int(cfg.OWNER))

              embed = discord.Embed(title = 'About Me', color = discord.Color.green())
              embed.description = (f'I am a Discord Bot Developed by {poison.mention} for MiND Server.\n'
                                   f'Type {ctx.prefix}help for more Help.\n'
                                   f'Get a custom bot for your sever by clicking on the button below.')
              embed.add_field(name = "Python Version", value = f'```diff\n'
                                   f'- Python Version: \n+ {((sys.version).split(" "))[0]}```', inline = True)
              embed.add_field(name = "\u200b", value = "\u200b", inline = True)
              embed.add_field(name = "Bot Version", value = f'```diff\n- Bot Version: \n+ 1.1.0a\n```')
              embed.add_field(name = "Discord.py Version", value = f'```diff\n- Discord.py Version: \n+ {discord.__version__}```', inline = True)
              embed.add_field(name = "\u200b", value = "\u200b", inline = True)
              embed.add_field(name ="Bot Developer", value = f'```diff\n- Bot Developer: \n+ {poison.name}#{poison.discriminator}```', inline = True)
              embed.set_author(name = poison.name, icon_url = poison.display_avatar.url)
              # embed.set_thumbnail(url=poison.display_avatar.url)
              embed.set_footer(text = f'{poison.name} | {poison.id}', icon_url = poison.display_avatar.url)
              embed.timestamp = discord.utils.utcnow()
              view = POISONDM()
              await ctx.send(embed = embed, view = view, delete_after = 600)


def setup(bot):
       bot.add_cog(Main(bot))