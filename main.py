import random

class Dice():
    def __init__(self, numSides, color):
        self.numSides = numSides
    def printInfo(self):
        print("The number of sides is: %d!" % (self.numSides))
    def getSides(self):
        return self.numSides
    def rollDice(self):
        chosenSide = random.randint(1,self.numSides)
        return chosenSide



def printDiceSide(givenDice):
    if(givenDice.getSides() > 6):
        print("A little too big for now!")
        return None
    outcome = givenDice.rollDice()
    sideToPrint={
            1:'*',
            2:'*\n\n    *',
            3:'*\n  *\n    *',
            4:'*  *\n*  *',
            5:'*   *\n  *\n*   *',
            6:'*  *\n*  *\n*  *'
            }
    print(sideToPrint[outcome])


d1 = Dice(6, "Blue")
#d1.seedDice()
printDiceSide(d1)
printDiceSide(d1)
printDiceSide(d1)
