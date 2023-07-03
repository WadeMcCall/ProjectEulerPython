from lib.TotientFunctions import is_coprime
import math

def main():
    sum = 0
    for d in range(4, 12001): # skip 1/2 and 1/3
        arr = [i for i in range(math.ceil(d/3), (d//2) + 1) if is_coprime(i, d)]
        sum += len(arr)
    print(sum)

if __name__ == '__main__':
    main()