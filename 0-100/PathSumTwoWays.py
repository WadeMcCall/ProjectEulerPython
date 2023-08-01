import copy

def getMatrix():
    f = open("../data/matrix.txt", "r")
    matrix = []
    for line in f:
        matrix.append([int(x) for x in line.split(",")])
    return matrix

def getNeighbors(matrix, row, column):
    assert(row >= 0 and row < len(matrix))
    assert(column >= 0 and column < len(matrix[0]))
    vals = []
    if row > 0:
        vals.append(matrix[row-1][column])
    if column > 0:
        vals.append(matrix[row][column-1])
    return vals

def addForcedPaths(matrix):
    newMatrix = copy.deepcopy(matrix)
    for row in range(len(matrix) - 1):
        newMatrix[row+1][0] += newMatrix[row][0]
        newMatrix[0][row+1] += newMatrix[0][row]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if(row == 0 or column == 0):
                continue
            neighbors = getNeighbors(newMatrix, row, column)
            newMatrix[row][column] += min(neighbors)
    return newMatrix

def main():
    matrix = getMatrix()
    print(addForcedPaths(matrix)[-1][-1])
    return

if __name__ == '__main__':
    main()