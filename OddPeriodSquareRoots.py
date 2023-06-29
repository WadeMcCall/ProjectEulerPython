# credit where it's due https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root
import math
from decimal import *

class ContinuedFraction:
    def __init__(self, numToSqrt):
        self.sqrt = numToSqrt
        self.integerPart = math.floor(math.sqrt(numToSqrt))
        self.periodPart = self._calculatePeriodPart(numToSqrt)

    def _calculatePeriodPart(self, numToSqrt):
        a = self.integerPart
        remainder = math.sqrt(numToSqrt) - a

        return self._calculatePeriodPartHelper(remainder, [])
    
    def _calculatePeriodPartHelper(self, remainder, integerList):
        firstRemainder = remainder
        while True:
            newNum = 1 /remainder
            newA = math.floor(newNum)
            integerList.append(newA)
            if math.isclose(firstRemainder, newNum - newA, rel_tol=.0001):
                return integerList
            remainder = newNum - newA
    
    def getPeriodOfSquareRoot(self):
        return len(self.periodPart)
    

"""  ____         n - a ^ 2
-\  /     =  a + -----------
  \/  n            a + sqrt(n)
"""

def calculatePeriodOfSqrt(numSqrt):
    n = numSqrt
    a = math.floor(math.sqrt(n))

    firstRemainder = math.sqrt(n) - a
    remainder = firstRemainder
    integerList = [a]
    sqrtPortion = 1
    constantPortion = -a
    while True:
        constantPortion = -1 * constantPortion
        denominator = numSqrt - constantPortion ** 2
        a = math.floor((sqrtPortion * (math.sqrt(n) + constantPortion)) / denominator)
        integerList.append(a)



def main():
    numOddPeriods = 0
    for i in range(1, 14):
        if math.sqrt(i) % 1 == 0:
            continue
        length, period = calculatePeriodOfSqrt(i)
        if(length > 30):
            print(i)
        if length % 2 == 1:
            numOddPeriods += 1
    print(numOddPeriods)
    # cf = ContinuedFraction(94)
    # print(cf.periodPart)
    # print(cf.getPeriodOfSquareRoot())

if __name__ == "__main__":
    main()