players = ["Jordan", "Luke", "Wiola", "Liam", "Andu", "Dan", "Joe", "Eugene"]

from random import sample
from itertools import combinations

goodTeams = False
badCombos = combinations(["Jordan", "Luke", "Joe"],2)

while not goodTeams:
    teams = []
    remainder = players
    for _ in range( len(players)>>1 ):
        teams += [sample(remainder, 2)]
        for p in teams[-1]:
            remainder.remove(p)

    goodTeams = not any( [t in badCombos for t in teams] )

print(teams)
    

