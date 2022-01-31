import discord
from discord.ext import commands
import mysql.connector
import time

cnx = mysql.connector.connect(user='root', password='mumbai1324',
                              host='poison-db.chlqcuovtbtk.us-east-1.rds.amazonaws.com', database='invitetracker')
cursor = cnx.cursor(buffered=True)


class xp_counter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author is self.bot.user:
            return
        prefix = ['.', '!', '?', '-']

        for i in prefix:
            if message.content.startswith(i):
                return

        author = message.author
        xp_new = len(message.content)

        cursor.execute(f'SELECT * FROM xp_count WHERE user={author.id}')
        cursor.fetchall()
        if cursor.rowcount == 0:
            cursor.execute(
                f'INSERT INTO xp_count (user, xp, msgs) VALUES ({author.id}, {xp_new}, 1)')
        else:
            cursor.execute(
                f'UPDATE xp_count SET xp = (xp + {xp_new}) WHERE user = {author.id}')
            cursor.execute(
                f'UPDATE xp_count SET msgs = msgs + 1 WHERE user = {author.id}')

        cnx.commit()

        await self.bot.process_commands(message)




def setup(bot):
    bot.add_cog(xp_counter(bot))
