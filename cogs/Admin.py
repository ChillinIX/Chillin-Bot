import discord
from discord.ext import commands

class admin(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def amideveloper(self,ctx):
    if ctx.author.id == 198622235236237312:
      return await ctx.send(f"Of course you are {ctx.author.name}... you wrote me")
    await ctx.send(f"no, heck off {ctx.author.name}")

def setup(client):
  client.add_cog(admin(client))