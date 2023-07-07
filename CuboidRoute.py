import math
from lib.PythagoreanTriples import FindAllPythagoreanTriplesWithHypotenuseUnderX

def findCuboidsWithIntegerShortestPathUnderM(M):
    triples = FindAllPythagoreanTriplesWithHypotenuseUnderX(math.ceil(math.sqrt(M ** 2 + (2 * M) ** 2)))

    sum = 0
    for trip in triples:
        if trip.a > M:
            continue
        num = math.ceil(trip.b / 2)
        if num <= trip.a:
            sum += trip.a - num + 1
        if trip.b <= M:
            sum += math.floor(trip.a/2)
    return sum

def main():
    # could implement a faster search with binary search-like behavior, but this is fast enough
    m = 100
    while(findCuboidsWithIntegerShortestPathUnderM(m) < 700000):
        print(m)
        m += 400
    while(findCuboidsWithIntegerShortestPathUnderM(m) < 950000):
        print(m)
        m += 100
    while(findCuboidsWithIntegerShortestPathUnderM(m) < 990000):
        print(m)
        m += 5
    while(findCuboidsWithIntegerShortestPathUnderM(m) < 1000000):
        print(m)
        m += 1
    print(m)
    return

if __name__ == "__main__":
    main()