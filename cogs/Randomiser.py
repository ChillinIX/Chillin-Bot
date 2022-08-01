import discord
from discord.ext import commands
import random
import numpy

class randomiser(commands.Cog):
    def __init__(self,client):
        self.client = client

    # !inhouse - 10 people randomised onto even teams of radiant and dire
    @commands.command()
    async def inhouse(self,ctx):
        inhouse = discord.Embed(title="5v5 Randomiser",color=0x03dffc)
        inhouse.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        inhouse.set_thumbnail(url="https://i.imgur.com/U2N9l0E.jpg")
        players = ["Anthony","Shanise","Connor","Colin","Harry","Tim","Shaun","Ivan","Tristan","Casey"]
        random.shuffle(players)
        splitting = numpy.array_split(players,2)
        inhouse.add_field(name="Radiant",value=' \n'.join(splitting[0]), inline = True)
        inhouse.add_field(name="Dire",value=' \n'.join(splitting[1]), inline = True)
        await ctx.send(embed=inhouse)

    # !giveteam - random 5 people in random positions with random characters
    @commands.command()
    async def giveteam(self,ctx):
    
        # Random team name - Adjective
        filename1=open('cogs/DB/f1.txt','r')
        wordList1=[line.rstrip('\n') for line in filename1]
        filename1.close()
        out1 = random.choice(wordList1)
    
        # Random team name - Animal
        filename2=open('cogs/DB/f2.txt','r')
        wordList2=[line.rstrip('\n') for line in filename2]
        filename2.close()
        out2 = random.choice(wordList2)

        # players and positions variables
        position = ['1', '2', '3', '4', '5']
        player = ['Colin','Nise','Connor','Harry','Tim']
        random.shuffle(player)

        # 5 hero lists, 1 for each position
        # print hero in same format for positions
        # Players are randomised into the positions

        # Build for the discord frame
        randomteam = discord.Embed(title=f"The {out1} {out2}'s",color=0x03dffc)
        randomteam.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        randomteam.set_thumbnail(url="https://i.imgur.com/U2N9l0E.jpg")
        randomteam.add_field(name="Position",value=' \n'.join(position), inline = True)
        randomteam.add_field(name="Player",value=' \n'.join(player), inline = True)
        await ctx.send(embed=randomteam)

def setup(client):
  client.add_cog(randomiser(client))