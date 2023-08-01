from lib.Polynomial import Polynomial

def lagrange(points):
    terms = []
    for i, (xi, yi) in enumerate(points):
        numerators = []
        denominators = []
        for j, (xj, yj) in enumerate(points):
            if i != j:
                term = Polynomial([1, -xj])
                numerators.append(term)
                denominator = xi - points[j][0]
                if denominator == 0:
                    continue
                denominators.append(denominator)
        terms.append({"coefficient":yi, "denominators":denominators, "numerators":numerators})

    
    def g(x):
        def evalTerm(term):
            ret = 1
            for i, numerator in enumerate(term["numerators"]):
                ret *= numerator(x) / term["denominators"][i]
            ret *= term["coefficient"]
            return ret
        ret = 0
        for term in terms:
            ret += evalTerm(term)
        return (ret)
    return g

def main():
    funct = Polynomial([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1])
    # funct = Polynomial([1, 0, 0, 0]) # test
    mismatchSum = 0
    
    for i in range(1, 20):
        points = [(j, funct(j)) for j in range(1, i)]
        g = lagrange(points)
        if(round(g(i)) != funct(i)):
            mismatchSum += round(g(i))
        else:
            break
    print(mismatchSum)


if __name__ == '__main__':
    main()