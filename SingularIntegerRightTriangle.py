from lib.TotientFunctions import is_coprime

# Euclid's formula generates all prime pythagorean triples
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
def findAllPrimeTripleSumsUnderX(x):
    wireLengths = []
    n = 1

    # I'm overgenerating here, this is really sloppy but still fast enough...
    while True:
        m = n+2
        while True:
            if is_coprime(m, n):
                a = m * n
                b = (m ** 2 - n ** 2) // 2
                c = (m ** 2 + n ** 2) // 2
                wireLengths.append(a + b + c)
                if a + b + c > x:
                    break
            m += 2
        n += 2
        if n * n > x:
            break

    wireLengths = [wireLengths[i] for i in range(len(wireLengths)) if wireLengths[i] <= x]
    return wireLengths

def main():
    wireLengths = findAllPrimeTripleSumsUnderX(1500000)

    # sieve
    lengths = [0 for _ in range(1500001)]
    for prime in wireLengths:
        for i in range(prime, 1500001, prime):
            lengths[i] += 1
    
    print(len([i for i in lengths if i == 1]))

if __name__ == '__main__':
    main()