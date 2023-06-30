class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __add__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial([a + b for a, b in zip(self.coefficients, other.coefficients)])
        else:
            return Polynomial([self.coefficients[0] + other] + self.coefficients[1:])

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            return Polynomial([a - b for a, b in zip(self.coefficients, other.coefficients)])
        else:
            return Polynomial([a - other for a in self.coefficients])

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for i, a in enumerate(self.coefficients):
                for j, b in enumerate(other.coefficients):
                    result[i + j] += a * b
            return Polynomial(result)
        else:
            return Polynomial([a * other for a in self.coefficients])

    def __call__(self, x):
        return sum([a * x ** i for i, a in enumerate(self.coefficients)])

    def __str__(self):
        if self.coefficients[0] == 0:
            ret = ""
        else:
            ret = str(self.coefficients[0]) + " + "

        return ret + " + ".join(["{}x^{}".format(a, i + 1) for i, a in enumerate(self.coefficients[1:]) if a != 0])
    
