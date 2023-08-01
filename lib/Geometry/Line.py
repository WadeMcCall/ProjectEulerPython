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