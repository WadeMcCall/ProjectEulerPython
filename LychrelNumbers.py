from lib.convenience import reverse_number, is_palindrome

def main():
    sum = 0
    # check all numbers under 10k
    for i in range(1, 10000):
        num = i
        lychrel = True
        # check 50 iterations deep
        for j in range(50):
            num = num + reverse_number(num)
            if(is_palindrome(num)):
                lychrel = False
                break
        if lychrel is True:
            sum += 1
    print(sum)


if __name__ == "__main__":
    main()