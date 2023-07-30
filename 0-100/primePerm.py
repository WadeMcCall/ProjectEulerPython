from lib.primes import Primes
from lib.convenience import are_permutations
import itertools

primes = Primes(10000)

def permute_digits(n):
    # Convert the integer into a list of its digits
    digit_strs = list(str(n))
    
    # Generate all permutations of the digits
    permutations = set(itertools.permutations(digit_strs, len(digit_strs)))
    
    # Convert each permutation back into an integer, but only if it has the same
    # number of digits as the original number (i.e., it doesn't start with a '0')
    permutation_ints = [int(''.join(p)) for p in permutations if p[0] != '0']

    return permutation_ints

def findCommonDifference(primes):
    primes.sort()
    for i in range(0, primes.__len__()):
        for j in range(i+1, primes.__len__()):
            for k in range(j+1, primes.__len__()):
                if(primes[j] - primes[i] == primes[k] - primes[j]):
                    print(primes[i], primes[j], primes[k])
                    return primes[i], primes[j], primes[k]
    return None


def main():
    generator = primes.getNextPrimeGenerator(1000)
    for prime in generator:
        newPrimes = []
        if(str(prime).__len__() > 4):
            break
        perms = permute_digits(prime)
        numPrimes = 0
        for perm in perms:
            if(primes.isPrime(perm)):
                newPrimes.append(perm)
                numPrimes += 1
        if(numPrimes >= 3):
            findCommonDifference(newPrimes)
            continue



if __name__ == "__main__":
    main()