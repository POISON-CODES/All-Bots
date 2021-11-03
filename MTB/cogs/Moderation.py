import discord
from discord.ext import commands
import time
import asyncio

from discord.ui import view


class Confirmation(discord.ui.View):
       def __init__( self):
              super().__init__(timeout = 15)
              self.value = None


       @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
       async def green(self, button: discord.ui.Button, interaction: discord.Interaction):
              self.value = True
              self.stop()


       @discord.ui.button(label='Cancel', style=discord.ButtonStyle.danger)
       async def red(self, button: discord.ui.Button, interaction: discord.Interaction):
              self.value =  False
              self.stop()

class Moderation(commands.Cog):
       def __init__(self, bot):
              self.bot = bot
              
       @commands.command()
       @commands.has_permissions(administrator = True)
       async def kick(self, ctx, user: discord.User, reason = None):
              if reason == None:
                     reason = "No reason provided."

              name = user.name
              view = Confirmation()

              embed = discord.Embed(title = "Kick", description = f'Are you sure you want to kick {user.mention}?\n Reason : ```{reason}```', color = discord.Color.red())
              confirmation = await ctx.send(embed = embed, view = view)

              await view.wait()
              if view.value == None:
                     return
              elif view.value == True:
                     try:
                            await user.kick(reason=reason)
                            await ctx.send(f'<@{user.id}> was kicked ({name})!')
                            await confirmation.delete()
                     except:
                            await ctx.send(f"I cannot kick {user.mention}", delete_after=5)
                            await confirmation.delete()

              elif view.value == False:
                     await ctx.send(f'Aborting.', delete_after = 5)
                     await confirmation.delete()
                     return

       @kick.error
       async def UserMissing(self, ctx, error):
              if isinstance(error, commands.MissingRequiredArgument):
                     await ctx.send(f'You Forgot to mention a user', delete_after = 5)

              if isinstance(error, commands.BotMissingPermissions):
                     await ctx.send(f'I dont have permission to kick the user.')

              

def setup(bot):
       bot.add_cog(Moderation(bot))