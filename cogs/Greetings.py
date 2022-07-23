import discord
from discord.ext import commands
love = 0

class Greetings(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def hello(self,ctx):
    await ctx.send(f"Sup {ctx.author.name}")

  @commands.command()
  async def goodbot(self,ctx):
    await ctx.send(f"Thanks {ctx.author.name}! [+1]")

  @commands.command()
  async def love(self,ctx):
    
    await ctx.send(f"love count: {love}")

def setup(client):
  client.add_cog(Greetings(client))