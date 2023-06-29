class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, x):
        if type(x) is Fraction:
            return NotImplementedError
        if type(x) is not int:
            return NotImplementedError
        self.numerator += x * self.denominator
        return self

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def evaluate(self):
        return self.numerator / self.denominator