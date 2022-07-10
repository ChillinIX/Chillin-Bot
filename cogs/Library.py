import discord
import os
import requests
import opendota
from discord.ext import commands

client=opendota.OpenDota()
openURL='https://api.opendota.com/api/'
playersURL = 'players/'
timID='99084628'
shaunID='145692671'
ivanID='51625083'
harryID='83942876'
anthonyID='282780720'
niseID='337288948'
caseyID='69558459'
colinID='44067861'
connorID='39958451'

playerTim=requests.get(openURL+playersURL+timID)
timData=playerTim.json()
playerShaun=requests.get(openURL+playersURL+shaunID)
shaunData=playerShaun.json()
playerIvan=requests.get(openURL+playersURL+ivanID)
ivanData=playerIvan.json()
playerHarry=requests.get(openURL+playersURL+harryID)
harryData=playerHarry.json()
playerAnthony=requests.get(openURL+playersURL+anthonyID)
anthonyData=playerAnthony.json()
playerNise=requests.get(openURL+playersURL+niseID)
niseData=playerNise.json()
playerCasey=requests.get(openURL+playersURL+caseyID)
caseyData=playerCasey.json()
playerColin=requests.get(openURL+playersURL+colinID)
colinData=playerColin.json()
playerConnor=requests.get(openURL+playersURL+connorID)
connorData=playerConnor.json()

class Library(commands.Cog):
    def __init__(self,client):
        self.client = client

        


def setup(client):
  client.add_cog(Library(client))