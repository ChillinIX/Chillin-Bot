import discord
import os
import random
import requests
import opendota
from discord.ext import commands

client=opendota.OpenDota()
playerResult=requests.get("https://api.opendota.com/api/heroes/1/matchups")
resultData = playerResult.json()

print(resultData)

class WinnersnLosers(commands.Cog):
    def __init__(self,client):
        self.client = client

def setup(client):
  client.add_cog(WinnersnLosers(client))
  
'''
if games played >= 10 :
    add to playedCharacters
    top5 = List[:5]
    bottom5 = List[5:]

!winners
Displays your top 5 characters for this patch along with your mathes played and win rate 

!losers
Displays your bottom 5 characters for this patch along with your matches played and loss rate

** MUST HAVE 10 MATCHES PLAYED TO COUNT **
removes the 0% win rates becasue you played a character once or 100% winrates for 

playerlist = [10, 55, 230, 2, 15, 200, 404, 300, 1532, 155, 1, 5, 3]
print (playerlist[:5])
print (playerlist[-5:])
'''