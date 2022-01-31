import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import re
import datetime
intents =discord.Intents.default()
intents.members = True

# channel3 = [832997529255018526]

class idpassbot(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # if message.channel.id in channel3 and message.author.id == 812952184505368606 or message.channel.id in channel3 and message.author.id == 199812023775789056 :
        if message.channel.id == 832997529255018526 : #1pm channel
            if message.content.startswith("id") or message.content.startswith("ID") or message.content.startswith("i'd") or message.content.startswith("I'd") or message.content.startswith("Id") or message.content.startswith("I'D"):
                channel = self.bot.get_channel(807913422276526091)
                await channel.send("**```ID PASS IS GIVEN```\n JOIN QUICKLY AND ALL THE BEST GUYS **<@&843709690009747457>")
        if message.channel.id == 832997779013763122 : #2pm channel
            if message.content.startswith("id") or message.content.startswith("ID") or message.content.startswith("i'd") or message.content.startswith("I'd") or message.content.startswith("Id") or message.content.startswith("I'D"):
                channel = self.bot.get_channel(807913422276526091)
                await channel.send("**```ID PASS IS GIVEN```\nJOIN QUICKLY AND ALL THE BEST GUYS **<@&833008683612766249>")
        if message.channel.id == 814122288764289044 : #3pm channel
            if message.content.startswith("id") or message.content.startswith("ID") or message.content.startswith("i'd") or message.content.startswith("I'd") or message.content.startswith("Id") or message.content.startswith("I'D"):
                channel = self.bot.get_channel(807913422276526091)
                await channel.send("**```ID PASS IS GIVEN```\nJOIN QUICKLY AND ALL THE BEST GUYS **<@&821704591384772608>")
        if message.channel.id == 750623601107140649 : #4pm channel
            if message.content.startswith("id") or message.content.startswith("ID") or message.content.startswith("i'd") or message.content.startswith("I'd") or message.content.startswith("Id") or message.content.startswith("I'D"):
                channel = self.bot.get_channel(807913422276526091)
                await channel.send("**```ID PASS IS GIVEN```\nJOIN QUICKLY AND ALL THE BEST GUYS **<@&821704711547781131>")
        if message.channel.id == 790092115664568330 : #5pm channel
            if message.content.startswith("id") or message.content.startswith("ID") or message.content.startswith("i'd") or message.content.startswith("I'd") or message.content.startswith("Id") or message.content.startswith("I'D"):
                channel = self.bot.get_channel(807913422276526091)
                await channel.send("**```ID PASS IS GIVEN```\nJOIN QUICKLY AND ALL THE BEST GUYS **<@&821704815440166933>")

def setup(bot):
    bot.add_cog(idpassbot(bot))
