from lib.primes import Primes
from itertools import combinations, permutations

primes = Primes(1000000)

def replace_asterisks_with_digits(s):
    num_asterisks = s.count('*')  # Count the number of asterisks in the string
    if num_asterisks == 0:  # No asterisks to replace
        return [s]
    
    result = []
    for digit in range(10):  # Iterate from 0 to 9
        replaced_s = s.replace('*', str(digit))  # Replace all asterisks with the same digit
        result.append(replaced_s)

    return result

def replace_digits_with_asterisks(num, x):
    num = str(num)
    num_length = len(num)
    result = []

    # Iterate over all possible combinations of x positions within the number
    for combo in combinations(range(num_length - 1), x):  # Exclude the last digit
        replaced_num = list(num)  # Convert to list for easy replacement
        for index in combo:
            replaced_num[index] = '*'
        result.append(''.join(replaced_num))

    return result

def checkForNReplacedPrimes(primeStr, n):
    replacedDigits = replace_asterisks_with_digits(primeStr)
    numPrimes = 0
    for num in replacedDigits:
        if primes.isPrime(int(num)):
            numPrimes += 1
            if(numPrimes == n):
                print(numPrimes)
                return True
            
    return False

def add_asterisks(num, x):
    num_str = str(num)
    num_length = len(num_str)

    # Calculate the number of asterisks needed to reach x digits
    num_asterisks = x - num_length

    # If no asterisks are needed, return the original number
    if num_asterisks <= 0:
        return [num_str]

    # If we need more asterisks than available spaces (not replacing first and last digit), return empty list
    if num_asterisks > num_length:
        return []

    # Create a string with the original number plus the needed asterisks
    num_str_with_asterisks = num_str + '*' * num_asterisks

    # Now generate all permutations, filter those that have an asterisk in the first or last position
    result = [''.join(p) for p in permutations(num_str_with_asterisks) if p[0] != '*' and p[-1] != '*']

    return result


def main():
    for i in range(10000):
        numsTocheck = []
        if(i % 2 == 0 or i % 5 == 0 or i%10 == 0):
            continue  
        for j in range(len(str(i)), 6):
            numsTocheck = add_asterisks(i, j)
            print(numsTocheck)
        for num in numsTocheck:
            if(checkForNReplacedPrimes(num, 6)):
                print(num)
                return


if __name__ == "__main__":
    main()