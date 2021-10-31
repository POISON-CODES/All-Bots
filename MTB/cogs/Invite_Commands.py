import discord
from discord.ext import commands
import mysql.connector
import time
from discord.ext import buttons 
from discord.ext.buttons import Paginator

cnx = mysql.connector.connect(user='root', password='mumbai1324', host='poison-db.chlqcuovtbtk.us-east-1.rds.amazonaws.com', database='invitetracker')
cursor = cnx.cursor(buffered=True)

class MyPaginator(buttons.Paginator):
       def __init__(self, *args, **kwargs):
              super().__init__(*args, **kwargs)

class InviteCommands(commands.Cog):
       
       def __init__(self, bot):
              self.bot = bot


       @commands.command(hidden = True)
       @commands.has_permissions(administrator = True)
       async def delete(self, ctx):
              cursor.execute(f'DELETE FROM invitecodes')
              cursor.execute(f'DELETE FROM invitecount')
              cursor.execute(f'DELETE FROM invited_users')
              cursor.execute(f'DELETE FROM xp_count')
              cnx.commit()
              
              await ctx.send('deleted')

       @delete.error
       async def missingpermission(self, ctx, error):
              if isinstance(error, commands.MissingPermissions):
                     await ctx.send('Oops looks like you dont have permissions')


       @commands.command(hidden = True)
       @commands.has_permissions(administrator = True)
       async def configure(self, ctx):
              inv = await ctx.guild.invites()
              x = len(inv)
              await ctx.send(f'There are {x} invites. Give me a few seconds.')
              for invite in inv:
                     try:
                            cursor.execute(f'INSERT INTO invitecodes (inviter_id, invite_code, uses) VALUES ({invite.inviter.id}, \'{invite.code}\', {invite.uses})')
                            cnx.commit()
                     
                     except:
                            print(f'{invite.code}\n{invite.inviter} already there')

              for members in ctx.guild.members():
                     cursor.execute(f'INSERT INTO invitecount (inviter_id, invited, leaved, fake) VALUES ({members.id}, 0, 0, 0)')
                     cnx.commit()


              for members in ctx.guild.members():
                     cursor.execute(f'INSERT INTO xp_count (user, xp, msgs) VALUES ({members.id}, 0, 0)')

       @configure.error
       async def missingpermission(self, ctx, error):
              if isinstance(error, commands.MissingPermissions):
                     await ctx.send('Oops looks like you dont have permissions')


       @commands.command()
       async def invited(self, ctx, user:discord.Member = None):

              if user == None:
                     user = ctx.author
              cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
              cursor.fetchall()
              if cursor.rowcount != 0:
                     cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
                     data = dict(zip(cursor.column_names, cursor.fetchone())) 
                     embed = discord.Embed(title = f'{user.name}', description = f"{user.mention} has {data['invited']} invites. ({data['invited']} invited, {data['leaved']} left, {data['fake']} fake)", color = discord.Color.blue()) 
                     await ctx.send(embed = embed)
              else:
                     embed = discord.Embed(title = f'{user.name}', description = f"{user.mention} has 0 invites. (0 invited, 0 left, 0 fake)", color = discord.Color.dark_red() )
                     await ctx.send(embed = embed)


       @commands.command()
       @commands.has_permissions(administrator = True)
       async def invcount(self, ctx):
              await ctx.send(f'There are {len(ctx.guild.invites)} invites.')

       @invcount.error
       async def missingpermission(self, ctx, error):
              if isinstance(error, commands.MissingPermissions):
                     await ctx.send('Oops looks like you dont have permissions')

       @commands.command()
       async def invitelb(self, ctx):
              cnx.reconnect(attempts=1, delay=0)
              cursor.execute(f'SELECT * FROM invitecount ORDER BY DESC')
              data0=cursor.fetchall()
                            
              list = []
              
              i=1

              for i in range(len(data0)):
                     user=data0['inviter_id']
                     invited=data0['invited']
                     left = data0['leaved']
                     fake = data0['fake']

                     user_user = self.bot.get_user(user)
                     if user_user in ctx.guild.members:
                            pass
                     else:
                            continue

                     description = (f'`{i}.`<@{user}> • **{invited}** invites. ({invited-left} regular, {left} left, {fake} fake.)')

                     list.append(description)

                     page = MyPaginator(colour=0xff1493, embed=True, entries=list, length=5, title='LeaderBoard', timeout=None, use_defaults=True)
                     await page.start(ctx)
                     cnx.reconnect(attempts=1, delay=0)

       @commands.command()
       @commands.has_permissions(administrator = True)
       async def invadd(self, ctx, user: discord.User = None, invs: int = None):

              if user == None and invs == None:
                     await ctx.send('You forgot to mention user and number of invites to add.')
              elif user == None and invs != None:
                     await ctx.send('You forgot to mention user.')
              elif user != None and invs == None:
                     await ctx.send('You forgot to mention number of invites to add.')
              else:
                     cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
                     cursor.fetchall()
                     if cursor.rowcount == 0:
                            cursor.execute(f'INSERT INTO invitecount (inviter_id, invited, leaved, fake) VALUES ({user.id}, {invs}, 0, 0)')
                            cnx.commit()
                     else:
                            cursor.execute(f'UPDATE invitecount SET invited = invited + {invs} WHERE inviter_id = {user.id}')
                            cnx.commit()

              cnx.commit()
              cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
              data = dict(zip(cursor.column_names, cursor.fetchone()))
              await ctx.send(f"{invs} invtes added to {user.mention} who now has {data['invited']} invites.")

       @invadd.error
       async def missingpermission(self, ctx, error):
              if isinstance(error, commands.MissingPermissions):
                     await ctx.send('Oops Looks like you dont have the permissions to use this command.')
              
       
   
def setup(bot):
       bot.add_cog(InviteCommands(bot))