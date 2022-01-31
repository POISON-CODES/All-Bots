import discord
from discord.ext import commands
import mysql.connector
import time
from discord.ext import buttons
from cogs.paginator import Paginator

cnx = mysql.connector.connect(user='root', password='mumbai1324',
                              host='poison-db.chlqcuovtbtk.us-east-1.rds.amazonaws.com', database='invitetracker')
cursor = cnx.cursor(buffered=True)

class MyPaginator(buttons.Paginator):
       def __init__(self, *args, **kwargs):
              super().__init__(*args, **kwargs)

class Commands(commands.Cog):
       
       def __init__(self, bot):
              self.bot = bot

              
       @commands.command(name='level')
       async def level_send(self, ctx, user: discord.User = None):
              if user == None:
                     user = ctx.author

              xp = 0

              try:
                     cursor.execute(f'SELECT * from xp_count WHERE user = {user.id}')
                     xp = dict(zip(cursor.column_names, cursor.fetchone()))

              except:

                     await ctx.send('User is inactive')

              z = int(xp['xp'])

              level = 0

              if z <= 1500:
                     level = 1

              elif z > 1500 and z < 3000:
                     level = 2

              elif z > 3000 and z < 6000:
                     level = 3

              elif z > 6000 and z < 12000:
                     level = 4

              elif z > 12000 and z < 24000:
                     level = 5

              elif z > 24000 and z < 48000:
                     level = 6
              
              elif z > 48000 and z < 96000:
                     level = 7
              
              elif z > 96000 and z < 192000:
                     level = 8
              
              elif z > 192000 and z < 384000:
                     level = 9
              
              elif z > 384000 and z < 768000:
                     level = 10
              
              elif z > 768000 and z < 1536000:
                     level = 11
              
              elif z > 1536000 and z < 3072000:
                     level = 12
              
              elif z > 3072000 and z < 6144000:
                     level = 13
              
              elif z > 6144000 and z < 12288000:
                     level = 14

              embed = discord.Embed(title=user.name, description=f'```LEVEL       --->>    {level}\n'
                                   f'XP          --->>    {z}\n'
                                   f"No. of msgs --->>    {xp['msgs']}```\n", color=discord.Color.random())

              await ctx.send(embed=embed)


       @commands.command(name="lb", brief="Shows chat leaderboard.")
       async def leaderboard(self, ctx):


              cursor.execute(f'SELECT * FROM xp_count ORDER BY xp DESC')
              data0=cursor.fetchall()
              
              list = []

              for i in range(len(data0)):
                     id = data0[i][0]
                     user = self.bot.get_user(id)

                     if user == None:
                            continue

                     if user.bot:
                            continue
                     
                     if not user in ctx.guild.members:
                            continue

                     xp = data0[i][1]
                     msgs = data0[i][2]

                     level = 0

                     if xp <= 1500:
                            level = 1

                     elif xp > 1500 and xp < 3000:
                            level = 2

                     elif xp > 3000 and xp < 6000:
                            level = 3

                     elif xp > 6000 and xp < 12000:
                            level = 4

                     elif xp > 12000 and xp < 24000:
                            level = 5

                     elif xp > 24000 and xp < 48000:
                            level = 6
                     
                     elif xp > 48000 and xp < 96000:
                            level = 7
                     
                     elif xp > 96000 and xp < 192000:
                            level = 8
                     
                     elif xp > 192000 and xp < 384000:
                            level = 9
                     
                     elif xp > 384000 and xp < 768000:
                            level = 10
                     
                     elif xp > 768000 and xp < 1536000:
                            level = 11
                     
                     elif xp > 1536000 and xp < 3072000:
                            level = 12
                     
                     elif xp > 3072000 and xp < 6144000:
                            level = 13
                     
                     elif xp > 6144000 and xp < 12288000:
                            level = 14

                     description=(f"User: {user.mention}"
                                   f'```LEVEL       --->>    {level}\n'
                                   f'XP          --->>    {xp}\n'
                                   f"No. of msgs --->>    {msgs}```"
                     )

                     list.append(description)

              page = MyPaginator(colour=0xff1493, embed=True, entries=list, length=5, title='LeaderBoard', timeout=None, use_defaults=True)
              await page.start(ctx)

              paginator = Paginator(ctx=self.context, embeds=list)
              paginator.message = await ctx.channel.send(
              embed=paginator.current_embed, view=paginator
              )

   
def setup(bot):
       bot.add_cog(Commands(bot))