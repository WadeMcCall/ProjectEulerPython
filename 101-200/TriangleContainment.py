from lib.Geometry.Line import LineSegment

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