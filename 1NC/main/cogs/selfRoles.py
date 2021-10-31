import discord
from discord import embeds 
from discord.ext import commands
from discord.ext.commands import Greedy
import json
import asyncio


class SR(discord.ui.View):
       
       def __init__(self):
              super().__init__(timeout=None)
              
       @discord.ui.button(label='Green', style=discord.ButtonStyle.green, custom_id='persistent_view:green')
       async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
              await interaction.response.send_message('This is green.', ephemeral=True)

       
                          


class SelfRoles(commands.Cog):

       def __init__(self, bot):
              self.bot = bot


       @commands.command()
       @commands.has_role(898993172917661737)
       async def sr1(self, ctx, role: Greedy[discord.Role]):
              embed=discord.Embed(title=ctx.guild.name, description="React on the Following to gain the Role.", color= discord.Color.random())

              for r in role:
                     embed.add_field(name = r.name, value=f'{r.mention}  ==>  ')

              
              self.bot.dict = {}
              i = 0
              for r in role:
                     await ctx.send(f'React with emoji for the following role: `@{r.name}`')

                     def check(reaction, user):
                            return str(reaction.emoji) and user == ctx.author

                     reaction, user = await self.bot.wait_for('reaction_add', check = check, timeout=15)

                     embed.set_field_at(i, name= r.name, value=f'{r.mention}  ==>  {reaction.emoji}' )

                     self.bot.dict[f'{r.id}'] = str(reaction.emoji)

                     await ctx.send(embed=embed, view=SR())


       @sr1.error
       async def MissingRole(self, ctx, error):
              if isinstance(error, commands.MissingRole):
                     await ctx.send('Too bad you dont have the power to use this command. Only my creator can use this command.')
                     return

              if isinstance(error, commands.MissingRequiredArgument):
                     await ctx.send(f'Wrong usage.\n \nCorrect Usage: {ctx.prefix}sr1 `<roles>`')
                     return

              if isinstance(error, asyncio.TimeoutError):
                     await ctx.send(f'Oops!! Too slow!!')
                     return

def setup(bot):
       bot.add_cog(SelfRoles(bot))