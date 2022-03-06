import random


def roll(sides, rolls):
    result = ""
    total = 0
    for x in range(rolls):
        roll = random.randrange(1, sides+1)
        result = result + "(" + str(roll) + ") "
        total = total + roll
    result = result + " - Total: " + str(total)

    return result
