import discord
import numpy
import random
from discord.ext import commands
from Keys import *

intents=discord.Intents.default()
intents.members=True
client=commands.Bot(command_prefix='!',intents=intents)
channel = client.get_channel(987059865023287396)

players = ["Anthony","Shanise","Connor","Colin","Harry","Tim","Shaun","Ivan","Tristan","Ben"]
random.shuffle(players)
splitting = numpy.array_split(players,2)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
  await ctx.send("Hi",ctx.author.display_name)

@client.command()
async def goodbot(ctx):
  await ctx.send("Thanks, ",ctx.author.display_name)

@client.command()
async def split(ctx):
  split = discord.Embed(title="5v5 Randomiser",color=0x03dffc)
  split.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
  split.set_thumbnail(url="https://i.imgur.com/U2N9l0E.jpg")
  split.add_field(name="Radiant",value=splitting[0], inline = True)
  split.add_field(name="Dire",value=splitting[1], inline = True)
  await ctx.send(embed=split)

client.run(Token)