from nextcord.ext import commands
import nextcord
import aiohttp
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self, ctx: commands.Context):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.reddit.com/r/memes/hot.json') as resp:
                data = await resp.json()
                data = data['data']
                children = data['children']
                post = random.choice(children)['data']
                title = post['title']
                url = post['url_overridden_by_dest']

        embed =nextcord.Embed(title=title)
        embed.set_image(url=url)
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Fun(client))