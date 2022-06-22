import random

pN = ('Chillin-Bot\playerNames.txt')

with open(pN) as a1:
    pLst = [line.rstrip('\n') for line in a1]
a1.close()

random.shuffle(pLst)
radiant, dire = pLst[:5], pLst[5:]
'''
print("---------\n Radiant\n---------",*radiant, sep = "\n• ")
print('\n')
print("---------\n  Dire\n---------",*dire, sep = "\n• ")
'''