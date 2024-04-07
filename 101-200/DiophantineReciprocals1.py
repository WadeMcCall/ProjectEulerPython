from lib.Fraction import Fraction
from lib.primes import getNextPrimeGenerator
from lib.TotientFunctions import findAllPhiUnderX
from lib.convenience import countDivisors

primorials = []

def getPrimorialGenerator():
    gen = getNextPrimeGenerator()
    n = 1
    while True:
        yield n
        n *= next(gen)

def CountSolutions(n):
    x = 2 * n
    sum = 0
    while x > n:
        if isSolution(x, n):
            sum += 1
        x -= 1
    return sum

def isSolution(x, n):
    sol = Fraction(1, n)
    xFrac = Fraction(1, x)
    yFrac = sol - xFrac
    yFrac.reduce()
    if yFrac.numerator == 1:
        return True
    return False

def main():
    max = 0
    for n in getPrimorialGenerator():
        primorials.append(n)
        sols = CountSolutions(n)
        if sols > max:
            max = sols
            print(n, max)
        if max > 1000:
            print(n, max)
            break
        n += 6
    n = primorials[-1]
    newBest = -1
    while n > primorials[-2]:
        n -= primorials[-3]
        sols = CountSolutions(n)
        if 1000 < sols < max:
            newBest = n
            max = sols
            print(n, max)
    print(newBest, max)

def test():
    i = 362880
    print(countDivisors(i), CountSolutions(i))

if __name__ == '__main__':
    test()