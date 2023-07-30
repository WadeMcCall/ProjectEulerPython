def countRectangles(m, n):
    sum = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            sum += ((m - i) + 1) * ((n - j) + 1)
    return sum

def main():
    goal = 2000000
    minDiff = 2000000
    bestArea = 0
    for i in range(1, 100):
        for j in range(1, 100):
            rect = countRectangles(i, j)
            diff = abs(goal - rect)
            if diff < minDiff:
                minDiff = diff
                bestArea = i * j
    print(bestArea)

if __name__ == "__main__":
    main()