from dis import disco
import discord
from discord.ext import commands
from discord import app_commands


from typing import Union, Optional



class Roles(commands.Cog):
        def __init__(self, bot):
                self.bot=bot
                super().__init__()

        group = app_commands.Group(name='role', description='sfbxg')

        @group.command(name='add')
        @commands.has_guild_permissions(manage_roles=True)
        @commands.bot_has_guild_permissions(manage_roles=True)
        async def role_add(self, interaction: discord.Interaction, user: Union[discord.User,discord.Member], roles: discord.Role, reason: Optional[str]):
                embed=discord.Embed(title='Summary', color=discord.Color(0xFFE100))
                await interaction.response.defer()

                if not roles < interaction.user.top_role:
                        embed.title=f'Incompatibility'
                        embed.description=f'Your Top Role is lower than {roles.mention}.\nYour Top Role needs to be higher than the Roles provided. Command Terminated.'
                        await interaction.followup.send(embed=embed, ephemeral=True)
                        return

                if not interaction.client.user.top_role > roles:
                        embed.title=f'Incompatibility'
                        embed.description=f'My Top Role is lower than provided role. Go to Server Settings and move my role above to allow me to add/remove the role.'
                        await interaction.followup.send(embed=embed, ephemeral=True)
                        return

                if roles in user.roles:
                        embed.title=f'Role Already Present.'
                        embed.description=f'The role provided is already present in users roles.'
                        await interaction.followup.send(embed=embed, ephemeral=True)
                        return
                else:
                        await user.add_roles(roles, reason='No reason provided' if reason is None else reason)


                

        
                
                

async def setup(bot):
        await bot.add_cog(Roles(bot), guilds=[discord.Object(id=770627092298596353)])