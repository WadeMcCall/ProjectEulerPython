import math
from lib.primes import getNextPrimeGenerator
from lib.convenience import are_permutations, factors

def main():
    arr = findAllPhiUnderX(10 ** 7)
    min = 10 ** 7
    for num in range(2, 10 ** 7):
        ratio = num/arr[num - 2]
        if ratio < min:
            if are_permutations(str(num), str(arr[num - 2])):
                print(num)
                min = ratio

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

if __name__ == "__main__":
    main()



"""
leaving below functions here for posterity, not used in solution
"""
# sieve approach
def phi2(x):
    coprimesArr = [True for _ in range(0, x)]
    facts = [*set(factors(x))]
    facts.sort()
    for p in facts:
        if p == 1:
            continue
        for i in range(0, x, p):
            coprimesArr[i] = False
    return len([i for i in coprimesArr if i is True])

def phi(x):
    return len([i for i in range(2,x) if math.gcd(i, x) == 1])