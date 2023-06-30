import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, x):
        if type(x) is Fraction:
            return NotImplementedError
        self.numerator += x * self.denominator
        return self
    
    def reduce(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def evaluate(self):
        return self.numerator / self.denominator