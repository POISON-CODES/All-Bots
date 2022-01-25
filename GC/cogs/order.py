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
              category = discord.utils.get(interaction.guild.categories, id = int(cfg.ORDER_TICK))
              channel = await category.create_text_channel(name = f'Unclaimed-{interaction.user.name}')
              support= discord.utils.get(interaction.guild.roles, id=int(cfg.SUPPORT))
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
                     ),
                     support: discord.PermissionOverwrite(
                            send_messages=True,
                            view_channel=True,
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

              embed = discord.Embed(title=f'Place Your Order', description=f'Place an order here.\nType `%procedure` to know the Procedure.\n`%price` to know basic price chart.\n`%form` to fill the form for our artists to understand your idea.', color = discord.Color(0x2C2F33))
              embed.set_footer(text = f'{interaction.guild.name} | {interaction.guild.id}', icon_url = interaction.guild.icon.url)
              embed.set_thumbnail(url=interaction.guild.icon)
              embed.timestamp = discord.utils.utcnow()
              view=BUTTON1(self.bot)
              msg=await channel.send(content = f'{interaction.user.mention} | <@&{cfg.SUPPORT}>',embed = embed, view = view)
              await msg.pin()
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
                            f'In the ticket channel explain your order to the artist in the format given in `%form`.\n'
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
              embed.add_field(name ='GFX', value = """GFX:
1. PFP(ANYTYPE) - ₹50/6 INVITES
2.NON-POPOUT AVI - ₹30/4 INVITES
3. POPOUT AVI - ₹40/6 INVITES
4. DRIP / CHROME AVI - ₹60/8 INVITES
 5.BANNER- ₹100/12 INVITES
6. HEADER- ₹100/12 INVITES
7.ROSTER - ₹80/14 INVITES
8. THUMBNAIL(ANY) - ₹60/10 INVITES
9.CONCEPT LOGO - ₹125/18 INVITES
10.MASCOT LOGO - ₹100/15 INVITES
11.POSTER - ₹50/10INVITES 
12.STATIC OVERLAY- ₹140/20 INVITES 
13. LINEUP PFPS (PACKS OF 8)- ₹200/20 INVITES 

VFX: 
1. INTRO/OUTRO- ₹150/17 INVITES 
2. ANIMATED OVERLAY- ₹200/25 INVITES 
3. ANIMATED LOGO - ₹150/17 INVITES 
4. MONTAGE EDITING (60SECS) - ₹200

NOTICE: PRICES OF THIS LIST  MAY VARY ACCORDING TO YOUR ORDER""", inline = False)
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

# @Graphics Code#3542 jsk py 
# male= discord.utils.get(_ctx.guild.roles, id=908960944959406110)
# female= discord.utils.get(_ctx.guild.roles, id=908961036068081685)
# giveaway= discord.utils.get(_ctx.guild.roles, id=909033901253603368)
# partnership= discord.utils.get(_ctx.guild.roles, id=909033666288685096)
# chat= discord.utils.get(_ctx.guild.roles, id=909034139137753119)
# announcement= discord.utils.get(_ctx.guild.roles, id=909033759448367144)
# pc= discord.utils.get(_ctx.guild.roles, id=914773730671099914)
# picsart= discord.utils.get(_ctx.guild.roles, id=916250174060380200)
# IBS= discord.utils.get(_ctx.guild.roles, id=916250106494332949)

# embed=discord.Embed(title="SELF ROLES", description="React below to take respective roles", color=discord.Color(0x00f064))
# embed.add_field(name="Gender", value=f"{male.mention}\n {female.mention}", inline=False)
# embed.add_field(name="Pings", value=f"{giveaway.mention}\n{partnership.mention}\n{chat.mention}\n{announcement.mention}", inline=False)
# embed.add_field(name="Editing App", value=f"{pc.mention}\n{picsart.mention}\n{IBS.mention}", inline=False)
# embed.timestamp=discord.utils.utcnow()
# embed.set_footer(icon_url=_ctx.guild.icon.url,text=f"{_ctx.guild.name} | {_ctx.guild.id}")
# embed.set_thumbnail(url=_ctx.guild.icon.url)
# embed.set_image(url="https://cdn.discordapp.com/attachments/909344866662744085/928953056824004618/unknown.png")
# return embed
       

# @Graphics Code#3542 jsk py
# async def on_message(message):
#   if message.channel.id != 905678036794486874:
#     return
#   embed=message.embeds[0]
#   embed.set_thumbnail(url=_ctx.guild.icon.url)
#   await message.edit(embed=embed)

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