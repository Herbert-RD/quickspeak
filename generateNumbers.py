from random import randrange

def generateNumbers():
    randomNumbers = [0, 0]
    x = 0
    while(x != 2):
        randomNumbers[x] = randrange(0, 1000)
        randomNumbers[x] = str(randomNumbers[x])
        x += 1


    stringRandomNumbers = " ".join(randomNumbers)
    return stringRandomNumbers

print(generateNumbers())