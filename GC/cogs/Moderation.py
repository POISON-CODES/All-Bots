import discord
from discord.errors import Forbidden, HTTPException
import cogs.config as cfg
from discord.ext import commands
from discord.ext.commands import Greedy
import json


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        if reason is None:
            reason = 'No reason provided'

        if user.top_role.position > self.bot.top_role.position:
            await ctx.send('Users top role is higher than mine. Hence I cannot kick them.')
            return
        if user is ctx.guild.owner:
            await ctx.send('The user is the owner of this guild.')
            return
        try:
            await user.kick(reason=reason)
            await ctx.send('Mission Successful.')
            return
        except Forbidden:
            await ctx.send("Couldn't kick the user.")

        try:
            await user.kick(reason=reason)
            await ctx.send('Mission Successful.')
            return
        except HTTPException:
            await ctx.send("I Couldn't kick the user.")

    @kick.error
    async def no_user(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You did not provide the user to kick.')
            return

        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops you do not have the permissions to kick a user.')
            return

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, num=None):
        if num is None:
            await ctx.send('You forgot the `numbers` argument.\n'
                           f'Correct usage: `{ctx.prefix}purge <number of messages to purge>`')
            return
        for i in range(num):
            try:
                await ctx.channel.purge(limit=1)
            except:
                await ctx.send(f'Cannot delete further messages as they are older than 14 days.')
                return
        await ctx.channel.purge(limit=1)
        return

    @purge.error
    async def no_user(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You did not provide the number of messages to purge')
            return

        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops you do not have the permissions to purge messages')
            return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, days, users: Greedy[discord.Member]):
        for user in users:
            try:
                await user.ban(delete_message_days=days)
            except Forbidden:
                await ctx.send('I cannot ban the user.')

            except HTTPException:
                await ctx.send('Couldnt ban the user.')

    @ban.error
    async def no_args(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Invalid arguments:')
            embed = discord.Embed(title='Correct Usage', color=discord.Color(0x00FF00))
            embed.description = f'```{ctx.prefix}ban <days> <users>```'
            embed.add_field(
                value='days - The number of days to delete the users messages. [between 0 and 7]\nDefault is 0'
                      f'Users : Mention the users to ban. [You can mention multiple users.]', inline=False)

            await ctx.send(embed=embed)

        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops you do not have the permissions to purge messages')
            return

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def warn(self, ctx, users: Greedy[discord.Member], *, reason=None):
        if reason is None:
            reason = 'No reason provided'
        with open('cogs/values.json', 'r') as f:
            warns = json.load(f)
        for user in users:
            if not str(user.id) in warns:
                warns[str(ctx.guild.id)][str(user.id)] = 0
            warns[str(ctx.guild.id)][str(user.id)] = warns[str(ctx.guild.id)][str(user.id)] + 1
            try:
                await user.send(
                    f'You have been warned in **{ctx.guild.name}** by **{ctx.author.name}** for the reason: \n{reason}')
            except:
                pass
            await ctx.send(
                f'{user.mention} has been warned and it was their **{warns[str(ctx.guild.id)][str(user.id)]}** warning.')

        with open('cogs/values.json', 'w') as f:
            json.dump(warns, f, indent=4)

    @warn.error
    async def errorsss(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You forgot to mention users to warn.\n'
                           f'```{ctx.prefix}warn <users> <reason>```')
            return
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops You do not have permissions to warm members')

    @commands.command()
    @commands.has_guild_permissions(mute_members=True)
    async def mute(self, ctx, users: Greedy[discord.Member], *, reason=None):
        if reason is None:
            reason = 'No reason provided'

        muted_role = discord.utils.get(ctx.guild.roles, name=f'{ctx.guild.name} Muted')
        if muted_role is None:
            muted_role = await ctx.guild.create_role(name=f'{ctx.guild.name} Muted')
            for channel in ctx.guild.channels:
                await channel.set_permissions(muted_role, send_messages=False)
        list_members = []
        for user in users:

            try:
                await user.add_roles(muted_role)
                list_members.append(user)
            except Forbidden:
                await ctx.send(f'I cannot add roles to this user. **{user.name}**')
                continue
        desc = ''
        for user in list_members:
            desc = desc + user.name + ', '

        await ctx.send(f'Muted the following users **{desc}**')

    @mute.error
    async def errorsss(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You forgot to mention users to Mute.\n'
                           f'```{ctx.prefix}mute <users> <reason>```')
            return
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops You do not have permissions to Mute members')

    @commands.command()
    async def lock(self, ctx):
        for channel in ctx.guild.channels:
            await channel.set_permissions(ctx.guild.default_role, view_channel=False)


async def setup(bot):
    await bot.add_cog(Moderation(bot))
