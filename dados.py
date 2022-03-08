import random


def roll(sides, rolls):
    rollResult = {}
    results = []
    total = 0
    for x in range(rolls):
        roll = random.randrange(1, sides+1)
        results.append("("+str(roll)+")")
        total = total + roll
    rollResult["results"] = results
    rollResult["total"] = total
    return rollResult
