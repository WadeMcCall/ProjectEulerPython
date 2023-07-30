from lib.primes import Primes
from lib.convenience import have_common_elements

primes = Primes(10000)

def prime_factors(n):
    factors = []
    for primeNums in primes.primes:
        if primeNums*primeNums > n:  # If prime is greater than sqrt(n), break the loop
            break
        while (n % primeNums == 0):
            if primeNums not in factors:  # Only append prime to factors if it's not already there
                factors.append(primeNums)
            n //= primeNums
    if n > 1 and n not in factors:
        factors.append(n)
    return factors

def main():
    n = 1
    numFactors = 4
    for n in range(1000000):
        nFactors = prime_factors(n)
        n1Factors = prime_factors(n+1)
        n2Factors = prime_factors(n+2)
        n3Factors = prime_factors(n+3)
        if(nFactors.__len__() != numFactors or n1Factors.__len__() != numFactors or n2Factors.__len__() != numFactors or n3Factors.__len__() != numFactors):
            continue
        print(nFactors)
        if(not have_common_elements(nFactors, n1Factors)):
            print(n)
            return

        

if __name__ == "__main__":
    main()
