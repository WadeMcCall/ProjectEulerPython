import sys

pentagonalNumbers = []
isPentagonalNums = {}


def isPentagonal(n):
    if(isPentagonalNums.get(n) != None):
        return isPentagonalNums[n]
    val = (1 + (1 + 24 * n) ** 0.5) % 6 == 0
    isPentagonalNums[n] = val
    return val

def getPentagonal(n):
    if(pentagonalNumbers.__len__() > n):
        return pentagonalNumbers[n]
    k = n * (3 * n - 1) // 2
    pentagonalNumbers.append(k)
    return k

def main():
    minDiff = sys.maxsize
    print(minDiff)
    for i in range(1, 5000):
        for j in range(1, 5000):
            iPent = getPentagonal(i)
            jPent = getPentagonal(j)
            difference = abs(iPent - jPent)
            if(i%1000 == 0 and j % 1000 == 0):
                print("i: " +str(i) + " j: " + str(j))
            if(difference > minDiff):
                continue
            if not isPentagonal(iPent + jPent) or not isPentagonal(difference):
                continue
            if(difference < minDiff and difference > 0):
                minDiff = difference
                print("minimum diff so far: " + str(minDiff))

    print("mindiff:" + str(minDiff))


if __name__ == "__main__":
    main()