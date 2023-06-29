from lib.convenience import count_digits
from lib.Fraction import Fraction

def main():
    sum = 0

    fraction = Fraction(1,2)
    for i in range(1, 1000):
        fraction += 2
        fraction = fraction.reciprocal()

        tempNumerator = fraction.numerator + fraction.denominator # add one
        if count_digits(tempNumerator) > count_digits(fraction.denominator):
            sum += 1
    
    print(sum)

if __name__ == "__main__":
    main()