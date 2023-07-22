import math

class Fraction:
    def __init__(self, numerator, denominator):
        assert type(numerator) is int and type(denominator) is int
        self.numerator = numerator
        self.denominator = denominator
    
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

    def __add__(self, x):
        if type(x) is Fraction:
            lcm = math.lcm(self.denominator, x.denominator)
            x.numerator *= (lcm // x.denominator)
            self.numerator *= (lcm // self.denominator)
            self.denominator = lcm
            self.numerator += x.numerator
            return self
        elif type(x) is int:
            self.numerator += x * self.denominator
            return self
        return NotImplementedError
    
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