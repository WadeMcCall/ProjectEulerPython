from lib.convenience import sum_digits

def main():
    max_sum = 0
    for a in range(1, 100):
        for b in range (1,100):
            num = pow(a, b)
            sum = sum_digits(num)
            if sum > max_sum:
                max_sum = sum
    print(max_sum)


if __name__ == "__main__":
    main()