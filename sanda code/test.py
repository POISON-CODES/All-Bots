import discord
from discord.ext import commands
from discord.ext.commands import Bot
import time
import re
import datetime
import json
intents =discord.Intents.default()
intents.members = True

channel3 = [832233708399755285]

class tkmbot(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        # if message.channel.id in channel3 and message.author.id == 812952184505368606 or message.channel.id in channel3 and message.author.id == 199812023775789056 :
        if message.channel.id in channel3:
            if message.content.startswith("lockall"):
                channel = self.bot.get_channel(832997143890624593)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=False, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(832997200731570206)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=False, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(807917933761527849)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=False, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(807918136077713428)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=False, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(814122165665529856)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=False, view_channel=True, read_message_history=True, add_reactions=False)
                # await message.send("**hey !!**")
                # await channel.send("**hey baby!!**")
                # channel = self.bot.get_channel(807917933761527849)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=True,view_channel=True, read_message_history=True, add_reactions=False)
                # channel = self.bot.get_channel(807918136077713428)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=True,view_channel=True, read_message_history=True, add_reactions=False)
                # channel = self.bot.get_channel(814122165665529856)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=True,view_channel=True, read_message_history=True, add_reactions=False)
                # channel = self.bot.get_channel(814122192219930655)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=True,view_channel=True, read_message_history=True, add_reactions=False)
            elif message.content.startswith("unlockall"):
                channel = self.bot.get_channel(832997143890624593)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(832997200731570206)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(807917933761527849)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(807918136077713428)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True, view_channel=True, read_message_history=True, add_reactions=False)
                channel = self.bot.get_channel(814122165665529856)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True, view_channel=True, read_message_history=True, add_reactions=False)
                # await message.send("**hey !!**")
                # await channel.send("**hey baby!!**")
                # channel = self.bot.get_channel(807917933761527849)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)
                # channel = self.bot.get_channel(807918136077713428)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)
                # channel = self.bot.get_channel(814122165665529856)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)
                # channel = self.bot.get_channel(814122192219930655)
                # await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)
            elif message.content.startswith("medm4"):

                channel = self.bot.get_channel(832997143890624593)
                embed = discord.Embed(title=f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : RANDOM\nSQUAD : ASIA (TPP)\nID PASS : 12:50 PM\nSTARTING : 01:05 PM\nREGISTRATION: 11:00AM\nSLOTS: 23 AVAILABLE\n```**", color=discord.Colour(0xFFFFFF))
                meg = await channel.send(embed=embed)
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(832997200731570206)
                embed = discord.Embed(title=f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : RANDOM\nSQUAD : ASIA (TPP)\nID PASS : 1:50 PM\nSTARTING : 02:05 PM\nREGISTRATION: 11:03AM\nSLOTS: 19 AVAILABLE\n```**", color=discord.Colour(0xFFFFFF))
                meg = await channel.send(embed=embed)
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")

                # channel = self.bot.get_channel(807917933761527849)
                channel = self.bot.get_channel(814122165665529856)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                embed = discord.Embed(title=f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : RANDOM\nSQUAD : ASIA (TPP)\nID PASS : 2:50 PM\nSTARTING : 03:05 PM\nREGISTRATION: 11:06AM\nSLOTS: 19 AVAILABLE\n```**", color=discord.Colour(0xFFFFFF))
                meg = await channel.send(embed=embed)
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(807918136077713428)
                channel = self.bot.get_channel(807917933761527849)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                embed = discord.Embed(title=f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : RANDOM\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:09AM\nSLOTS: 18 AVAILABLE\n```**", color=discord.Colour(0xFFFFFF))
                meg = await channel.send(embed=embed)
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(807918136077713428)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 5:50 PM\nSTARTING : 06:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                embed = discord.Embed(title=f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : RANDOM\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:12AM\nSLOTS: 23 AVAILABLE\n```**", color=discord.Colour(0xFFFFFF))
                meg = await channel.send(embed=embed)
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(814122192219930655)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 6:50 PM\nSTARTING : 07:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                # await meg.add_reaction("<:MTB:792844123945566238>")
                # await meg.add_reaction("<a:cuba:792843777533935677>")
            elif message.content.startswith("medtu4"):
                channel = self.bot.get_channel(807917933761527849)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(807918136077713428)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(814122165665529856)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 5:50 PM\nSTARTING : 06:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(814122192219930655)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 6:50 PM\nSTARTING : 07:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                # await meg.add_reaction("<:MTB:792844123945566238>")
                # await meg.add_reaction("<a:cuba:792843777533935677>")
            elif message.content.startswith("medwe4"):
                channel = self.bot.get_channel(807917933761527849)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(807918136077713428)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(814122165665529856)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 5:50 PM\nSTARTING : 06:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(814122192219930655)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 6:50 PM\nSTARTING : 07:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                # await meg.add_reaction("<:MTB:792844123945566238>")
                # await meg.add_reaction("<a:cuba:792843777533935677>")
            elif message.content.startswith("medth4"):
                channel = self.bot.get_channel(807917933761527849)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                
                channel = self.bot.get_channel(807918136077713428)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(814122165665529856)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 5:50 PM\nSTARTING : 06:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(814122192219930655)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : ERANGLE\nSQUAD : ASIA (TPP)\nID PASS : 6:50 PM\nSTARTING : 07:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                # await meg.add_reaction("<:MTB:792844123945566238>")
                # await meg.add_reaction("<a:cuba:792843777533935677>")
            elif message.content.startswith("medf4"):
                channel = self.bot.get_channel(807917933761527849)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(807918136077713428)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(814122165665529856)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 5:50 PM\nSTARTING : 06:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(814122192219930655)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : MIRAMAR\nSQUAD : ASIA (TPP)\nID PASS : 6:50 PM\nSTARTING : 07:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                # await meg.add_reaction("<:MTB:792844123945566238>")
                # await meg.add_reaction("<a:cuba:792843777533935677>")
            elif message.content.startswith("meds4"):
                channel = self.bot.get_channel(807917933761527849)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 3:50 PM\nSTARTING : 04:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(807918136077713428)
                meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 4:50 PM\nSTARTING : 05:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                channel = self.bot.get_channel(814122165665529856)
                me=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 5:50 PM\nSTARTING : 06:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                await meg.add_reaction("<:MTB:792844123945566238>")
                await meg.add_reaction("<a:cuba:792843777533935677>")
                # channel = self.bot.get_channel(814122192219930655)
                # meg=await channel.send(f"__**\nMANAGED BY METAL BLOOD ESPORTS\n**__\n**```\nMAP : SANHOK\nSQUAD : ASIA (TPP)\nID PASS : 6:50 PM\nSTARTING : 07:05 PM\nREGISTRATION: 11:00PM\nSLOTS: 23 AVAILABLE\n```**")
                # await meg.add_reaction("<:MTB:792844123945566238>")
                # await meg.add_reaction("<a:cuba:792843777533935677>")
            elif message.content.startswith("cleanall"):
                # channel = self.bot.get_channel(807917933761527849)
                # await channel.purge(limit=200)
                file2 = open('demo4.txt', 'w')
                file2.truncate()
                file2.close()

                # elif message.content.startswith("clean4"):
                # channel = self.bot.get_channel(807918136077713428)
                # await channel.purge(limit=200)
                file2 = open('demo5.txt', 'w')
                file2.truncate()
                file2.close()
                # channel = self.bot.get_channel(814122165665529856)
                # await channel.purge(limit=200)
                file2 = open('demo3.txt', 'w')
                file2.truncate()
                file2.close()
                # channel = self.bot.get_channel(814122192219930655)
                # await channel.purge(limit=200)
                # file2 = open('demo7.txt', 'w')
                # file2.truncate()
                # file2.close()


            elif message.content.startswith("notefiy1"):
                channel = self.bot.get_channel(832997143890624593)
                await channel.send("**REGISTRATION STARTS NOW!\n<@&779965137184096267>**")
                file2 = open('demo1.txt', 'w')
                file2.truncate()
                file2.close()
            elif message.content.startswith("notefiy2"):
                channel = self.bot.get_channel(832997200731570206)
                await channel.send("**REGISTRATION STARTS NOW!\n<@&779965137184096267>**")
                file2 = open('demo2.txt', 'w')
                file2.truncate()
                file2.close()
            elif message.content.startswith("notefiy4"):
                channel = self.bot.get_channel(807917933761527849)
                await channel.send("**REGISTRATION STARTS NOW!\n<@&779965137184096267>**")
                file2 = open('demo4.txt', 'w')
                file2.truncate()
                file2.close()
            elif message.content.startswith("notefiy5"):
                channel = self.bot.get_channel(807918136077713428)
                await channel.send("**REGISTRATION STARTS NOW!\n<@&779965137184096267>**")
                file2 = open('demo5.txt', 'w')
                file2.truncate()
                file2.close()
            elif message.content.startswith("notefiy3"):
                channel = self.bot.get_channel(814122165665529856)
                await channel.send("**REGISTRATION STARTS NOW!\n<@&779965137184096267>**")
                file2 = open('demo3.txt', 'w')
                file2.truncate()
                file2.close()
                # channel = self.bot.get_channel(814122192219930655)
                # await channel.send("**REGISTRATION STARTS NOW!\n<@&797362104750833706>**")
                # file2 = open('demo7.txt', 'w')
                # file2.truncate()
                # file2.close()
            elif message.content.startswith("slotlist4pm"):
                channel = self.bot.get_channel(807917933761527849)
                await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)

                infile = 'demo4.txt'
                outfile = 'demof4.txt'
                delete_list = ["TEAM", "NAME", "-", ":"]
                fin = open(infile)
                fout = open(outfile, "w+")
                for line in fin:
                    for word in delete_list:
                        line = line.replace(word, "")
                    fout.write(line)
                fin.close()
                fout.close()
                fh = open('demof4.txt', 'r')
                channel = self.bot.get_channel(750623601107140649)
                await channel.send(f"**```\nMANAGED BY METAL BLOOD ESPORTS\nMAP : GIVEN\nSQUAD : ASIA (TPP)\nID PASS :  3:50 PM\nSTARTING : 4:05 PM```**\n**★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\nSLOT 1 | NOT TO BE OCCUPIED\n{fh.read()}SLOT 25 | NOT TO BE OCCUPIED\n\n★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\n\n⚠️ Everyone Must Sit In Alloted Slot Or Else Kick Out From The Room.\n\n⚠️ Please Download All The Maps To Avoid Kick Out From The Room.**")
                fh.close()

            elif message.content.startswith("slotlist5pm"):
                channel = self.bot.get_channel(807918136077713428)
                await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)

                infile = 'demo5.txt'
                outfile = 'demof5.txt'
                delete_list = ["TEAM", "NAME", "-", ":"]
                fin = open(infile)
                fout = open(outfile, "w+")
                for line in fin:
                    for word in delete_list:
                        line = line.replace(word, "")
                    fout.write(line)
                fin.close()
                fout.close()
                fh = open('demof5.txt', 'r')
                channel = self.bot.get_channel(790092115664568330)
                await channel.send(f"**```\nMANAGED BY METAL BLOOD ESPORTS\nMAP : GIVEN\nSQUAD : ASIA (TPP)\nID PASS :  4:50 PM\nSTARTING : 5:05 PM```**\n**★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\nSLOT 1 | NOT TO BE OCCUPIED\n{fh.read()}SLOT 25 | NOT TO BE OCCUPIED\n\n★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\n\n⚠️ Everyone Must Sit In Alloted Slot Or Else Kick Out From The Room.\n\n⚠️ Please Download All The Maps To Avoid Kick Out From The Room.**")
                fh.close()
            elif message.content.startswith("slotlist3pm"):
                channel = self.bot.get_channel(814122165665529856)
                await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)

                infile = 'demo3.txt'
                outfile = 'demof3.txt'
                delete_list = ["TEAM", "NAME", "-", ":"]
                fin = open(infile)
                fout = open(outfile, "w+")
                for line in fin:
                    for word in delete_list:
                        line = line.replace(word, "")
                    fout.write(line)
                fin.close()
                fout.close()
                fh = open('demof3.txt', 'r')
                channel = self.bot.get_channel(814122288764289044)
                await channel.send(f"**```\nMANAGED BY METAL BLOOD ESPORTS\nMAP : GIVEN\nSQUAD : ASIA (TPP)\nID PASS :  5:50 PM\nSTARTING : 6:05 PM```**\n**★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\nSLOT 1 | NOT TO BE OCCUPIED\n{fh.read()}SLOT 25 | NOT TO BE OCCUPIED\n\n★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\n\n⚠️ Everyone Must Sit In Alloted Slot Or Else Kick Out From The Room.\n\n⚠️ Please Download All The Maps To Avoid Kick Out From The Room.**")
                fh.close()
            # elif message.content.startswith("slotlist7pm"):
            #     channel = self.bot.get_channel(814122192219930655)
            #     await channel.set_permissions(message.guild.get_role(797362104750833706), send_messages=False,view_channel=True, read_message_history=True, add_reactions=False)
            #
            #     infile = 'demo7.txt'
            #     outfile = 'demof7.txt'
            #     delete_list = ["TEAM", "NAME", "-", ":"]
            #     fin = open(infile)
            #     fout = open(outfile, "w+")
            #     for line in fin:
            #         for word in delete_list:
            #             line = line.replace(word, "")
            #         fout.write(line)
            #     fin.close()
            #     fout.close()
            #     fh = open('demof7.txt', 'r')
            #     channel = self.bot.get_channel(814122320141877258)
            #     await channel.send(f"**```\nMANAGED BY METAL BLOOD ESPORTS\nMAP : GIVEN\nSQUAD : ASIA (TPP)\nID PASS :  6:50 PM\nSTARTING : 7:05 PM```**\n**★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\nSLOT 1 | NOT TO BE OCCUPIED\n{fh.read()}SLOT 25 | NOT TO BE OCCUPIED\n\n★▬▬▬✫▬▬▬★▬▬▬★▬▬▬✫▬▬▬★▬▬▬✫▬▬▬★▬▬▬★\n\n⚠️ Everyone Must Sit In Alloted Slot Or Else Kick Out From The Room.\n\n⚠️ Please Download All The Maps To Avoid Kick Out From The Room.**")
            #     fh.close()

            elif message.content.startswith("test"):
                channel = self.bot.get_channel(814122165665529856)
                await channel.send("test :)")
            elif message.content.startswith("timee"):
                channel = self.bot.get_channel(814122165665529856)
                embed = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                      color=discord.Colour(0xFFC300))
                embed.add_field(name="SLOTS : 21 AVAILABLE", value="Registration Starts In 5 Sec", inline=False)
                hy = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                   color=discord.Colour(0xFF0000))
                hy.add_field(name="SLOTS : 21 AVAILABLE", value="Registration Starts In 4 Sec", inline=False)
                t1 = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                   color=discord.Colour(0xFFC300))
                t1.add_field(name="SLOTS : 21 AVAILABLE", value="Registration Starts In 3 Sec", inline=False)
                t2 = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                   color=discord.Colour(0xFF0000))
                t2.add_field(name="SLOTS : 21 AVAILABLE", value="Registration Starts In 2 Sec", inline=False)
                t3 = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                   color=discord.Colour(0xFFC300))
                t3.add_field(name="SLOTS : 21 AVAILABLE", value="Registration Starts In 1 Sec", inline=False)
                t4 = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                   color=discord.Colour(0xFF0000))
                t4.add_field(name="SLOTS : 21 AVAILABLE", value="Registration Starts In 0 Sec", inline=False)
                meg = await channel.send(embed=embed)
                time.sleep(1)
                await meg.edit(embed=hy)
                time.sleep(1)
                await meg.edit(embed=t1)
                time.sleep(1)
                await meg.edit(embed=t2)
                time.sleep(1)
                await meg.edit(embed=t3)
                time.sleep(1)
                await meg.edit(embed=t4)
                channel = self.bot.get_channel(814122165665529856)
                await channel.purge(limit=1)
            elif message.content.startswith("feedback"):
                channel = self.bot.get_channel(832997143890624593)
                embed = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                      color=discord.Colour(0xFFFFFF))
                embed.add_field(name="RATE  THE MACTH", value="LOBBY WAS GOOD??", inline=False)
                meg = await channel.send(embed=embed)
                await meg.add_reaction("👍")
                await meg.add_reaction("👎")
                await channel.send("<@&833008632970084382>")
                channel = self.bot.get_channel(832997200731570206)
                embed = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                      color=discord.Colour(0xFFFFFF))
                embed.add_field(name="RATE  THE MACTH", value="LOBBY WAS GOOD??", inline=False)
                meg = await channel.send(embed=embed)
                await meg.add_reaction("👍")
                await meg.add_reaction("👎")
                await channel.send("<@&833008683612766249>")
                channel = self.bot.get_channel(814122165665529856)
                embed = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                      color=discord.Colour(0xFFFFFF))
                embed.add_field(name="RATE  THE MACTH", value="LOBBY WAS GOOD??", inline=False)
                meg= await channel.send(embed=embed)
                await meg.add_reaction("👍")
                await meg.add_reaction("👎")
                await channel.send("<@&821704591384772608>")
                channel = self.bot.get_channel(807917933761527849)
                embed = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                      color=discord.Colour(0xFFFFFF))
                embed.add_field(name="RATE  THE MACTH", value="LOBBY WAS GOOD??", inline=False)
                meg = await channel.send(embed=embed)
                await meg.add_reaction("👍")
                await meg.add_reaction("👎")
                await channel.send("<@&821704711547781131>")
                channel = self.bot.get_channel(807918136077713428)
                embed = discord.Embed(title="MTB ESPORTS PUBG T3 SCRIMS",
                                      color=discord.Colour(0xFFFFFF))
                embed.add_field(name="RATE  THE MACTH", value="LOBBY WAS GOOD??", inline=False)
                meg = await channel.send(embed=embed)
                await meg.add_reaction("👍")
                await meg.add_reaction("👎")
                await channel.send("<@&821704815440166933>")

            elif message.content.startswith("t2"):
                channel = self.bot.get_channel(814127073034895411)
                embed = discord.Embed(title="MTB ESPORTS PUBG MOBILE SCRIMS \n\n",
                                      color=discord.Colour(0xFFFFFF))
                embed.add_field(name="T2 QUALIFIERS", value="UPDATING SOON\n<a:cube:760407600327163924>", inline=False)
                meg= await channel.send(embed=embed)
                await meg.add_reaction("⚙️")
            elif message.content.startswith("cleanrole"):
                with open('data.json') as f:
                    data = json.load(f)
                for rm1 in data['rmrole']:
                    # await (await message.channel.send("Removing roles...")).delete(delay=5)
                    await message.add_reaction("<a:emoji_105:842963842976055296>")
                    role = discord.utils.get(message.guild.roles, name=rm1)
                    await (await message.channel.send(f"**<a:emoji_105:842963842976055296> It Minght Take {len(role.members)} Sec's **")).delete(delay=len(role.members))
                    for member in message.guild.members:
                        if role in member.roles:
                            # print(member.roles)
                            await member.remove_roles(role)
                            time.sleep(1)
                    await message.clear_reaction("<a:emoji_105:842963842976055296>")
                    await message.add_reaction("✅")
                    await (await message.channel.send("Done!")).delete(delay=2)



            elif message.content.startswith("allroleinfo"):
                with open('data.json') as f:
                    data = json.load(f)
                for ri in data['roleinfo']:
                    role = message.guild.get_role(ri)
                    await message.channel.send(f"> {len(role.members)} Members have {role.mention} role..")

                # role = message.guild.get_role(833008683612766249)
                # await message.channel.send(f"> {len(role.members)} Members have {role.mention} role..")
                # role = message.guild.get_role(821704591384772608)
                # await message.channel.send(f"> {len(role.members)} Members have {role.mention} role..")
                # role = message.guild.get_role(821704711547781131)
                # await message.channel.send(f"> {len(role.members)} Members have {role.mention} role..")
                # role = message.guild.get_role(821704815440166933)
                # await message.channel.send(f"> {len(role.members)} Members have {role.mention} role..")
            elif message.content.startswith("unlock1"):
                channel = self.bot.get_channel(832997143890624593)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True,
                                              view_channel=True, read_message_history=True, add_reactions=False)
            elif message.content.startswith("unlock2"):
                channel = self.bot.get_channel(832997200731570206)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True,
                                              view_channel=True, read_message_history=True, add_reactions=False)
            elif message.content.startswith("unlock3"):
                channel = self.bot.get_channel(814122165665529856)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True,
                                              view_channel=True, read_message_history=True, add_reactions=False)
            elif message.content.startswith("unlock4"):
                channel = self.bot.get_channel(807917933761527849)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True,
                                              view_channel=True, read_message_history=True, add_reactions=False)
            elif message.content.startswith("unlock5"):
                channel = self.bot.get_channel(807918136077713428)
                await channel.set_permissions(message.guild.get_role(779965137184096267), send_messages=True,
                                              view_channel=True, read_message_history=True, add_reactions=False)

def setup(bot):
    bot.add_cog(tkmbot(bot))