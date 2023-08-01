superScriptDigits = {"": "",
                     0: '⁰',
                     1: '¹',
                     2: '²',
                     3: '³',
                     4: '⁴',
                     5: '⁵',
                     6: '⁶',
                     7: '⁷',
                     8: '⁸',
                     9: '⁹'}

def numToSuperScript(num):
    return "".join([superScriptDigits[int(digit)] for digit in str(num)])

class Polynomial:
    def __init__(self, coefficients, isReversed=True, variable="x"):
        assert isinstance(coefficients, list)
        if isReversed:
            coefficients = list(reversed(coefficients))
        self.coefficients = coefficients
        self._trimCoefficients()
        
        self.variable = variable

    def _trimCoefficients(self):
        while self.coefficients[-1] == 0 and len(self.coefficients) > 1:
            self.coefficients.pop(-1)

    def __add__(self, other):
        if isinstance(other, Polynomial):
            length = max(len(self.coefficients), len(other.coefficients))
            result = [0] * length
            difference = abs(len(self.coefficients) - len(other.coefficients))
            if len(self.coefficients) > len(other.coefficients):
                other.coefficients = [0] * difference + other.coefficients
            else:
                self.coefficients = [0] * difference + self.coefficients
            for i in range(length):
                result[i] = self.coefficients[i] + other.coefficients[i]
            self._trimCoefficients()
            return Polynomial(result, isReversed=False, variable=self.variable)
        else:
            return Polynomial([self.coefficients[0] + other] + self.coefficients[1:], isReversed=False, variable=self.variable)

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            length = max(len(self.coefficients), len(other.coefficients))
            result = [0] * length
            difference = abs(len(self.coefficients) - len(other.coefficients))
            if len(self.coefficients) > len(other.coefficients):
                other.coefficients = [0] * difference + other.coefficients
            else:
                self.coefficients = [0] * difference + self.coefficients
            for i in range(length):
                result[i] = self.coefficients[i] - other.coefficients[i]
            self._trimCoefficients()
            return Polynomial(result, isReversed=False, variable=self.variable)
        else:
            return Polynomial([a - other for a in self.coefficients], isReversed=False, variable=self.variable)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
            for degreea, coeffa in enumerate(self.coefficients):
                for degreeb, coeffb in enumerate(other.coefficients):
                    result[degreea + degreeb] += coeffa * coeffb
            return Polynomial(result, isReversed=False, variable=self.variable)
        else:
            return Polynomial([a * other for a in self.coefficients], isReversed=False, variable=self.variable)
        
    def __truediv__(self, other):
        if isinstance(other, Polynomial):
            return NotImplementedError
        else:
            return Polynomial([a / other for a in self.coefficients], isReversed=False, variable=self.variable)

    def __call__(self, x):
        return sum([a * x ** i for i, a in enumerate(self.coefficients)])
    
    def __repr__(self):
        return f"Polynomial({str(self)})"

    def __str__(self):
        def addTerm(coeff, degree, ret):
            if coeff == 0:
                return ret
            if ret != "":
                if coeff < 0:
                    ret += " - "
                else:
                    ret += " + "
            if degree == 0:
                if ret == "":
                    ret += str(coeff)
                else:
                    ret += str(abs(coeff))
                return ret
            if coeff == 1:
                coeff = ""
            if coeff == -1:
                coeff = "-"
            if degree == 1:
                degree = ""
            if not isinstance(coeff, str):
                if coeff % 1 == 0:
                    coeff = int(coeff)
                coeff = str(abs(coeff))
            ret += f"{coeff}{self.variable}{numToSuperScript(degree)}"
            return ret
            
        ret = ""
        for i, coeff in enumerate(reversed(self.coefficients)):
            degree = len(self.coefficients) - i - 1
            ret = addTerm(coeff, degree, ret)
        return ret
    
