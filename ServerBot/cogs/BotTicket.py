import discord
from discord.ext import commands


import cogs.config as cfg


class BotorderPanel(discord.ui.View):
        def __init__(self):
                super().__init__(timeout=None)
        

        @discord.ui.button(label='Order Bot', style=discord.ButtonStyle.green, emoji='<a:Discord:952588204102537236>')
        async def buttton(self, button = discord.ui.Button, interaction = discord.Interaction):
                embed1=discord.Embed(description='<a:Discord:952588204102537236> | Opening your ticket....', color=0xFFFFFF)
                
                await interaction.response.send_message(embed= embed1, ephemeral = True)
                chan=await interaction.guild.create_text_channel(name=f'bot-ticket-{interaction.user.name}')
                await chan.edit(permissions={})
                await chan.set_permissions(interaction.guild.default_role, view_channel=False)
                await chan.set_permissions(interaction.user, view_channel=True, send_messages=True)
                embed3=discord.Embed(title='BOT TICKET', description=f"""{interaction.user.mention} has opened this bot ticket.
                
Help will be with you soon.

Please make sure to - 

> Read and Follow <#953171218050220083>

> Check the estime pricing by {cfg.PREFIX}price""", color=0xFFFFFF)

                await chan.send(content=interaction.user.mention, embed=embed3)
                embed2=discord.Embed(description=f'<a:tick:953168442113032273> | Ticket Opened. Please move to <#{chan.id}>', color=0xFFFFFF)
                await interaction.edit_original_message(embed=embed2)
                return


class BotTicket(commands.Cog):
        def __init__(self, bot):
                self.bot = bot
                super().__init__()


        @commands.command(name='BotPanel', hidden = True)
        @commands.has_permissions(administrator=True)
        async def Bot_ticket_panel(self, ctx):
                embed=discord.Embed(title = 'Order Bots!', description=f"""> Order Bots by Clicking on the button below.
                
**> Prices of bots depend on the features required.

> The prices are based monthly.

> Paid Bots-

\u200b> Free Hosting - `Significant Downtime`

\u200b> Paid Hosting - `Negligible Downtime`

> Free Bots

\u200b> We have the rights to take down the bots at anytime.

\u200b> If you leave the server, the bots will go offline and will be deleted.

\u200b> Only one free bot is allowed per user per server.**""", color=self.bot.COLOR)

                embed.set_footer(text=f'{self.bot.GUILD.name} | {self.bot.GUILD.id}', icon_url=self.bot.GUILD.icon.url)
                
                view=BotorderPanel()

                await ctx.send(embed =embed, view = view)



async def setup(bot):
        await bot.add_cog(BotTicket(bot))