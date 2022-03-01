import discord
from discord.ext import commands


class BoosterMessage(commands.Cog):
        def __init__(self, bot):
                self.bot = bot


        @commands.Cog.listener()
        async def on_member_update(self, before, after):
                before_premium_since=0
                if before.premium_since==None:
                        before_premium_since=0
                else:
                        before_premium_since=before.premium_since

                if after.premium_since==None:
                        return

                if after.premium_since==before_premium_since:
                        return

                if after.premium_since>before_premium_since:
                        description=f"""**♘ 么 𝚆𝚁𝙰𝚃𝙷𝚁𝙰𝙽𝙲𝙴𝚁𝚂𐎕** currently has **{after.guild.premium_subscription_count}** boosts!

<a:boostergif:946967327361105950> 𝐓𝐇𝐀𝐍𝐊 𝐘𝐎𝐔 𝐅𝐎𝐑 𝐒𝐀𝐋𝐔𝐃 <a:boostergif:946967327361105950>
❈•≫────≪•◦ <a:1_:946962164583919736> ◦•≫────≪•❈
<a:Crownie:945953812248662056> 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐇𝐄
𝐁𝐀𝐑𝐁𝐀𝐑𝐈𝐀𝐍 𝐊𝐍𝐎𝐓<a:Crownie:945953812248662056>
❈•≫────≪•◦ <a:1_:946962164583919736> ◦•≫────≪•❈
<a:L_Wing:945953879584038972>𝐄𝐍𝐉𝐎𝐘 𝐘𝐎𝐔𝐑 𝐒𝐓𝐀𝐘 𝐖𝐈𝐓𝐇<a:R_Wing:945953894813560832>
🗼𝐑𝐎𝐋𝐄𝐒 & 𝐇𝐎𝐒𝐏𝐈𝐓𝐀𝐋𝐈𝐓𝐘🗼"""
                        embed=discord.Embed(title = "\"Thanks For The Boost\"", description=description, color=0xFF00AE)
                        embed.set_author(name=after.name, icon_url=after.display_avatar.url)
                        embed.set_thumbnail(url = after.display_avatar.url)
                        embed.set_footer(text=f'{after.name} boosted the server :)')
                        chan=after.guild.get_channel(944608705029234768)
                        await chan.send(embed=embed)
                        role=after.guild.get_role(946991251562065951)
                        if not role in after.roles:
                                await after.add_roles(role)



def setup(bot):
        bot.add_cog(BoosterMessage(bot))