from lib.primes import Primes

primes = Primes(1000)

# given a prime number, can it be written as the sum of consecutive primes?
def isConsecutivePrimeSum(x):
    for prime in primes.primes:
        if(prime > x/2):
            return False
        sum = 0
        numTerms = 0
        generator = primes.getNextPrimeGenerator(prime)
        for prime in generator:
            sum += prime
            numTerms += 1
            if(sum == x):
                return {"numTerms" : numTerms, "prime" : x, "terms": primes.primes[primes.primes.index(prime) - numTerms + 1:primes.primes.index(prime) + 1]}
            if(sum > x):
                break

def findMaxConsecutivePrimeSum(index):
    generator = primes.getNextPrimeGenerator(primes.primes[index])
    sum = 0
    numTerms = 0
    currBest = {"numTerms" : 0, "prime" : 0}
    for prime in generator:
        sum += prime
        numTerms += 1
        if sum > 1000000:
            break
        if(primes.isPrime(sum)):
            currBest = {"numTerms" : numTerms, "prime" : sum}
    return currBest

def main():
    currBest = { "numTerms" : 0, "prime" : 0}
    for index in range(0, len(primes.primes)):
        newBest = findMaxConsecutivePrimeSum(index)
        if(newBest["numTerms"] > currBest["numTerms"]):
            currBest = newBest
            print(currBest)
    print(currBest)

if __name__ == "__main__":
    main()