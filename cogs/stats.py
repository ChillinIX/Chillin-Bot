import discord
from discord.ext import commands

class patchplayed(commands.Cog):
    def __init__(self,client):
        self.client = client

    # !patchplayed - shows the top 5 and bottom 5 performing heroes played this patch for the user
    @commands.command()
    async def patchplayed(self,ctx):
        dota = True

#if games played >= 10 :
#    add to playedCharacters
#    top5 = List[:5]
#    bottom5 = List[5:]

#** MUST HAVE 10 MATCHES PLAYED TO COUNT **
#removes the 0% win rates becasue you played a character once or 100% winrates for 


def setup(client):
    client.add_cog(patchplayed(client))