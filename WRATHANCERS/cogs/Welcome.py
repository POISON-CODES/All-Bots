import discord
from discord.ext import commands


class Welcome(commands.Cog):
        def __init__(self, bot):
                self.bot = bot



        @commands.Cog.listener()
        async def on_member_join(self, member: discord.Member ):
                WELCOME_CHANNEL=944605790730350633
                WELCOME_CHANNEL=discord.utils.get(member.guild.channels, id=WELCOME_CHANNEL)
                embed=discord.Embed(title =f'Welcome {member.name       }', description=f"""❈•≫────≪•◦ <a:1_:946962164583919736> ◦•≫────≪•❈

<a:2_:946962152097452133>𝐍𝐀𝐌𝐀𝐒𝐓𝐄{member.mention}<a:2_:946962152097452133>
<a:3_:946964052490457168>𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐓𝐇𝐄
𝗪𝗥 么 𝗪𝗥𝗔𝗧𝗛𝗥𝗔𝗡𝗖𝗘𝗥𝗦𐎕<a:3_:946964052490457168>

<a:4_:946962132333891675> 𝐅𝐎𝐋𝐋𝐎𝐖 - <#944608554508255252> ⚜️
<a:4_:946962132333891675> 𝐅𝐎𝐑 𝐒𝐄𝐑𝐕𝐄𝐑 𝐄𝐗𝐏𝐈𝐃𝐀𝐓𝐈𝐎𝐍 - <#944608430054850630> ⚜️
<a:4_:946962132333891675> 𝐅𝐎𝐑 𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓 & 𝐒𝐔𝐒 - <#944642429531865098> & <#944631285941420042> ⚜️
<a:4_:946962132333891675> 𝐆𝐄𝐓 𝐃𝐑𝐄𝐒𝐒𝐄𝐃 𝐔𝐏 - <#944605883516743720> ⚜️
<a:4_:946962132333891675> 𝐅𝐎𝐑 𝐃𝐄𝐄𝐃𝐒 & 𝐃𝐄𝐁𝐓𝐒 - <#945724264328335461> ⚜️

❈•≫────≪•◦ <a:1_:946962164583919736> ◦•≫────≪•❈""")
                embed.color=0xA8001A
                embed.set_author(name=member.name, icon_url=member.display_avatar.url)
                embed.set_thumbnail(url=member.display_avatar.url)
                embed.timestamp = discord.utils.utcnow()
                embed.set_image(url='https://cdn.discordapp.com/attachments/947881116038234202/947916255136981002/standard_5.gif')
                await WELCOME_CHANNEL.send(content=f'Hello! {member.mention}', embed= embed)

                general_channel=member.guild.get_channel(944190757407969310)
                desc=f"""❈•≫─────────≪•◦ <a:1_:946962164583919736> ◦•≫─────────≪•❈
           <a:2_:946962152097452133>○○𝐍𝐄𝐖 𝐀𝐑𝐌 𝐇𝐀𝐒 𝐔𝐍𝐈𝐓𝐄𝐃○○<a:2_:946962152097452133>
                          ⛩ 𝐍𝐀𝐌𝐀𝐒𝐓𝐄 {member.mention} ⛩
                        <a:3_:946964052490457168> 𝐖𝐄𝐋𝐂𝐎𝐌𝐄  𝐓𝐎 𝐓𝐇𝐄
                     𝗪𝗥 么 𝗪𝗥𝗔𝗧𝗛𝗥𝗔𝗡𝗖𝗘𝗥𝗦𐎕<a:3_:946964052490457168> 

<a:4_:946962132333891675> 𝐅𝐎𝐑 𝐈𝐌𝐏𝐎𝐑𝐓𝐀𝐍𝐓 & 𝐒𝐔𝐒  - <#944642429531865098>
<a:4_:946962132333891675> 𝐆𝐄𝐓 𝐃𝐑𝐄𝐒𝐒𝐄𝐃 𝐔𝐏 - <#944605883516743720>
🗼 𝐖𝐄 𝐀𝐂𝐊𝐍𝐎𝐖𝐋𝐄𝐃𝐆𝐄 𝐔𝐑 𝐏𝐑𝐄𝐒𝐄𝐍𝐂𝐄 🗼

❈•≫─────────≪•◦ <a:1_:946962164583919736> ◦•≫─────────≪•❈"""
                await general_channel.send(desc)





def setup(bot):
        bot.add_cog(Welcome(bot))