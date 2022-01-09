import random


def generateText(filename, amountOfBytes):
    with open(filename, "w") as file:
        for b in range(amountOfBytes):
            file.write(chr(random.randrange(65, 90)))
