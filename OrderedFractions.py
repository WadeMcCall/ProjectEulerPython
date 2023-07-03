from lib.Fraction import Fraction

def main():
    numerator = 0
    denominator = 1
    closest = Fraction(0, 1)
    ideal = Fraction(3, 7)
    while denominator <= 1000000:
        frac = Fraction(numerator, denominator)
        if frac >= ideal:
            denominator += 1
            continue
        if frac > closest:
            closest = frac
        numerator += 1
    print(closest)
                

if __name__ == '__main__':
    main()