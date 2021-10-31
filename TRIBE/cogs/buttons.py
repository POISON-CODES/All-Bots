from discord.ext import buttons 
import discord
from discord.ext import commands
import discord.ui.button


class MyPaginator(buttons.Paginator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class MyCog(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command(brief='A simple example usage of the buttons ext.')
       async def testbutton(self, ctx):
              my_list = ['Hello!', 'This is a list...', '...that will become paginated soon™️', 'dvbsdfbsdfgbsdfgbdf']
              page = MyPaginator(colour=0xff1493, embed=True, entries=my_list, length=2, title='This is an example usage of buttons.', timeout=90, use_defaults=True)
              await page.start(ctx)


       @commands.command(brief="Send a message with a button!") # Create a command inside a cog
       async def button(self, ctx):
              view = discord.ui.View() # Establish an instance of the discord.ui.View class
              style = discord.ButtonStyle.gray  # The button will be gray in color
              button1 = discord.ui.Button(style=style, label="Read the docs!", url="https://discordpy.readthedocs.io/en/master")  # Create an item to pass into the view class.
              button2 = discord.ui.Button(style=discord.ButtonStyle.danger, label="✅", custom_id='button2')
              
              view.add_item(item=button1)  # Add that item into the view class  
              view.add_item(item=button2)  

              await ctx.send("This message has buttons!", view=view)  # Send your message with a button.





def setup(bot):
       bot.add_cog(MyCog(bot))