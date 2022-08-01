import discord
from discord.ext import commands
import random

class characterRandom(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def giveteam(self,ctx):
    
    filename1=open('cogs/DB/f1.txt','r')
    wordList1=[line.rstrip('\n') for line in filename1]
    filename1.close()
    out1 = random.choice(wordList1)
    
    filename2=open('cogs/DB/f2.txt','r')
    wordList2=[line.rstrip('\n') for line in filename2]
    filename2.close()
    out2 = random.choice(wordList2)

    players = ["Shanise","Connor","Colin","Harry","Tim"]
    pos = ["Pos1","Pos2","Pos3","Pos4","Pos5"]
    random.shuffle(players)

    for r in players:
      print(pos,players)
    
    return await ctx.send(f"Team Name: {out1} {out2}")

# random player, random character

#Tim - Axe
#Shanise - Underlord
#Colin - Puck
#Shaun - Phantom Assassin
#Casey - Witch Doctor

def setup(client):
  client.add_cog(characterRandom(client))