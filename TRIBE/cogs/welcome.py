import discord
from discord.ext import commands
import json
from PIL import Image , ImageDraw , ImageOps , ImageFont, ImageChops
from io import BytesIO
import math
from pilmoji import Pilmoji

######################     JSON      #################
with open("config.json", "r") as f:
       config=json.load(f)

welcome_channel_id=int(config['WELCOME']['CHANNEL'])
server_id=int(config['GUILD']['GUILD_ID'])
Family_role_id=int(config['WELCOME']['ROLE'])

######################      JSON      #################

def circle(pfp, size = (215, 215)):
	pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")

	bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
	mask = Image.new('L', bigsize, 0)
	draw = ImageDraw.Draw(mask)
	draw.ellipse((0, 0) + bigsize, fill = 255)
	mask = mask.resize(pfp.size, Image.ANTIALIAS)
	mask = ImageChops.darker(mask, pfp.split()[-1])
	pfp.putalpha(mask)
	return pfp

class Welcome(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.Cog.listener()
       async def on_member_join(self, member: discord.Member):
              
              server = self.bot.get_guild(int(server_id))
              welcome_channel = server.get_channel(int(welcome_channel_id))

              await member.add_roles(server.get_role(int(Family_role_id)))

              await welcome_channel.send(f'\t \t <a:0_:898500174232559628>TRIBE GAMERZ<a:0_:898500174232559628>\n'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>\n'
                                          f'             Welcome To Our Official\n'
                                          f'                      Discord Server\n'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>\n'
                                          f'<a:ds:898500254842908702> 〢User Registered <a:ds:898500254842908702> {member.mention}\n'
                                          f'<a:ds:898500254842908702> 〢User Position   <a:ds:898500254842908702> {len(member.guild.members)}\n'
                                          f'<a:ds:898500254842908702> 〢Server Name     <a:ds:898500254842908702> {member.guild.name}\n'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>'
                                          f'<a:g_:898500090669445120><a:l_:898500076001951755><a:g_:898500090669445120><a:l_:898500076001951755>\n'
                                          f'Follow Server Rules  -  <#898495488628777010>\n'
                                          f'Want Roles? Check    -  <#898495482995806208>\n'
                                          f'Want Color? Check    -  <#898522219360174090>')


              welcome = Image.open('cogs/welcome.jpg').convert('RGBA')
              W, H = (welcome.size)
		
              pfp = member.display_avatar.with_size(1024)
              data = BytesIO(await member.display_avatar.with_size(1024).read())
              pfp = Image.open(data).convert('RGBA')

              draw = ImageDraw.Draw(welcome)
              pfp = circle(pfp, size=(240,240))		

              welcome.paste(pfp, (int(math.floor((W-240)/2)), 10), pfp)

              name_font = ImageFont.truetype("./MomcakeBold-WyonA (2).otf", 70)
		
              W, H = (welcome.size)

              text =f"{member.name}"      
              msg = text
              
              w,h = draw.textsize(msg, font=name_font)
              draw.text(((W-w)/2,625),msg, (255, 255, 255) , font =  name_font)
		
              with BytesIO() as a:
                     welcome.save(a, "PNG")
                     a.seek(0)
                     await welcome_channel.send(file = discord.File(a, 'pfp.jpg'))
			 


def setup(bot):
       bot.add_cog(Welcome(bot))