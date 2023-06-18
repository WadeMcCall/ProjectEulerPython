from lib.convenience import XchooseN

# n is the first number found which is greater than the number we're looking for
def howManyOverNum(x, n):
    middle = x / 2
    diff = middle - n
    return 2 * diff + 1

def main():
    numOver = 1000000
    sum = 0
    for i in range(23, 101):
        for j in range(i):
            res = XchooseN(i, j)
            if res > numOver:
                sum += howManyOverNum(i, j)
                break
    print(sum)
    return

if __name__ == "__main__":
    main()