from os import name
import discord
from discord.ext import commands
from PIL import Image , ImageDraw , ImageOps , ImageFont, ImageChops
from io import BytesIO
import math
from pilmoji import Pilmoji




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

class Memberjoins(commands.Cog):
     
	def __init__(self, bot):
	  self.bot = bot




	@commands.Cog.listener()
	async def on_member_join(self, member: discord.Member ):

		family = member.guild.get_role(898998761886449684)

		await member.add_roles(family)

		'''await self.bot.get_user(724283255959978057).send(f'ADDED FAMILY ROLE TO {member.mention}')'''
		
		guild = member.guild

		mems = len(guild.members)
		
		await self.bot.get_channel(813095809306198056).send(f' ━━━━━━━━━━━━━━━━━━━━━━━━━\n'
														   '<a:arrowright:854575621053349888> 𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐓𝐨 𝟏𝐍𝐂厶𝐢𝐧𝐞𝐫𝐚𝐭𝐞 𝐞𝐒𝐩𝐨𝐫𝐭𝐬 <a:arrowleft:854575880310751242>\n'
														   '<a:dumdum:854950982748209152> 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐃𝐈𝐒𝐂𝐎𝐑𝐃 𝐒𝐄𝐑𝐕𝐄𝐑 <a:dumdum:854950982748209152> \n'
														   ' ━━━━━━━━━━━━━━━━━━━━━━━━━\n'
														   f'<a:arrowright20:854611940998119434> 𝐔𝐬𝐞𝐫 𝐑𝐞𝐠𝐢𝐬𝐭𝐞𝐫    <a:arrowright:854575621053349888>  {member.mention}\n'
														   f'<a:arrowright20:854611940998119434> 𝐔𝐬𝐞𝐫  𝐏𝐨𝐬𝐢𝐭𝐢𝐨𝐧   <a:arrowright:854575621053349888>  {mems}\n'
														   f'<a:arrowright20:854611940998119434> 𝐒𝐞𝐫𝐯𝐞𝐫 𝐍𝐚𝐦𝐞     <a:arrowright:854575621053349888>  1NCINERATE ESPORTS\n'
														   f' ━━━━━━━━━━━━━━━━━━━━━━━━━\n'
														   f'<a:arrowright:854575621053349888> 𝐅𝐨𝐥𝐥𝐨𝐰 𝐑𝐮𝐥𝐞𝐬      <a:arrowright:854575621053349888>  <#815453533654089767>\n'
														   f'<a:arrowright:854575621053349888> 𝐏𝐮𝐛𝐥𝐢𝐜 𝐂𝐡𝐚𝐭         <a:arrowright:854575621053349888>  <#813101986303836212>\n'
														   f'<a:arrowright:854575621053349888> 𝐑𝐨𝐥𝐞𝐬                     <a:arrowright:854575621053349888>  <#813107560512225310>\n'
														   f' ━━━━━━━━━━━━━━━━━━━━━━━━━')

		'''await self.bot.get_channel(813095809306198056).send('https://cdn.discordapp.com/attachments/886532487768064030/897332578946781204/standard_2.gif')'''
		welcome = Image.open('welcome4.jpg').convert('RGBA')
		W, H = (welcome.size)
		
		pfp = member.display_avatar.with_size(1024)
		data = BytesIO(await member.display_avatar.with_size(1024).read())
		pfp = Image.open(data).convert('RGBA')

		draw = ImageDraw.Draw(welcome)
		pfp = circle(pfp, size=(240,240))		

		welcome.paste(pfp, (75, 82), pfp)

		name_font = ImageFont.truetype("./MomcakeBold-WyonA (2).otf", 50)
		'''name_font2 = ImageFont.truetype("./MomcakeBold-WyonA (2).otf", 120)
		len_font = ImageFont.truetype("./MomcakeBold-WyonA (2).otf", 180)'''

		W, H = (welcome.size)
		'''msg = "WELCOME"
		w,h = draw.textsize(msg, font=name_font)
		draw.text(((W-w)/2 ,705), msg,(179, 16, 19),  font = name_font)'''

		text =f"{member.name}"
		msg = text
		
		w,h = draw.textsize(msg, font=name_font)
		draw.text((410,230),msg, (255, 255, 255) , font =  name_font)
		
		'''msg = f"You are our {len(member.guild.members)} Member"
		w,h = draw.textsize(msg, font=len_font)
		draw.text(((W-w)/2,990), msg, (255, 255, 255), font = len_font)'''

		with BytesIO() as a:
			welcome.save(a, "PNG")
			a.seek(0)
			await self.bot.get_channel(813095809306198056).send(file = discord.File(a, 'pfp.jpg'))
			await self.bot.get_channel(813095809306198056).send('https://cdn.discordapp.com/attachments/886532487768064030/897332578946781204/standard_2.gif')


def setup(bot):
    bot.add_cog(Memberjoins(bot))
