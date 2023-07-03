from lib.primes import getNextPrimeGenerator
from lib.convenience import factors
import math

# generalized sieve approach
def findAllPhiUnderX(x):
    arr = [i for i in range(2, x)]
    gen = getNextPrimeGenerator()
    for prime in gen:
        if prime > x:
            break
        for i in range(prime, x, prime):
            arr[i - 2] = int(arr[i - 2] * (1 - 1/prime))
    return arr


# sieve approach
def phi(x):
    coprimesArr = [True for _ in range(0, x)]
    facts = [*set(factors(x))]
    facts.sort()
    for p in facts:
        if p == 1:
            continue
        for i in range(0, x, p):
            coprimesArr[i] = False
    return len([i for i in coprimesArr if i is True])

def is_coprime(x, y):
    return math.gcd(x, y) == 1

# def phi(x):
#     return len([i for i in range(2,x) if math.gcd(i, x) == 1])