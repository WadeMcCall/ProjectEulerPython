from lib.TotientFunctions import findAllPhiUnderX, phi
from lib.primes import getNextPrimeGenerator, getPrimeArray
from lib.Fraction import Fraction

primes = getPrimeArray(1000000)

def getPromorialNumGenerator():
    gen = getNextPrimeGenerator()
    n = 1
    while True:
        yield n
        n *= next(gen)

def evaluatePowers(arrAs):
    product = 1
    for i in range(len(arrAs)):
        product *= primes[i] ** arrAs[i]

    return product

def getNextArrAs(arrAs):
    # special cases
    if arrAs[0] == 1:
        return [2]
    if arrAs[0] == 2 and len(arrAs) == 1:
        return [2, 1]
    if arrAs[0] == 2 and arrAs[1] == 1:
        return [3, 1]
    if arrAs[0] == 3 and arrAs[1] == 1:
        return [2, 2]
    
    

def highlyCompositeNumberGenerator():
    arrAs = [1]
    while True:
        

def findResilience(d):
    return Fraction(phi(d),(d-1))

def main():
    GOAL = 15499/94744
    record = Fraction(1,1)
    d = 6469693230
    while True:
        Rd = findResilience(d)
        if(Rd < record):
            print(d, Rd)
            print (Rd < GOAL)
            record = Rd
        d += 2
    max = 0
    gen = getPromorialNumGenerator()
    print(findResilience(6469693230) < GOAL)
    return
    for n in gen:
        print(n)
    while True:
        print(d)
        if findResilience(d) < GOAL:
            print(d)
            break
        d += 2
    return

if __name__ == '__main__':
    main()