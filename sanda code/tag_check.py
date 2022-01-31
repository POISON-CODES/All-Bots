import discord
from discord.ext import commands
import re

tag_checks=[796261994784489512]


class Tag(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author:
            if message.author.bot:
                return
            role = discord.utils.get(message.guild.roles, name="𒁷 ━『Scrims Manager』━")
            roles = message.author.roles
            if role in roles:
                return
        if message.channel.id in tag_checks:
            if message.content.startswith("<@"):
                if message.author.bot:
                    return
                await message.add_reaction(":warning:")
                await message.reply(f" **TAG IS IN FIRST LINE ! CHECK REGISTRATION FORMAT PLEASE..**", delete_after = 30)
            elif message.content.lower().startswith("team"):

                try:
                    mm = message.mentions[1]
                    if mm:
                        if message.author.bot:
                            return
                        await message.add_reaction(":verif_yellow:")
                        str2 = str(message.content)
                        str3 = str2.split('\n')[0]
                        str4 = str3.upper()
                        str5 = re.sub(r'^TEAM|NAME|=|-|:|-:|:-', "", str4)
                        str6 = re.sub('\s+', "", str5)

                        # await (await message.channel.send(f"{message.author.mention}  **TAG VERIFIED \n YOUR TEAM NAME : {str6}**")).delete(delay=25)
                        await message.reply(f" **TAG VERIFIED \n`` YOUR TEAM NAME : {str6}``**", delete_after = 25)

                except:
                    if message.author.bot:
                        return
                    await message.add_reaction(":loading~8:")
                    await message.reply(f"** YOU SHOULD HAVE TWO TAGS AND CHECK YOUR FORMAT**", delete_after = 25)

def setup(bot):
    bot.add_cog(Tag(bot))