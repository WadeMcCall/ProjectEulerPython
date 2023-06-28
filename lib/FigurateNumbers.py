def SquareNumberGen():
    n = 1
    while True:
        yield n * n
        n += 1

def triangleNumberGen():
    n = 1
    while True:
        yield n * ((n + 1) / 2)
        n += 1

def pentagonalNumberGen():
    n = 1
    while True:
        yield n * ((3*n - 1) / 2)
        n += 1

def hexagonalNumberGen():
    n = 1
    while True:
        yield n * (2 * n - 1)
        n += 1

def heptagonalNumberGen():
    n = 1
    while True:
        yield n * ((5 * n - 3) / 2)
        n += 1

def octagonalNumberGen():
    n = 1
    while True:
        yield n  * (3 * n - 2)
        n += 1