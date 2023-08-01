from lib.Polynomial import Polynomial

def main():
    funct = Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
    mismatchSum = 0
    
    for i in range(1, 20):
        points = [(j, funct(j)) for j in range(1, i)]
        g = Polynomial.polyFit(points)
        if(round(g(i)) != funct(i)):
            mismatchSum += round(g(i))
        else:
            break
    print(mismatchSum)


if __name__ == '__main__':
    main()