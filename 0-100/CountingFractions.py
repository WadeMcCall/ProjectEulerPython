from lib.Fraction import Fraction
from lib.TotientFunctions import findAllPhiUnderX

def count_fractions(d):
    arr = findAllPhiUnderX(d + 1)
    return sum(arr)

def main():
    print(count_fractions(1000000))

if __name__ == '__main__':
    main()