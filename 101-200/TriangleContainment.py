from lib.Polynomial import Polynomial

class LineSegment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.line = Line(point1, point2)
        self.xIntercept = self._setXIntercept()
        self.yIntercept = self._setYIntercept()

    def _setXIntercept(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        
        if self.line.xIntercept is None:
            return None
        if self.line.xIntercept < min(x1, x2) or self.line.xIntercept > max(x1, x2):
            return None
        return self.line.xIntercept

    def _setYIntercept(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        
        if self.line.yIntercept is None:
            return None
        if self.line.yIntercept < min(y1, y2) or self.line.yIntercept > max(y1, y2):
            return None
        return self.line.yIntercept
            

class Line:
    def __init__(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        self.f = Polynomial([1])
        if x1 == x2:
            self.slope = None
            self.yIntercept = None
            self.xIntercept = x1
        elif y1 == y2:
            self.slope = 0
            self.yIntercept = y1
            self.xIntercept = None
        else:
            self.slope = (y1 - y2) / (x1 - x2)
            self.yIntercept = y1 - self.slope * x1
            self.xIntercept = -self.yIntercept / self.slope
        if self.slope is not None:
            self.f = Polynomial([self.slope, self.yIntercept])

def getTriangles():
    file = open("../data/triangles.txt", "r")
    for line in file:
        coords = line.split(",")
        coords = [(int(coords[i]), int(coords[i+1])) for i in range(0, len(coords) - 1, 2)]
        yield coords

def main():
    triangles = getTriangles()
    sum = 0
    for triangle in triangles:
        a, b, c = triangle
        line1 = LineSegment(a, b)
        line2 = LineSegment(b, c)
        line3 = LineSegment(a, c)
        numPositiveIntercepts = 0
        if line1.xIntercept != None and line1.xIntercept > 0:
            numPositiveIntercepts += 1
        if line2.xIntercept != None and line2.xIntercept > 0:
            numPositiveIntercepts += 1
        if line3.xIntercept != None and line3.xIntercept > 0:
            numPositiveIntercepts += 1
        if numPositiveIntercepts == 1:
            sum += 1
    print(sum)
    return

if __name__ == '__main__':
    main()