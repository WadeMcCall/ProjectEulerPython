from lib.Fraction import Fraction
from lib.convenience import sum_digits

def getNextEConvergentGenerator():
    yield 2
    yield 1
    k = 1
    while True:
        yield 2 * k
        yield 1
        yield 1
        k += 1

def getXTermsinEContinuedFraction(x):
    # 2, 1, 2, 1, 1, 4, 1, 1, 6, 1, ...
    assert(type(x) is int)
    assert x > 0
    gen = getNextEConvergentGenerator()
    series = []
    for i in range(x):
        series.append(next(gen))
    return series

def main():
    series = getXTermsinEContinuedFraction(100)
    print(series)
    f = Fraction(1, series.pop())
    print(f)

    while len(series) > 0:
        f += series.pop()
        f = f.reciprocal()
    f = f.reciprocal()
    print(sum_digits(f.numerator))

if __name__ == "__main__":
    main()