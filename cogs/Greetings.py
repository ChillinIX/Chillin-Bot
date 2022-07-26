import discord
from discord.ext import commands

class greetings(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def hello(self,ctx):
    await ctx.send(f"Sup {ctx.author.name}")

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

  @commands.command()
  async def love(self,ctx):
    l = open('cogs\DB\counter.txt','r')
    love = int(l.readline())
    await ctx.send(f"Love = {love}")

def setup(client):
  client.add_cog(greetings(client))