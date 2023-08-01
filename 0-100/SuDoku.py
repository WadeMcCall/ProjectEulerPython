class Space:
    def __init__(self, num):
        if num is None or num == '0':
            self.possible = ['1','2','3','4','5','6','7','8','9']
            self.value = '■'
        else:
            self.value = num
            self.possible = [num]

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self)

class SuDoku:
    def __init__(self, nums):
        self._nums = nums
        self.spaces = self._initSpaces(nums)
        self.squares = self._initSquares()
        self.guessing = False

    # this method ended up not being used. It was here in case we had to guess deeper than one guess
    def _checkForContradictions(self):
        for space in self.spaces:
            if space.value == '■' and len(space.possible) == 0:
                return True
        return False
    
    def _guess(self):
        if self.guessing:
            return False
        for x in range(9):
            for y in range(9):
                if self.spaces[x][y].value == '■':
                    for possibility in self.spaces[x][y].possible:
                        newSuDo = SuDoku(self._nums)
                        newSuDo.spaces[x][y].value = possibility
                        newSuDo.guessing = True
                        newSuDo.solve()
                        if newSuDo.isCompleted():
                            self.spaces = newSuDo.spaces
                            return True
        return False

    def isCompleted(self):
        for row in self.spaces:
            for space in row:
                if space.value == '■':
                    return False
        return True

    def _analyzeValues(self, lst, space, skip):
        changed = False
        for i in range(9):
            if i == skip:
                continue
            if lst[i].value != '■' and lst[i].value in space.possible:
                val = lst[i].value
                space.possible.remove(val)
                changed = True
        return changed

    def _analyzePossibilities(self, lst, space, skip):
        changed = False
        for j in range (9):
            found = False
            looking = 0
            for i in range(9):
                looking = str(j + 1)
                if looking not in space.possible:
                    found = True
                    break
                if(i == skip):
                    continue
                if looking in lst[i].possible:
                    found = True
                    break
            if not found:
                space.value = looking
                space.possible = [looking]
                changed = True
        return changed

    def _columnPass(self, x, y):
        return self._analyzeValues([self.spaces[i][y] for i in range(9)], self.spaces[x][y], x)

    def _rowPass(self, x, y):
        return self._analyzeValues(self.spaces[x], self.spaces[x][y], y)

    def _squarePass(self, x, y):
        square = self._getSquare(x, y)
        squareCoords = self._spaceToSquareCoords(x, y)
        return self._analyzeValues(square, self.spaces[x][y], squareCoords[1])
    
    def _columnPass2(self, x, y):
        return self._analyzePossibilities([self.spaces[i][y] for i in range(9)], self.spaces[x][y], x)

    def _rowPass2(self, x, y):
        return self._analyzePossibilities(self.spaces[x], self.spaces[x][y], y)

    def _squarePass2(self, x, y):
        changed = False
        square = self._getSquare(x, y)
        squareCoords = self._spaceToSquareCoords(x, y)
        changed = self._analyzePossibilities(square, self.spaces[x][y], squareCoords[1])
        
        return changed

    
    def _removePossibilities(self, lst, possibility, skip):
        changed = False
        for i in range(len(lst)):
            if i in skip:
                continue
            if possibility in lst[i].possible:
                changed = True
                lst[i].possible.remove(possibility)
        return changed

    def _solvePass1(self, x, y):
        changed = False
        changed = self._columnPass(x, y)
        changed = self._rowPass(x, y) or changed
        changed = self._squarePass(x, y) or changed
        return changed
    
    def _solvePass2(self, x, y):
        changed = False
        changed = self._columnPass2(x, y)
        changed = self._rowPass2(x, y) or changed
        changed = self._squarePass2(x, y) or changed
        return changed

    def _solveSpace(self, x, y):
        space = self.spaces[x][y]
        if space.value != '■':
            return
        
        changed = False
        changed = self._solvePass1(x, y)
        if self._solvePass2(x, y):
            changed = True
        
        if len(space.possible) == 1:
            self.spaces[x][y].value = self.spaces[x][y].possible[0]
            return True
        return changed
    
    # considering i ended up having to implement guess and check, this is probably not necessary
    # it is such a specific case that it is not worth the time to implement
    # but i already did, so fuck it, we ball.
    # ---------------------------------------
    # this method checks if there is a row or column in a square which is the only row or column that
    # has a certain possibility. Then if it is, it removes the possibility 
    # from the other spaces in that row or column in the rest of the puzzle
    def _checkSquare(self, index):
        square = self.squares[index]
        changed = False
        for i in range(1, 10):
            val = str(i)
            if val in [space.value for space in square]:
                continue
            for j in range(3):
                columnIndexes = [j, j + 3, j + 6]
                # check if only one column has the possibility
                if val not in square[columnIndexes[0]].possible and \
                val not in square[columnIndexes[1]].possible and \
                val not in square[columnIndexes[2]].possible:
                    continue

                foundOtherPossibility = False
                for k in range(9):
                    if k in columnIndexes:
                        continue
                    if val in square[k].possible:
                        foundOtherPossibility = True
                        break
                
                # only one column in this square has this possibility, so we need to remove the possibility 
                # in the same column from all the other squares in this column of the puzzle
                if not foundOtherPossibility:
                    column = (index % 3) * 3 + j
                    skips = [index // 3 * 3, index // 3 * 3 + 1, index // 3 * 3 + 2]
                    changed = self._removePossibilities([self.spaces[k][column] for k in range(9)], val, skips) or changed
            
            for j in range(3):
                rowIndexes = [j * 3, j * 3 + 1, j * 3 + 2]
                # check if only one row has the possibility
                if val not in square[rowIndexes[0]].possible and \
                val not in square[rowIndexes[1]].possible and \
                val not in square[rowIndexes[2]].possible:
                    continue

                foundOtherPossibility = False
                for k in range(9):
                    if k in rowIndexes:
                        continue
                    if val in square[k].possible:
                        foundOtherPossibility = True
                        break
                # only one row in this square has this possibility, so we need to remove the possibility
                # in the same row from all the other squares in this row of the puzzle
                if not foundOtherPossibility:
                    row = (index // 3) * 3 + j
                    skips = [index % 3 * 3, index % 3 * 3 + 1, index % 3 * 3 + 2]
                    changed = self._removePossibilities(self.spaces[row], val, skips) or changed
        return changed


    def solve(self):
        while True:
            changed = False
            for i in range(9):
                for j in range(9):
                    if self.spaces[i][j].value == '■':
                        thisOneChanged = self._solveSpace(i, j)
                        if not changed:
                            changed = thisOneChanged
            if changed:
                continue
            for i in range(9):
                square = self.squares[i]
                if '■' not in [space.value for space in square]:
                    continue # Square is solved
                sqChange = self._checkSquare(i)
                if not changed:
                    changed = sqChange
            if not changed:
                if self.isCompleted():
                    return
                self._guess()
                break
        return

    def _getSquare(self, x, y):
        return self.squares[self._spaceToSquareCoords(x, y)[0]]
    
    def _spaceToSquareCoords(self, x, y):
        row = x // 3
        column = y // 3
        sqRow = x - row * 3
        sqColumn = y - column * 3
        yCoord = sqRow * 3 + sqColumn
        return (row*3 + column, yCoord)
    
    def _squareToSpaceCoords(self, x, y):
        row = x // 3
        spRow = row + y // 3
        column = x % 3 * 3
        spColumn = column + y % 3
        return (spRow, spColumn)

    def _initSpaces(self, nums):
        spaces = []
        for i in range(len(nums)):
            spaces.append([])
            for value in nums[i]:
                spaces[i].append(Space(value))
        return spaces

    def _initSquares(self):
        squares = []
        for square in range(9):
            squares.append([])
            for i in range(3):
                for j in range(3):
                    iOffset = square //  3 * 3
                    jOffset = square * 3 % 9
                    squares[square].append(self.spaces[i + iOffset][j + jOffset])
        return squares

    def __str__(self):
        ret = "SUDOKU:\n"
        for j in range(9):
            for i in range(9):
                if i % 3 == 0 and i != 0:
                    ret += "| "
                ret += str(self.spaces[j][i]) + " "
                if i == 8:
                    ret += "\n"
            if j % 3 == 2 and j != 8:
                ret += "---------------------\n"
        return ret
    
    def __repr__(self):
        return str(self)
    
def getSuDoku(file):    
    nums = []
    row = 0
    for line in file:
        if line[0] == 'G':
            continue
        nums.append([])
        for i in range(9):
            nums[row].append(line[i])
        row+=1
        if row == 9:
            sudo = SuDoku(nums)
            yield sudo
            nums = []
            row = 0
    return

def main():
    file = open("../data/sudoku.txt", "r")
    sum = 0
    for sudo in getSuDoku(file):
        sudo.solve()
        sum += int(sudo.spaces[0][0].value) * 100 + int(sudo.spaces[0][1].value) * 10 + int(sudo.spaces[0][2].value)
    print(sum)
    return

if __name__ == '__main__':
    main()