from lib.PythagoreanTriples import FindAllPrimePythagoreanTriplesWithPerimeterUnderX

# Euclid's formula generates all prime pythagorean triples
# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

def main():
    wireLengths = FindAllPrimePythagoreanTriplesWithPerimeterUnderX(1500000)

    # sieve
    lengths = [0 for _ in range(1500001)]
    for prime in [i.perimeter for i in wireLengths]:
        for i in range(prime, 1500001, prime):
            lengths[i] += 1
    
    print(len([i for i in lengths if i == 1]))

if __name__ == '__main__':
    main()