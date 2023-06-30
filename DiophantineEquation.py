# this problem is pell's equation: https://en.wikipedia.org/wiki/Pell%27s_equation
# AKA more continued fraction shenanigans

from lib.ContinuedSqrtFraction import ContinuedSqrtFraction
from itertools import cycle
import math

def main():
    max = 0
    bigD = 0
    # x^2 - d * y^2 = 1
    for d in range(1000):
        if math.sqrt(d) % 1 == 0:
            continue
        cf = ContinuedSqrtFraction(d)
        gen = cf.getFractionalConvergentGenerator()
        for frac in gen:
            if frac.numerator ** 2 - d * frac.denominator ** 2 == 1:
                if frac.numerator > max:
                    max = frac.numerator
                    bigD = (d)
                break
    print(bigD)
    return

if __name__ == "__main__":
    main()