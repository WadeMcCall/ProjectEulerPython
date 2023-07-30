from decimal import *
from math import sqrt

def main():
    getcontext().prec = 102 # extra precision for rounding errors
    sum = 0
    for i in range(2, 100):
        num = Decimal(i).sqrt()
        num = str(num)
        for char in num[:-2]:
            if char != '.':
                sum += int(char)
    print(sum)

if __name__ == '__main__':
    main()