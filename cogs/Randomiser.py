import discord
from discord.ext import commands
import random
import numpy

class randomiser(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def inhouse(self,ctx):
        inhouse = discord.Embed(title="5v5 Randomiser",color=0x03dffc)
        inhouse.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        inhouse.set_thumbnail(url="https://i.imgur.com/U2N9l0E.jpg")
        players = ["Anthony","Shanise","Connor","Colin","Harry","Tim","Shaun","Ivan","Tristan","Casey"]
        random.shuffle(players)
        splitting = numpy.array_split(players,2)
        inhouse.add_field(name="Radiant",value=' \n'.join(splitting[0]), inline = True)
        inhouse.add_field(name="Dire",value=' \n'.join(splitting[1]), inline = True)
        await ctx.send(embed=inhouse)

    @commands.command()
    async def random(self, ctx):
        randomd = discord.Embed(title="Random Team",color=0x03dffc)
        randomd.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        randomd.set_thumbnail(url="https://i.imgur.com/U2N9l0E.jpg")
        player='Colin'
        playerHero=" - "+"Axe"
        grouping = player + playerHero

        randomd.add_field(name="Team Test!", value=' \n'.join(grouping), inline=True)
        await ctx.send(embed=randomd)

def setup(client):
  client.add_cog(randomiser(client))