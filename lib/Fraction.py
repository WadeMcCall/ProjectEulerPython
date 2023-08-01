import math

class Fraction:
    def __init__(self, numerator, denominator, reduce=True):
        assert type(numerator) is int and type(denominator) is int
        self.numerator = numerator
        self.denominator = denominator
        if reduce:
            self.continueReducing = True
            self.reduce()
    
    def reduce(self):
        if self.numerator == 0 or self.denominator == 0:
            return
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def evaluate(self):
        assert self.denominator != 0
        return self.numerator / self.denominator
    
    def __sub__(self, x):
        result = Fraction(self.numerator, self.denominator)
        if type(x) is Fraction:
            lcm = math.lcm(self.denominator, x.denominator)
            x.numerator *= (lcm // x.denominator)
            result.numerator *= (lcm // self.denominator)
            result.denominator = lcm
            result.numerator -= x.numerator
        elif type(x) is int:
            result.numerator -= x * result.denominator
        else:
            return NotImplementedError
        if self.continueReducing:
            result.reduce()
        return result

    def __add__(self, x):
        result = Fraction(self.numerator, self.denominator)
        if type(x) is Fraction:
            lcm = math.lcm(result.denominator, x.denominator)
            x.numerator *= (lcm // x.denominator)
            result.numerator *= (lcm // self.denominator)
            result.denominator = lcm
            result.numerator += x.numerator
        elif type(x) is int:
            result.numerator += x * result.denominator
        else:
            return NotImplementedError
        if self.continueReducing:
            result.reduce()
        return result
    
    def __mul__(self, x):
        result = Fraction(self.numerator, self.denominator)
        if type(x) is Fraction:
            result.numerator *= x.numerator
            result.denominator *= x.denominator
        elif type(x) is int:
            result.numerator *= x
        else:
            return NotImplementedError
        if self.continueReducing:
            result.reduce()
        return result
    
    def __truediv__(self, x):
        result = Fraction(self.numerator, self.denominator)
        result = result.reciprocal()
        return result * x
    
    def mixedForm(self):
        if self.numerator > self.denominator:
            return str(self.numerator // self.denominator) + " " + str(self.numerator % self.denominator) + "/" + str(self.denominator)
        else:
            return str(self.numerator) + "/" + str(self.denominator)
    
    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, x):
        if type(x) is Fraction:
            x.reduce()
            temp = Fraction(self.numerator, self.denominator)
            temp.reduce()
            return temp.numerator == x.numerator and temp.denominator == x.denominator
        return self.evaluate() == x
    
    def __ne__(self, x):
        return not self.__eq__(x)
    
    def __lt__(self, x):
        if type(x) is Fraction:
            return self.evaluate() < x.evaluate()
        return self.evaluate() < x
    
    def __gt__(self, x):
        if type(x) is Fraction:
            return self.evaluate() > x.evaluate()
        return self.evaluate() > x
    
    def __le__(self, x):
        if type(x) is Fraction:
            return self.evaluate() <= x.evaluate()
        return self.evaluate() <= x
    
    def __ge__(self, x):
        if type(x) is Fraction:
            return self.evaluate() >= x.evaluate()
        return self.evaluate() >= x