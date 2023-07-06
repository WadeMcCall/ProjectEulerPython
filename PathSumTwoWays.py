import copy

def getMatrix():
    f = open("data/matrix.txt", "r")
    matrix = []
    for line in f:
        matrix.append([int(x) for x in line.split(",")])
    return matrix

def addForcedPaths(matrix):
    newMatrix = copy.deepcopy(matrix)
    for row in range(len(matrix) - 1):
        newMatrix[row+1][0] += newMatrix[row][0]
        newMatrix[0][row+1] += newMatrix[0][row]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if(row == 0 or column == 0):
                continue
            newMatrix[row][column] += min(newMatrix[row-1][column], newMatrix[row][column-1])
    return newMatrix

def main():
    matrix = getMatrix()
    print(addForcedPaths(matrix))
    return

if __name__ == '__main__':
    main()