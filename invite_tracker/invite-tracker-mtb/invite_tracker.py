from io import StringIO
import logging
import discord
import os
from discord import channel
from discord import colour
from discord.ext import commands
import asyncio
from discord.ext.commands.core import bot_has_permissions
import mysql.connector
import mysql.connector.pooling
from discord.ext.commands.converter import InviteConverter, RoleConverter, TextChannelConverter
from urllib.parse import urlparse
import time

jdbc = "mysql://bb872c2b356f7d:fae7bb08@us-cdbr-east-04.cleardb.com/heroku_1ffe3a8238a512c?reconnect=true"
result=  urlparse(jdbc)


'''MySQLdb.connect(host=result.host,
                user=result.username,
                passwd=result.password,
                db="web3db4")'''

'''cnx = mysql.connector.connect(host=result.hostname,
                user=result.username,
                password=result.password,
                database="heroku_1ffe3a8238a512c") '''

'''dbconfig = {
  "database": "heroku_1ffe3a8238a512c",
  "user":     "bb872c2b356f7d",
  "host":     'us-cdbr-east-04.cleardb.com',
  "password": 'fae7bb08'
}'''

'''cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 3,
                                                      **dbconfig)'''

cnx = mysql.connector.connect(user='root', password='mumbai1324', host='poison-db.chlqcuovtbtk.us-east-1.rds.amazonaws.com', database='invitetracker') 
cursor = cnx.cursor(buffered = True)




description = '''Help Command for testbot'''

intents = discord.Intents.default()
intents.members = True



bot = commands.Bot(command_prefix = '.' ,intents=intents, )


class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return '%s%s %s' % (bot.command_prefix, command.qualified_name, command.signature)

    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help")
        for cog, commands in mapping.items():
           filtered = await self.filter_commands(commands, sort=True)
           command_signatures = [self.get_command_signature(c) for c in filtered]
           if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_command_help(self, command):
        embed = discord.Embed(title=self.get_command_signature(command))
        embed.add_field(name="Help", value=command.help)
        alias = command.aliases
        if alias:
            embed.add_field(name="Aliases", value=", ".join(alias), inline=False)

        channel = self.get_destination()
        await channel.send(embed=embed)

bot.help_command = MyHelp()


@bot.event
async def on_ready():
    logging.basicConfig(filename='myapp.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.info('Started')
    logging.info('Finished')
    print('test')
    print(f'logged in as {bot.user}')   
    print(f'ID:{bot.user.id}')

@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send(f'my default prefix is `.`')
    await bot.process_commands(message)



@bot.command()
@commands.has_permissions(administrator = True)
async def delete(ctx):
    cursor.execute(f'DELETE FROM invitecodes')
    cursor.execute(f'DELETE FROM invitecount')
    cursor.execute(f'DELETE FROM invited_users')
    cnx.commit()
      
    await ctx.send('deleted')

@bot.command()
async def configure(ctx):
    stringdump = ''

    inv = await ctx.guild.invites()
    x = len(inv)
    deletable = await ctx.send(f'There are {x} invites. Give me a few seconds.')
    for invite in inv:
        try:
            cursor.execute(f'INSERT INTO invitecodes (inviter_id, invite_code, uses) VALUES ({invite.inviter.id}, \'{invite.code}\', {invite.uses})')
            cnx.commit()
            #time.sleep(0.5)
            
            stringdump = stringdump + (f'{invite.inviter.id}  ===>  {invite.code}\n')
        except:
            print(f'{invite.code}\n{invite.inviter} already there')
    #file.close()
    #print(stringdump)
    with open("invite_codes.txt", "w", encoding='utf-8') as file:
        file.write(stringdump)
    with open("invite_codes.txt", "rb") as file:
        await ctx.send("Your file is:", file=discord.File(file, "invite_codes.txt"))
    await deletable.edit(content = f'done {x} invites logged', delete_after = 5)


    for members in ctx.guild.members():
        cursor.execute(f'INSERT INTO invitecount (inviter_id, invited, leaved, fake) VALUES ({members.id}, 0, 0, 0)')
        cnx.commit()
      
    
'''@bot.command()
async def upload(ctx):
    with open("result.txt", "a") as file:
        file.write('arg1 = {0}, arg2 = {1}'.format('arg1', 'arg2'))
    with open("result.txt", "rb") as file:
        await ctx.send("Your file is:", file=discord.File(file, "result.txt"))'''


@bot.command()
async def invited(ctx, user:discord.Member = None):
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


@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))



@bot.command()
async def invcount(ctx):
    inv = await ctx.guild.invites()
    x = 0
    
    for invite in inv:
        x += 1
    await ctx.send(f'There are {x} invites.')




@bot.event
async def on_invite_create(invite):
    cursor.execute(f'INSERT INTO invitecodes (inviter_id, invite_code, uses) VALUES ({invite.inviter.id}, \'{invite.code}\', {invite.uses})')
    #user = bot.get_channel(id = 883687924401598544)
    #await user.send(f'INVITE CREATED by <@!{invite.inviter.id}> code = {invite.code}')
    cnx.commit()

    
      

@bot.event
async def on_invite_delete(invite):
    cursor.execute(f'DELETE FROM invitecodes WHERE invite_code = {invite.code}')
   # cursor.execute(f'DELETE FORM invitecount WHERE inviter_id = {invite.inviter.id}')
    cnx.commit()
      

@bot.event
async def on_member_join(member: discord.Member):
    x = 0
    guild = bot.get_guild(711902380785926205)
    inssss = await guild.invites()
    for inv in inssss:
        cursor.execute(f'SELECT * FROM invitecodes WHERE invite_code = \'{inv.code}\'')
        cursor.fetchall()
              
        if cursor.rowcount == 0:
            continue

        cursor.execute(f'SELECT * FROM invitecodes WHERE invite_code = \'{inv.code}\'')
        data = dict(zip(cursor.column_names, cursor.fetchone()))
        if data['uses'] != inv.uses:
            cursor.execute(f'UPDATE invitecodes SET uses = {inv.uses} WHERE invite_code = \'{inv.code}\'')
            cnx.commit()
            global inviterrrr 
            inviterrrr = inv.inviter
            x = 1
            cnx.commit()
            break

    
    if x == 1:
        y = 0
        cursor.execute(f'SELECT * FROM invited_users WHERE inviter_id = {inviterrrr.id} AND user_invited = {member.id}')
        cursor.fetchall()
        if cursor.rowcount == 0:
            cursor.execute(f'INSERT INTO invited_users (inviter_id, user_invited) VALUES ({inviterrrr.id}, {member.id})')
            cnx.commit()

        else:
            cursor.execute(f'UPDATE invitecount SET fake = fake + 1 WHERE inviter_id = {inviterrrr.id}')
            cursor.execute(f'UPDATE invitecount SET invited = invited + 1 WHERE inviter_id = {inviterrrr.id}')
            y = 1
            cnx.commit()
            
        if y == 0:
            cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {inviterrrr.id}')
            cursor.fetchall()
            if cursor.rowcount == 0:
                cursor.execute(f'INSERT INTO invitecount (inviter_id, invited, leaved, fake) VALUES ({inviterrrr.id}, 1, 0, 0)')
                cnx.commit()

            else:
                cursor.execute(f'UPDATE invitecount SET invited = invited + 1 WHERE inviter_id = {inviterrrr.id}')
                cnx.commit()       
    
        channell = bot.get_channel(883687924401598544)
        cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {inviterrrr.id}')
        data7 = dict(zip(cursor.column_names, cursor.fetchone()))
        embed = discord.Embed(description = f"{member.mention}({member.name}) was invited by **{inviterrrr.name}**(**{data7['invited']}** invites)", color = discord.Color.green())
        await channell.send(embed = embed)

    else:

        channell = bot.get_channel(883687924401598544)
        embed = discord.Embed(description = f'{member.mention} joined through the Vanity URL', color = discord.Color.blue())

        await channell.send(embed = embed)        
          
            



@bot.event
async def on_member_remove(member):
    cursor.execute(f'SELECT * FROM invited_users WHERE user_invited = {member.id}')
    cursor.fetchall()      
    if cursor.rowcount == 0:
        
        return
    else:
        cursor.execute(f'SELECT * FROM invited_users WHERE user_invited = {member.id}')
        data = dict(zip(cursor.column_names, cursor.fetchone()))
        global invitr 
        invitr = data['inviter_id']

        cursor.execute(f'UPDATE invitecount SET leaved = leaved + 1 WHERE inviter_id = {invitr}')
        cnx.commit()
        
        return


@bot.command(brief="this is brief", help="this is help")
@commands.has_permissions(manage_guild = True)
async def invadd(ctx, user: discord.User = None, ad: int = None):
    if user == None and ad == None:
        await ctx.send('You forgot to mention user and number of invites to add.')
    elif user == None and ad != None:
        await ctx.send('You forgot to mention user.')
    elif user != None and ad == None:
        await ctx.send('You forgot to mention number of invites to add.')
    else:
        cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
        cursor.fetchall()
        if cursor.rowcount == 0:
            cursor.execute(f'INSERT INTO invitecount (inviter_id, invited, leaved, fake) VALUES ({user.id}, {ad}, 0, 0)')
        else:
            cursor.execute(f'UPDATE invitecount SET invited = invited + {ad} WHERE inviter_id = {user.id}')
    cnx.commit()
    cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
    data = dict(zip(cursor.column_names, cursor.fetchone()))
    await ctx.send(f"{ad} invtes added to {user.mention} who now has {data['invited']} invites.")



@bot.command()
@commands.has_permissions(manage_guild = True)
async def invrem(ctx, user: discord.User = None, ad: int = None):
    if user == None and ad == None:
        await ctx.send('You forgot to mention user and number of invites to remove.')
    elif user == None and ad != None:
        await ctx.send('You forgot to mention user.')
    elif user != None and ad == None:
        await ctx.send('You forgot to mention number of invites to remove.')
    else:
        cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
        cursor.fetchall()
        if cursor.rowcount == 0:
            await ctx.send('User has 0 invites.')
        else:
            cursor.execute(f'UPDATE invitecount SET invited = invited - {ad} WHERE inviter_id = {user.id}')
    cnx.commit()
    cursor.execute(f'SELECT * FROM invitecount WHERE inviter_id = {user.id}')
    data = dict(zip(cursor.column_names, cursor.fetchone()))
    await ctx.send(f"{ad} invtes removed from {user.mention} who now has {data['invited']} invites.")


'''@bot.command()
async def inv(ctx, user: discord.User = None):
    if user == None:
        user = ctx.author
    
    cursor.execute(f'SELECT * from invited_users WHERE inviter_id = {user.id}')
    cursor.fetchall()
    invs = cursor.rowcount

    embed = discord.Embed(title = f'{user.display_name}({invs}invites)')

    if cursor.rowcount == 0:
        return
    else:
        cursor.execute(f'SELECT * from invited_users WHERE inviter_id = {user.id}')
        data = dict(zip(cursor.column_names, cursor.fetchall()))
        userss = data['user_invited']
        j = 1
        for i in userss:
            userrr = bot.get_user(i)
            if userrr in ctx.guild.members:
                embed.add_field(name = f'{j}', value = f'{userrr.mention}({userrr.display_name})', inline = False)
                j += 1
            else:
                embed.add_field(name = f'{j}',value = f'{userrr.mention}({userrr.display_name}) ``- Left SERVER``', inline = False)
                j += 1
                

    await ctx.send(embed = embed)'''


initial_extensions = ['cogs.xp_counter', 'cogs.commands', 'jishaku']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run('ODgzMjMyOTcwNDE1MTUzMTcz.YTG8zQ.CoVQrRswbBi1VCjNlJ5gygiIVcM')
