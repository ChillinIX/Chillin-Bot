import discord
from discord.ext import commands

class Greetings(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def hello(self,ctx):
    await ctx.send("Hi")

  @commands.command()
  async def goodbot(self,ctx):
    await ctx.send("Thanks")

def setup(client):
  client.add_cog(Greetings(client))