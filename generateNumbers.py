from random import randrange

def generateNumbers():
    randomNumbers = [0, 0, 0]
    x = 0
    while(x != 3):
        randomNumbers[x] = randrange(0, 1000)
        randomNumbers[x] = str(randomNumbers[x])
        x += 1

    return randomNumbers