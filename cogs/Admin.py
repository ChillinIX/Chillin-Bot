import discord
from discord.ext import commands
import os

class Admin(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    #Commands
    #additions
def setup(client):
  client.add_cog(Admin(client))