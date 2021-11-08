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
from discord.ext import buttons 
from discord.ext.buttons import Paginator
from cogs.selfRoles import *

class MyPaginator(buttons.Paginator):
       def __init__(self, *args, **kwargs):
              super().__init__(*args, **kwargs)

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



bot = commands.Bot(command_prefix = '+' ,intents=intents, )


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

#Svshsyjhfmghjm,h

@bot.event
async def on_ready():
    bot.persistent_views_added = False

    if not bot.persistent_views_added:
        bot.add_view(Gender())
        bot.add_view(Age())
        bot.add_view(Game())
        bot.add_view(Pings())
        bot.persistent_views_added = True
    print(f'logged in as {bot.user}')   
    print(f'ID:{bot.user.id}')

@bot.event
async def on_message(message):
    if message.content.startswith(f"<@!{bot.user.id}>") and len(message.content) == len(f"<@!{bot.user.id}>"):
        await message.channel.send(f'my default prefix is `.`')
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))
    
@bot.event
async def on_invite_create(invite):
    cursor.execute(f'INSERT INTO invitecodes (inviter_id, invite_code, uses) VALUES ({invite.inviter.id}, \'{invite.code}\', {invite.uses})')
    cnx.commit()     

@bot.event
async def on_invite_delete(invite):
    cursor.execute(f'DELETE FROM invitecodes WHERE invite_code = {invite.code}')
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
            bot.inviter= inviterrrr
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
        bot.invited_users = data7['invited']
        channel = bot.get_channel(750623569255333918) 
        await channel.send(f'<a:point:758100879903031328> User Joined      : {member.mention}\n'
                           f'<a:point:758100879903031328> Invited b        : {inviterrrr.mention}\n'
                           f"<a:point:758100879903031328> Total Invites    : {bot.invited_users}\n"
                           f"<a:point:758100879903031328> Total Member Now : {len(member.guild.members)}")

    else:

        channell = bot.get_channel(883687924401598544)
        embed = discord.Embed(description = f'{member.mention} joined through the Vanity URL', color = discord.Color.blue())

        await channell.send(embed = embed)

        channel = bot.get_channel(750623569255333918) 
        await channel.send(f'<a:point:758100879903031328> User Joined      : {member.mention}\n'
                           f'<a:point:758100879903031328> Invited b        : {inviterrrr.mention}\n'
                           f"<a:point:758100879903031328> Total Invites    : {bot.invited_users}\n"
                           f"<a:point:758100879903031328> Total Member Now : {len(member.guild.members)}")       

            

@bot.event
async def on_member_remove(member: discord.Member):
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

initial_extensions = ['cogs.xp_counter',
                        'cogs.xp_commands',
                        'cogs.Invite_Commands',
                        'cogs.Moderation', 
                        'jishaku', 
                        'cogs.selfRoles']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f'Loaded {extension}')

        except:
            print(f"couldnt load extension {extension}")

'''
if __name__ == "__main__":
    for extension in initial_extensions:
        bot.load_extension(extension)
        '''

bot.run('ODgzMjMyOTcwNDE1MTUzMTcz.YTG8zQ.CoVQrRswbBi1VCjNlJ5gygiIVcM')
