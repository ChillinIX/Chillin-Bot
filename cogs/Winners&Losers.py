"""
imports, call player, call heroes, call matches for this patch for that player

variables establishing the calls

discern the players top 5

if games played > 10
    add to playedCharacters
    top5 = List[:5]
    bottom5 = List[5:]

!winners
Displays your top 5 characters for this patch along with your mathes played and win rate 

!losers
Displays your bottom 5 characters for this patch along with your matches played and loss rate



** MUST HAVE 10 MATCHES PLAYED TO COUNT **
removes the 0% win rates becasue you played a character once or 100% winrates for 

"""
from Keys import *

opendotaToken

Playerlist = [10, 55, 230, 2, 15, 200, 404, 300, 1532, 155, 1, 5, 3]

print (Playerlist[:5])
print (Playerlist[-5:])
