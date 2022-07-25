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
    if ctx.send == "Thanks":
      try:
        f = open('counter.txt','r')
        love = int(f.readline())
      except:
        f = open('counter.txt','a')
        f.write(str(0))
      
      love += 1
      f = open('counter.txt','w')
      f.write(str(love))

      await message.channel.send('Test!' + str(love))

  @commands.command()
  async def love(self,ctx):
    await ctx.send(f"love count: {love}")

def setup(client):
  client.add_cog(Greetings(client))