from lib.primes import Primes, isPrime
from itertools import permutations, combinations
import time

def generate_pairs(numbers):
    str_numbers = [str(num) for num in numbers]  # Convert the numbers into strings.
    pairs = list(permutations(str_numbers, 2))  # Generate all possible pairs of numbers.
    concatenated_pairs = [int(x + y) for x, y in pairs]  # Concatenate each pair of numbers.
    return concatenated_pairs

def isPrimePairSet(set):
    for pair in set:
        if not isPrime(pair):
            return False
    return True

def generate_new_pairs(list, newPrime):
    return [[num, newPrime] for num in list]

def append_to_lists(array_2d, new_num):
    return [lst + [new_num] for lst in array_2d]    

def __main():
    primes = Primes(10)
    gen = primes.getNextPrimeGenerator()
    list = []
    numPairs = 0
    pairsThatWork = []
    numTrips = 0
    triplesThatWork = []
    numQuads = 0
    quadsThatWork = []
    pentsThatWork = []
    numPrimePairs = 5
    for prime in gen:
        if prime == 2 or prime == 5:
            continue
        if len(list) >= 1:
            # pents
            if len(quadsThatWork) > 0:
                pents = append_to_lists(quadsThatWork, prime)
                for pent in pents:
                    pentsToTest = generate_pairs(pent)
                    if not isPrimePairSet(pentsToTest):
                        continue
                    pentsThatWork.append(pent)
                if len(pentsThatWork) >= 1 and numPrimePairs == 5:
                    print(pentsThatWork)
                    return
            # quads
            if len(triplesThatWork) > 0:
                quads = append_to_lists(triplesThatWork, prime)
                for quad in quads:
                    quadsToTest = generate_pairs(quad)
                    if not isPrimePairSet(quadsToTest):
                        continue
                    quadsThatWork.append(quad)
                # if len(quadsThatWork) > numQuads:
                #     numQuads = len(quadsThatWork)
                #     print(quadsThatWork)
                if len(quadsThatWork) >= 1 and numPrimePairs == 4:
                    print(quadsThatWork)
                    return
            # trips
            if len(pairsThatWork) > 0:
                trips = append_to_lists(pairsThatWork, prime)
                for trip in trips:
                    tripsToTest = generate_pairs(trip)
                    if not isPrimePairSet(tripsToTest):
                        continue
                    triplesThatWork.append(trip)
                # if len(triplesThatWork) > numTrips:
                #     numTrips = len(triplesThatWork)
                #     print(triplesThatWork)
                if len(triplesThatWork) >= 1 and numPrimePairs == 3:
                    print(triplesThatWork)
                    return
            # pairs
            newPairs = generate_new_pairs(list, prime)
            for pair in newPairs:
                pairsToTest = generate_pairs(pair)
                if not isPrimePairSet(pairsToTest):
                    continue
                pairsThatWork.append(pair)
            # if len(pairsThatWork) > numPairs:
            #     numPairs = len(pairsThatWork)
            #     print(pairsThatWork)
            if len(pairsThatWork) >= 1 and numPrimePairs == 2:
                print(pairsThatWork)
                return
        
        list.append(prime)

    return


if __name__ == "__main__":
    __main()