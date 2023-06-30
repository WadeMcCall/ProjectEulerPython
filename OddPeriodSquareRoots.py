# credit where it's due https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root
import math
from decimal import *

class ContinuedSqrtFraction:
    def __init__(self, numToSqrt):
        self.sqrt = numToSqrt
        self.integerPart = math.floor(math.sqrt(numToSqrt))
        self.calculatePeriodicPart()
    
    def getPeriodOfSquareRoot(self):
        return len(self.periodicPart)
    
    def _reduceTerms(self, sqrtPortion, constantPortion, denominator):
        gcd = math.gcd(sqrtPortion, denominator, constantPortion)
        return sqrtPortion // gcd, constantPortion // gcd, denominator // gcd

    def calculatePeriodicPart(self):
        n = self.sqrt
        a = math.floor(math.sqrt(n))

        firstRemainder = math.sqrt(n) - a
        remainder = firstRemainder
        integerList = []
        sqrtPortion = 1
        constantPortion = -a
        denominator = 1
        while True:
            prevConstantPortion = constantPortion
            constantPortion =  denominator * constantPortion * -1
            sqrtPortion = sqrtPortion * denominator
            denominator = self.sqrt - prevConstantPortion ** 2
            sqrtPortion, constantPortion, denominator = self._reduceTerms(sqrtPortion, constantPortion, denominator)
            evaluation = (sqrtPortion * (math.sqrt(n)) + constantPortion) / denominator
            a = math.floor(evaluation)
            integerList.append(a)
            remainder = evaluation - a
            if math.isclose(remainder, firstRemainder, rel_tol=.0001):
                break
            constantPortion = constantPortion - a * denominator
        self.periodicPart = integerList

def main():
    numOddPeriods = 0
    for i in range(1, 10001):
        if math.sqrt(i) % 1 == 0:
            continue
        cf = ContinuedSqrtFraction(i)
        if cf.getPeriodOfSquareRoot() % 2 == 1:
            numOddPeriods += 1
    print(numOddPeriods)

if __name__ == "__main__":
    main()