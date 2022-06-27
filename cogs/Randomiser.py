import discord
from discord.ext import commands
import os
import random
import numpy

players = ["Anthony","Shanise","Connor","Colin","Harry","Tim","Shaun","Ivan","Tristan","Ben"]
random.shuffle(players)
splitting = numpy.array_split(players,2)

class Randomiser(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def split(self,ctx):
        split = discord.Embed(title="5v5 Randomiser",color=0x03dffc)
        split.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        split.set_thumbnail(url="https://i.imgur.com/U2N9l0E.jpg")
        split.add_field(name="Radiant",value=' '.join(splitting[0]), inline = True)
        split.add_field(name="Dire",value=' '.join(splitting[1]), inline = True)
        await ctx.send(embed=split)

def setup(client):
  client.add_cog(Randomiser(client))