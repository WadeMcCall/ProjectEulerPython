from lib.convenience import are_permutations 

def check_leftmost_digit(num):
    # Convert the number to a string to be able to access the digits
    num_str = str(num)
    
    # Check if the leftmost digit is greater than or equal to 5
    if int(num_str[0:2]) >= 17:
        return False
    else:
        return True
    
def next_smallest_larger_digits(num):
    # Convert the number to a string to get the number of digits
    num_digits = len(str(num))
    
    # The next smallest number with a larger number of digits is 10 raised to the power of the current number of digits
    next_num = 10 ** num_digits
    
    return next_num

    
def find_next_x(n):
    n += 1
    if not check_leftmost_digit(n):
        n = next_smallest_larger_digits(n) + 1
    return n

def main():
    x = 10
    while True:
        for i in range(2, 6):
            if not (are_permutations(str(x), str(x * i))):
                x = find_next_x(x)
                break
            print(x)
            if(i == 6):
                print(x)
                return

if __name__ == "__main__":
    main()