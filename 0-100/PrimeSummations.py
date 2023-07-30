from lib.primes import isPrime
import itertools
import copy

def main():
    primePartitions = [[],[],[[2]],[[3]]]
    primes = [2,3]
    goal = 5000
    while True:
        n = len(primePartitions)
        k = []
        for p in primes:
            newList = copy.deepcopy(primePartitions[n-p])
            for i in newList:
                i.append(p)
                k.append(i)
        for l in k:
            l.sort()
        
        primePartitions.append([])
        for elem in k:
            if elem not in primePartitions[n]:
                primePartitions[n].append(elem)
        if isPrime(n):
            primes.append(n)
            primePartitions[n].append([n])
        if len(primePartitions[n]) >= goal:
            break
    print(len(primePartitions) - 1)

if __name__ == '__main__':
    main()