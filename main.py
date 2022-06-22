import discord
from discord.ext import commands
from Keys import *

client=commands.Bot(command_prefix='!')

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.command()
async def hello(ctx):
  await ctx.send("Hi")

client.run(Token)