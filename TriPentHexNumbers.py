pentagonalNumbers = {}
isPentagonalNums = {}

triangleNumbers = {}
hexagonalNumbers = {}

def isPentagonal(n):
    if(isPentagonalNums.get(n) != None):
        return isPentagonalNums[n]
    val = (1 + (1 + 24 * n) ** 0.5) % 6 == 0
    isPentagonalNums[n] = val
    return val

def getPentagonal(n):
    if(pentagonalNumbers.get(n) != None):
        return pentagonalNumbers[n]
    k = n * (3 * n - 1) // 2
    pentagonalNumbers[n] = k
    return k

def getTriangleNumber(n):
    if(triangleNumbers.get(n) != None):
        return triangleNumbers[n]
    k = n * (n + 1) // 2
    triangleNumbers[n] = k
    return k

def getHexagonalNumber(n):
    if(hexagonalNumbers.get(n) != None):
        return hexagonalNumbers[n]
    k = n * (2 * n - 1)
    hexagonalNumbers[n] = k
    return k

def isHexNumber(n):
    firstHex = 1
    hexNum = 1
    while(firstHex < n):
        hexNum += 1
        firstHex = getHexagonalNumber(hexNum)
        if(n == firstHex):
            return True
    return False

def main():
    n=1
    while(True):
        n += 1
        tri = getTriangleNumber(n)
        if(isPentagonal(tri) and isHexNumber(tri)):
            print(tri)

if __name__ == "__main__":
    main()