from lib.primes import getPrimeArray
from lib.convenience import primeFacs
import math

def main():
    M = 50000000
    PRIMES = getPrimeArray(math.ceil(math.sqrt(M)))
    sum = 0
    nums = {}
    for i in range(len(PRIMES)):
        num1 = PRIMES[i] ** 2
        if num1 >= M:
            break
        for j in range(len(PRIMES)):
            num2 = num1 + PRIMES[j] ** 3
            if num2 >= M:
                break
            for k in range(len(PRIMES)):
                num = num2 + PRIMES[k] ** 4
                if num >= M:
                    break
                nums[num] = 1
    print(len(list(nums.keys())))
    return

if __name__ == '__main__':
    main()