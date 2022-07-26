import discord
from discord.ext import commands
import os

class characterRandom(commands.Cog):
    def __init__(self,client):
        self.client = client

"""
random player, random character

tie them together like the animal adjective program
name the teamlike so:

Team Awkward Aardvark!

Tim - Axe
Shanise - Underlord
Colin - Puck
Shaun - Phantom Assassin
Casey - Witch Doctor

"""

def setup(client):
  client.add_cog(characterRandom(client))