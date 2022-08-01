import discord
from discord.ext import commands

class greetings(commands.Cog):
  def __init__(self,client):
    self.client = client

  # !hello - connectivity testing
  @commands.command()
  async def hello(self,ctx):
    await ctx.send(f"Sup {ctx.author.name}")

  # !goodbot - bot commends
  @commands.command()
  async def goodbot(self,ctx):
    try:
      f = open('cogs\DB\counter.txt','r')
      love = int(f.readline())
    except:
      f = open('cogs\DB\counter.txt','a')
      f.write(str(0))
    love += 1
    f = open('cogs\DB\counter.txt','w')
    f.write(str(love))
    return await ctx.send(f"Thanks {ctx.author.name}! :heart_eyes:")

  # !love - shows commends from goodbot
  @commands.command()
  async def love(self,ctx):
    l = open('cogs\DB\counter.txt','r')
    love = int(l.readline())
    await ctx.send(f"Love = {love}")

  # !amideveloper - test for checking discord ID in a command
  @commands.command()
  async def amideveloper(self,ctx):
    if ctx.author.id == 198622235236237312:
      return await ctx.send(f"Of course you are {ctx.author.name}... you wrote me")
    await ctx.send(f"no, heck off {ctx.author.name}")

def setup(client):
  client.add_cog(greetings(client))