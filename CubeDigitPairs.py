from itertools import combinations

squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

def canMakeSquare(die1, die2, square):
    if int(square[0]) in die1 and int(square[1]) in die2:
        return True
    if int(square[1]) in die1 and int(square[0]) in die2:
        return True
    return False

def canMakeAllSquares(die1, die2):
    global squares

    if 6 in die1:
        die1.append(9)
    if 9 in die1:
        die1.append(6)
    if 6 in die2:
        die2.append(9)
    if 9 in die2:
        die2.append(6)
    
    for square in squares:
        if not canMakeSquare(die1, die2, square):
            return False
    return True

def main():
    oneDigitNums = [i for i in range(10)]
    combs = [list(i) for i in combinations(oneDigitNums, 6)]
    sum = 0
    for i in range(len(combs)):
        for j in range(i, len(combs)):
            if canMakeAllSquares(combs[i], combs[j]):
                sum += 1
    print(sum)
    return

if __name__ == '__main__':
    main()