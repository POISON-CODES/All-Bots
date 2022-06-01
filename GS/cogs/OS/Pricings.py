import discord
from discord.ext import commands

from discord import app_commands

from db import db

class PrettyTable:
  def __init__(self, headers: list):
    self.headers = [str(x) for x in headers]
    self.rows = []

  def add_row(self, items: list):
    self.rows.append([str(x) for x in items])

  def build_table(self):
    table = []
    separator = "+" + "+".join("-"*(len(header) + 5) for header in self.headers) + "+"
    table.append(separator)
    headers = "|" + "|".join(header.center(len(header) + 5) for header in self.headers) + "|"
    table.append(separator)             
    table.append(headers)  
    table.append(separator)
    for row in self.rows:
      row = "|" + "|".join(entry.center(len(header) + 5) for entry, header in zip(row, self.headers)) + "|"
      table.append(row)
      table.append(separator)
#     table.append(separator)
    return "\n".join(table)



class Pricing(commands.Cog):
        def __init__(self, bot):
                self.bot=bot


        @commands.command(name='sync')
        @commands.is_owner()
        async def syncing(self, ctx):
                await self.bot.tree.sync(guild=discord.Object(id=883054783446011936))
                await ctx.send(f'Synced.', delete_after=10)

        @app_commands.command(name='pricing')
        async def pricing_embed(self, interaction: discord.Interaction):
                embed=discord.Embed(color=discord.Color(0x5affbb))
                embed.title="Pricing."

                x=PrettyTable(["Style", "INR Price", "USD Price", "INV Price"])
                data=db.records(f"SELECT * FROM pricing")
                for a in data:
                        x.add_row([a[0], a[1], a[2], a[3]])

                embed.description=f"```{x.build_table()}```"

                await interaction.response.send_message(embed=embed, ephemeral=True)        


async def setup(bot):
        await bot.add_cog(Pricing(bot), guilds=[discord.Object(id=883054783446011936)])