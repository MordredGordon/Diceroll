import random
tentativas = 1


def rolar(max):
    result = ""
    total = 0
    for x in range(tentativas):
        rodada = random.randrange(1, max+1)
        result = result + "(" + str(rodada) + ") "
        total = total + rodada
    result = result + " - Total: " + str(total)

    return result
