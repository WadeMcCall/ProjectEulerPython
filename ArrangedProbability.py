# using algebra, we obtain the form 
# x = 1/4 (-(1 + sqrt(2)) (3 - 2 sqrt(2))^n + (sqrt(2) - 1) (3 + 2 sqrt(2))^n + 2) and 
# y = 1/8 ((2 + sqrt(2)) (3 - 2 sqrt(2))^n - (sqrt(2) - 2) (3 + 2 sqrt(2))^n + 4)
# which generates positive solutions by plugging in n > 0

import math

def funct(n):
    x = 1/4 * (-(1 + math.sqrt(2)) * (3 - 2 * math.sqrt(2)) ** n + (math.sqrt(2) - 1) * (3 + 2 * math.sqrt(2)) ** n + 2)
    y = 1/8 * ((2 + math.sqrt(2)) * (3 - 2 * math.sqrt(2)) ** n - (math.sqrt(2) - 2) * (3 + 2 * math.sqrt(2)) ** n + 4)
    return x, y

def main():
    TARGET = 10**12
    i = 2
    nums = [0, 0]
    while nums[0] < TARGET:
        nums = funct(i)
        i += 1
    print(round(nums[1]))
    return

if __name__ == '__main__':
    main()