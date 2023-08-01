import math

class Fraction:
    def __init__(self, numerator, denominator=1, reduce=True):
        if type(numerator) is float:
            numerator, denominator = numerator.as_integer_ratio()
        if type(numerator) is Fraction and type(denominator) is Fraction:
            result = numerator / denominator
            numerator, denominator = result.numerator, result.denominator
        assert type(numerator) is int and type(denominator) is int, f"numerator: {numerator}, denominator: {denominator}"
        self.numerator = numerator
        self.denominator = denominator
        if reduce:
            self.continueReducing = True
            self.reduce()
    
    def reduce(self):
        if self.numerator < 0 and self.denominator < 0 or self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1
        if self.numerator == 0:
            self.denominator = 1
            return
        if self.denominator == 0: # undefined fraction
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
            raise NotImplementedError
        if self.continueReducing:
            result.reduce()
        return result

    def __add__(self, x):
        result = Fraction(self.numerator, self.denominator)
        if type(x) is float:
            x = Fraction(x)
        if type(x) is Fraction:
            lcm = math.lcm(result.denominator, x.denominator)
            x.numerator *= (lcm // x.denominator)
            result.numerator *= (lcm // self.denominator)
            result.denominator = lcm
            result.numerator += x.numerator
        elif type(x) is int:
            result.numerator += x * result.denominator
        else:
            print(type(x), "is not supported")
            raise NotImplementedError
        if self.continueReducing:
            result.reduce()
        return result
    
    def __radd__(self, x):
        return self.__add__(x)
    
    def __mul__(self, x):
        result = Fraction(self.numerator, self.denominator)
        if type(x) is float:
            x = Fraction(x)
        if type(x) is Fraction:
            result.numerator *= x.numerator
            result.denominator *= x.denominator
        elif type(x) is int:
            result.numerator *= x
        else:
            raise NotImplementedError
        if self.continueReducing:
            result.reduce()
        return result
    
    def __truediv__(self, x):
        if type(x) is float:
            x = Fraction(x)
        if type(x) is Fraction:
            result = x.reciprocal()
            result = result * self
        elif type(x) is int:
            result = Fraction(self.numerator, self.denominator * x)
        if self.continueReducing:
            result.reduce()
        return result
    
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