import discord
import random
from discord.ext import commands

class characterRandom(commands.Cog):
  def __init__(self,client):
    self.client = client


  @commands.command()
  async def giveteam(self,ctx):
    
    # Declare Variables
    filename1 = open('cogs\DB\f1.txt','r')
    filename2 = open('cogs\DB\f2.txt','r')

    # Open each .txt file using a loop into a list(s) named wordList#. Strip the new lines from each word.
    with open(filename1) as f1:
      wordList1 = [line.rstrip('\n') for line in f1]

    with open(filename2) as f2:
      wordList2 = [line.rstrip('\n') for line in f2]
    
    # Close the .txt files.
    f1.close()
    f2.close()
    
    # Randomly select a index value in each list using the choice module within Random.
    # Concatenate the string using a simple print statement. 
    print(random.choice(wordList1) + "_" + random.choice(wordList2))



# random player, random character

#tie them together like the animal adjective program
#name the teamlike so:

#Team Awkward Aardvark!

#Tim - Axe
#Shanise - Underlord
#Colin - Puck
#Shaun - Phantom Assassin
#Casey - Witch Doctor

def setup(client):
  client.add_cog(characterRandom(client))