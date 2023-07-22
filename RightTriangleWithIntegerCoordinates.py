from lib.Fraction import Fraction

def main():
    boxSize = 50
    sum = 0
    for x in range(boxSize + 1):
        for y in range(boxSize + 1):
            # There is no line segment between the origin and itself
            if y == 0 and x == 0:
                continue
            # slope of the perpindecular line
            slope = Fraction(-y, x)
            if slope.denominator == 0:
                slope = Fraction(0, 1)
            if slope.numerator == 0:
                slope = Fraction(1, 0)
            slope.reduce()
            i = 1
            while True:
                previousSum = sum
                newPoint1 = (x + i * slope.numerator, y + i * slope.denominator)
                newPoint2 = (x - i * slope.numerator, y - i * slope.denominator)
                if newPoint1[0] <= boxSize and newPoint1[1] <= boxSize and newPoint1[0] >= 0 and newPoint1[1] >= 0:
                    sum += 1
                if newPoint2[0] <= boxSize and newPoint2[1] <= boxSize and newPoint2[0] >= 0 and newPoint2[1] >= 0:
                    sum += 1
                if sum == previousSum:
                    break
                i += 1
    # triangles with their right angle at the origin
    sum += boxSize ** 2
    print(sum)
    return

if __name__ == '__main__':
    main()