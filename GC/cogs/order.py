import discord
from discord.ext import commands
from cogs.buttons import *
import json
import cogs.config as cfg

class ORDERBUTTON(discord.ui.View):
       def __init__(self, bot):
              self.bot = bot
              super().__init__(timeout=None)

       @discord.ui.button(label='Place an Order', style=discord.ButtonStyle.grey, custom_id='Place:grey')
       async def ORDER(self, button = discord.ui.Button, interaction = discord.Interaction):
              channel = await interaction.guild.create_text_channel(name = f'Unclaimed-{interaction.user.name}')
              artists = interaction.guild.get_role(int(cfg.ARTISTS))
              overwrites = {
                     interaction.user: discord.PermissionOverwrite(
                            send_messages=True,
                            view_channel=True,
                            manage_messages=False,
                            manage_channels=False,
                            manage_permissions=False
                     ),
                     artists: discord.PermissionOverwrite(
                            send_messages=True,
                            view_channel=True,
                            manage_messages=False,
                            manage_channels=False,
                            manage_permissions=False
                     ),
                     interaction.guild.default_role: discord.PermissionOverwrite(
                            send_messages=False,
                            view_channel=False,
                            manage_messages=False,
                            manage_channels=False,
                            manage_permissions=False
                     )

              }
              await channel.edit(overwrites=overwrites)

              #####################################################################
              with open('cogs/orders.json', 'r') as f:
                     data = json.load(f)

              data['CHANNELS'][str(channel.id)] = str(interaction.user.id)

              with open('cogs/orders.json','w') as f:
                     json.dump(data, f, indent = 4)
              ####################################################################

              embed = discord.Embed(title=f'Place Your Order', description=f'Place an order here.\nType `!procedure` to know the Procedure.\n`!price` to know basic price chart.\n`!form` to fill the form for our artists to understand your idea.', color = discord.Color(0x2C2F33))
              embed.set_footer(text = f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
              embed.set_thumbnail(url=interaction.guild.icon)
              embed.timestamp = discord.utils.utcnow()
              view=BUTTON1(self.bot)
              await channel.send(content = f'<@&{cfg.ARTISTS}>',embed = embed, view = view)
              await interaction.response.send_message(f'Your Ticket has been opened. {channel.mention}',ephemeral=True)

class ORDER(commands.Cog):
       def __init__(self, bot):
              self.bot = bot

       @commands.command(hidden=True)
       @commands.has_permissions(administrator = True)
       async def ORDER(self, ctx):
              embed = discord.Embed(title = 'Place an Order', description='Click on the button to create a Ticket and Place an order.', color = discord.Color(0x2C2F33))
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}', icon_url = ctx.guild.icon.url)
              embed.set_thumbnail(url=ctx.guild.icon.url)
              view = ORDERBUTTON(self.bot)
              await ctx.send(embed = embed, view= view)

       @commands.command()
       async def procedure(self, ctx):
              description = (f'Step 1: Open a ticket from <#{int(cfg.ORDER)}>\n'
                            f'In the ticket channel explain your order to the artist in the format given in `!form`.\n'
                            f'Wait for an artist to claim your Order. Once an artist claims your order, you will be notified in your DMs.\n'
                            f'After an artist has claimed your order, he/she will complete your order and notify you.\n'
                            f'In order to cancel your order, you can click **[Cancel]** Button at any point in time and the artists will be notified.\n'
                            f'In case the artist is unable to Complete your order, he/she will **[Unclaim]** your order and you need to wait till another artist accepts your request.\n'
                            f'In case of incompatibiliy, the artists may **[Reject]** your order and the ticket will be closed.')
              embed = discord.Embed(title = 'Procedure',description=description ,color = discord.Color(0x2F3136))
              embed.timestamp = discord.utils.utcnow()
              embed.set_footer(text = f'Requested by {ctx.author.name} | {ctx.author.id}')
              await ctx.send(embed = embed)

       @commands.command()
       async def price(self, ctx):
              embed = discord.Embed(title = 'Pricing', description = f'Pricing for GFX/VFX\n'
                                                                      f'Note: These pricings may vary depending on your order.', color = discord.Color(0x2F3136))
              embed.add_field(name ='GFX', value = f'1. PFP(ANYTYPE) -5INVITES/₹30\n2.NON-POPOUT AVI - 5INVITES/₹30\n3. POPOUT AVI - 6INVITES/₹40\n4. DRIP AVI - 8INVITES/₹50\n5. MANIPULATION- 10INVITES/₹60\n6. YT BANNER- 8INVITES/₹50\n7. HEADER- 8 INVITES/₹50\n8 ROSTER - 12INVITES/₹ 80\n9. THUMBNAIL(ANY) - 8INVITES/₹50\n10. 3D TEXT - 3INVITES/₹10\n11. TEXT STYLE LOGO - 12INVITES/₹80\n12, CONCEPT LOGO - 15 INVITES/₹120\n13. MASCOT LOGO - 18 INVITES/₹140\n14, WALLPAPER - 20INVITES/₹150\n15. VECOTOR - 50INVITES/₹400\n16. POSTER(TOURNEY) - 10INVITES/₹60\n17. POSTER(EVENT) - 8INVITES/₹50\n18. STATIC OVERLAY- 14INVITES/₹100\n19. LINEUP PFPS - 24INVITES/₹200 (SET OF 8)\n20. WATERMARK- 6INVITES/₹35\n', inline = False)
              embed.add_field(name= 'VFX', value = f'1. INTRO/OUTRO- 15INVITES/₹100. (EACH)\n2. ANIMATED OVERLAY- 20INVITES/₹140\n3. ANIMATED LOGO - 15INVITES/₹100 (MUST PROVIDE CONCEPT)\n4. MONTAGE EDITING (60SECS) - 25INVITES/₹200.', inline = False)
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}')
              embed.timestamp= discord.utils.utcnow()
              embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
              await ctx.send(embed = embed)

       @commands.command()
       async def form(self, ctx):
              embed = discord.Embed(title = 'Order Form', description=f'Information :-\n'
                                                        f'1) What are you ordering.\n'
                                                        f'2) Colour Scheme.\n'
                                                        f'3) an example of what are you ordering.\n'
                                                        f'4) payment method', color = discord.Color(0x2F3136))
              embed.set_footer(text = f'{ctx.guild.name} | {ctx.guild.id}')
              embed.timestamp= discord.utils.utcnow()
              embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon.url)
              await ctx.send(embed = embed)

       

def setup(bot):
       bot.add_cog(ORDER(bot))


# PFP(ANIME/AESTHETIC)- 5INVITES/₹30
# AVI- 5INVITES / ₹30
# DRIP AVI - 8INVITES/₹50
# HEADERS/BANNERS - 8INVITES/₹50
# THUMBNAILS-8INVITES/₹50
# JERSEY- 10INVITES/₹60
# ROSTER- 10 INVITES/₹60
# OVERLAY- 12INVITES/₹70
# CONCEPT LOGO- 14INVITES/₹100
# MASCOT LOGO - 16INVITES/₹120
# TOURNEY POSTER/EVENT POSTER- 10INVITES/₹60
# WATERMARK- 5INVITES/₹30
# VECTOR- 40INVITES/₹450