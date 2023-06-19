from lib.convenience import count_digits

def main():
    sum = 0
    numerator = 1
    denominator = 2
    for i in range(1, 1000):
        numerator += 2 * denominator
        numerator, denominator = denominator, numerator

        tempNumerator = numerator + denominator # add one
        if count_digits(tempNumerator) > count_digits(denominator):
            sum += 1
    
    print(sum)

if __name__ == "__main__":
    main()