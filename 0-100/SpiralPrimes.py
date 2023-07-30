from lib.primes import isPrime

def getNextCornerNumbers(currentSideLength, largestCurrentNumber):
    add = currentSideLength + 1
    return [largestCurrentNumber + add, largestCurrentNumber + 2 * add, largestCurrentNumber + 3 * add, largestCurrentNumber + 4 * add]

def main():
    largestCurrentNum = 9
    sideLength = 3
    numPrimes = 3
    numTotal = 5
    while ((numPrimes / numTotal) * 100) > 10:
        print(numPrimes / numTotal)
        newNums = (getNextCornerNumbers(sideLength, largestCurrentNum))
        prime_count = sum(isPrime(n) for n in newNums)
        numPrimes += prime_count
        numTotal += 4
        sideLength += 2
        largestCurrentNum = newNums[-1]
    print(sideLength)

if __name__ == "__main__":
    main()