# credit where it's due https://math.stackexchange.com/questions/265690/continued-fraction-of-a-square-root
import math
from decimal import *
from lib.ContinuedSqrtFraction import ContinuedSqrtFraction

def main():
    numOddPeriods = 0
    for i in range(1, 10001):
        if math.sqrt(i) % 1 == 0:
            continue
        cf = ContinuedSqrtFraction(i)
        if cf.getPeriodOfSquareRoot() % 2 == 1:
            numOddPeriods += 1
    print(numOddPeriods)

if __name__ == "__main__":
    main()