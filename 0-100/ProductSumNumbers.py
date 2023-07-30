from lib.convenience import factors
from lib.primes import isPrime
import copy

factorsList = {1: [[1]], 2: [[2]], 3: [[3]], 4:[[4], [2,2]]}

def product(nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod

def generate_all_factor_combinations(n):
    global factorsList
    if(isPrime(n)):
        factorsList[n] =[[n]]
    if n in factorsList:
        return factorsList[n]
    factorsList[n] = []
    facts = factors(n)
    facts = [fact for fact in facts if fact < n/2]
    facts.remove(1)
    for fact in facts:
        x = n // fact
        factorsList[n].append([fact, x])
        xFacts = copy.deepcopy(generate_all_factor_combinations(x))
        for xFact in xFacts:
            xFact.append(fact)
            xFact.sort()
            if xFact not in factorsList[n]:
                assert(product(xFact) == n), f"{xFacts} is not a factorization of {n}"
                factorsList[n].append(xFact)
    return factorsList[n]

def productSumNumbers(n):
    i = n
    while True:
        facts = generate_all_factor_combinations(i)
        for fact in facts:
            if sum(fact) + (n - len(fact)) == i:
                return i
        i += 1

def main():
    nums = []
    for n in range(2, 12001):
        num = productSumNumbers(n)
        if num not in nums:
            nums.append(num)
    print(sum(nums))

if __name__ == '__main__':
    main()