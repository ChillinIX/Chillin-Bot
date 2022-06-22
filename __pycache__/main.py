from turtle import color
import discord
from discord.ext import commands
from Keys import *

intents=discord.Intents.default()
intents.members=True
client=commands.Bot(command_prefix='!',intents=intents)
channel = client.get_channel(987059865023287396)



@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
  await ctx.send("Hi")

@client.command()
async def Goodbot(ctx):
  await ctx.send("Thanks!")

@client.command()
async def split(ctx):
  split == discord.Embed(title="5v5 Randomiser", description="Good Luck!",color=0x03dffc)
  await ctx.send(embed=split)

client.run(Token)