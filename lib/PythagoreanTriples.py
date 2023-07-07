from lib.TotientFunctions import is_coprime
import math

class RightTriangle:
    def __init__(self, a, b, c):
        self.a = min(a, b)
        self.b = max(a, b)
        self.c = c
        self.perimeter = a + b + c
        self.area = None

    def getArea(self):
        if self.area == None:
            self.area = self.a * self.b // 2
        return self.area
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b and self.c == other.c
    
    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.a}, {self.b}, {self.c})"
    
def makesIntegerTriple(a, b):
    return math.sqrt(a ** 2 + b ** 2) % 1 == 0

def isPythagoreanTriple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2 and a %1 == 0 and b %1 == 0 and c %1 == 0 

def FindAllPythagoreanTriplesWithHypotenuseUnderX(x):
    n = 1
    triangles = []

    # I'm overgenerating here, this is really sloppy but still fast enough...
    while True:
        m = n+2
        while True:
            if is_coprime(m, n):
                a = m * n
                b = (m ** 2 - n ** 2) // 2
                c = (m ** 2 + n ** 2) // 2
                if not c > x:
                    triangles.append(RightTriangle(a, b, c))
                else:
                    break
            m += 2
        n += 2
        if n * n > x:
            break

    # sieve
    for triangle in triangles:
        for i in range(0, x):
            c = (i + 2) * triangle.c
            if c > x:
                break
            newTriangle = RightTriangle((i + 2) * triangle.a, (i + 2) * triangle.b, c)
            if newTriangle not in triangles:
                triangles.append(newTriangle)

    return triangles

def FindAllPrimePythagoreanTriplesWithPerimeterUnderX(x):
    n = 1
    triangles = []

    # I'm overgenerating here, this is really sloppy but still fast enough...
    while True:
        m = n+2
        while True:
            if is_coprime(m, n):
                a = m * n
                b = (m ** 2 - n ** 2) // 2
                c = (m ** 2 + n ** 2) // 2
                if not a + b + c > x:
                    triangles.append(RightTriangle(a, b, c))
                else:
                    break
            m += 2
        n += 2
        if n * n > x:
            break

    return triangles