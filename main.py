import discord
import os
import random
from replit import db

client=discord.Client()
my_secret = os.environ['TOKEN']

def update_players(player_add):
  if "player" in db.keys():
    player = db["player"]
    player.append(player_add)
    db["player"] = player
  else:
    db["player"] = [player_add]
    
def remove_player(index):
  player = db["player"]
  if len(player) > index:
    del player[index]
    db["player"] = player

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return

  if message.content.startswith('Good bot'):
    await message.channel.send('Thanks, Colin!')
'''
  options = ('playerNames.txt')
  if "player" in db.keys():
    options=options+db["player"]

  if message.content.startswith("!add"):
    player_add = message.split("!add ",1) [1]
    update_players(player_add)
    await message.channel.send("Player Added.")

  if message.content.startswith("!remove"):
    player = []
    if 'player' in db.keys():
      index = int(message.split('!remove',1)[1])
      delete_player(index)
      player = db["player"]
    await message.channel.send(player)
    
 # pN = ('playerNames.txt')
 # with open(pN) as a1:
 #   pLst = [line.rstrip('\n') for line in a1]
 # a1.close()
  #random.shuffle(pLst)
 # radiant, dire = pLst[:5], pLst[5:]
  
 # if message.content.startswith('!split',*args,**kwargs):
  #  await message.channel.send("Radiant:\n",radiant)
  #  await message.channel.send("Dire:\n",dire)
'''

client.run(my_secret)