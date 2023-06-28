from lib.FigurateNumbers import SquareNumberGen, triangleNumberGen, pentagonalNumberGen, hexagonalNumberGen, heptagonalNumberGen, octagonalNumberGen
import time

squareNumbers = {}
triangleNumbers = {}
pentagonalNumbers = {}
hexagonalNumbers = {}
heptagonalNumbers = {}
octagonalNumbers = {}

class FigurateNumber:

    def __init__(self, _type, _value):
        self.type = _type
        self.value = _value
        self.leadingValue = int(str(_value)[:2])
        self.trailingValue = int(str(_value)[-2:])
        self.squareChains = []
        self.triangleChains = []
        self.pentagonChains = []
        self.hexagonChains = []
        self.heptagonChains = []
        self.octagonChains = []

    def findChains(self):
        if self.type != "square":
            self._findChainsOfType("square")
        if self.type != "triangle":
            self._findChainsOfType("triangle")
        if self.type != "pentagonal":
            self._findChainsOfType("pentagonal")
        if self.type != "hexagonal":
            self._findChainsOfType("hexagonal")
        if self.type != "heptagonal":
            self._findChainsOfType("heptagonal")
        if self.type != "octagonal":
            self._findChainsOfType("octagonal")
    
    def _findChainsOfType(self, type):        
        global squareNumbers
        global triangleNumbers
        global pentagonalNumbers
        global hexagonalNumbers
        global heptagonalNumbers
        global octagonalNumbers

        if type == "square":
            arr = squareNumbers
            chainArr = self.squareChains
        if type == "triangle":
            arr = triangleNumbers
            chainArr = self.triangleChains
        if type == "pentagonal":
            arr = pentagonalNumbers
            chainArr = self.pentagonChains
        if type == "hexagonal":
            arr = hexagonalNumbers
            chainArr = self.hexagonChains
        if type == "heptagonal":
            arr = heptagonalNumbers
            chainArr = self.heptagonChains
        if type == "octagonal":
            arr = octagonalNumbers
            chainArr = self.octagonChains
        for val in arr:
            if val.leadingValue == self.trailingValue:
                chainArr.append(val)
    
    def __str__(self):
        return(str(self.value))
    
    def __repr__(self):
        return self.__str__()
    
    def __add__(self, other):
        if type(other) == int:
            return self.value + other
        return self.value + other.value


def generateAll4DigitSquares():
    generator = SquareNumberGen()
    return generateAll4DigitNumsFromGenerator(generator, "square")

def generateAll4DigitTriangles():
    generator = triangleNumberGen()
    return generateAll4DigitNumsFromGenerator(generator, "triangle")

def generateAll4DigitPentagons():
    generator = pentagonalNumberGen()
    return generateAll4DigitNumsFromGenerator(generator, "pentagonal")

def generateAll4DigitHexagons():
    generator = hexagonalNumberGen()
    return generateAll4DigitNumsFromGenerator(generator, "hexagonal")

def generateAll4DigitHeptagons():
    generator = heptagonalNumberGen()
    return generateAll4DigitNumsFromGenerator(generator, "heptagonal")

def generateAll4DigitOctogons():
    generator = octagonalNumberGen()
    return generateAll4DigitNumsFromGenerator(generator, "octagonal")

def generateAll4DigitNumsFromGenerator(generator, type):
    numbers = []
    for i in generator:
        if i < 1000:
            continue
        if i >= 10000:
            break
        numbers.append(FigurateNumber(type, int(i)))
    
    return numbers

def dfsHelper(val, depth, chain):
    chainTypes = []
    for val in chain:
        chainTypes.append(val.type)
    if depth == 6:
        if val.trailingValue == chain[0].leadingValue:
            print(chain)
            sum = 0
            for num in chain:
                sum += num.value
            print(sum)
            return
        else:
            return
    for chainType in [val.squareChains, val.triangleChains, val.pentagonChains, val.hexagonChains, val.heptagonChains, val.octagonChains]:
        for chainVal in chainType:
            if chainVal.type in chainTypes: # don't backtrack to the same type
                continue
            dfsHelper(chainVal, depth + 1, chain + [chainVal])
            continue

def dfs():
    for val in squareNumbers:
        dfsHelper(val, 1, [val])

def main():
    global squareNumbers
    global triangleNumbers
    global pentagonalNumbers
    global hexagonalNumbers
    global heptagonalNumbers
    global octagonalNumbers

    squareNumbers = generateAll4DigitSquares()
    triangleNumbers = generateAll4DigitTriangles()
    pentagonalNumbers = generateAll4DigitPentagons()
    hexagonalNumbers = generateAll4DigitHexagons()
    heptagonalNumbers = generateAll4DigitHeptagons()
    octagonalNumbers = generateAll4DigitOctogons()

    for val in squareNumbers:
        val.findChains()
    for val in triangleNumbers:
        val.findChains()
    for val in pentagonalNumbers:
        val.findChains()
    for val in hexagonalNumbers:
        val.findChains()
    for val in heptagonalNumbers:
        val.findChains()
    for val in octagonalNumbers:
        val.findChains()
        
    dfs()

    return

if __name__ == "__main__":
    main()