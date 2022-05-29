import discord
from discord.ext import commands
from discord import app_commands

class SlashCommands(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                super().__init__()

        @app_commands.command(name='partnership', description='Partnership Embeds.')
        @app_commands.guilds(discord.Object(id=950744623897251900))
        async def partnership(self, interaction:discord.Interaction, invite: str, user: discord.User):
                await interaction.response.send_message(f'{invite} {user.mention}', ephemeral=True)



async def setup(bot):
        await bot.add_cog(SlashCommands(bot))