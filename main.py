import discord
from discord.ext import commands
import os
from Keys import *

intents=discord.Intents.default()
intents.members=True
client=commands.Bot(command_prefix='!',intents=intents)
channel = client.get_channel(987059865023287396)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

inital_extensions = []

for filename in os.listdir('Chillin-Bot\cogs'):
  if filename.endswith('.py'):
    inital_extensions.append("cogs." +filename[:-3])

if __name__=='__main__':
  for extensions in inital_extensions:
    client.load_extension(extensions)


client.run(Token)