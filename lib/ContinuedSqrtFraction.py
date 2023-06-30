import math
from itertools import cycle
from lib.Fraction import Fraction

class ContinuedSqrtFraction:
    def __init__(self, numToSqrt):
        self.sqrt = numToSqrt
        self.integerPart = math.floor(math.sqrt(numToSqrt))
        self.calculatePeriodicPart()
    
    def getPeriodOfSquareRoot(self):
        return len(self.periodicPart)
    
    def getAgenerator(self):
        yield self.integerPart
        periodic = cycle(self.periodicPart)
        for p in periodic:
            yield p

    def getFractionalConvergentGenerator(self):
        a = self.getAgenerator()
        a0 = next(a)
        oldFraction = Fraction(1, 0)
        currFraction = Fraction(a0, 1)
        yield currFraction
        a1 = next(a)
        while True:
            Pn = a1 * currFraction.numerator + oldFraction.numerator
            Qn = a1 * currFraction.denominator + oldFraction.denominator
            oldFraction = currFraction
            currFraction = Fraction(Pn, Qn)
            yield currFraction
            a1 = next(a)
    
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