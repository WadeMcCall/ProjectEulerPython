# A collection of useful functions that i havent categorized into another file yet

from collections import Counter
from math import factorial, sqrt
from functools import reduce

def have_common_elements(list1, list2):
    return any(element in set(list2) for element in list1)

def are_permutations(s1, s2):
    return Counter(s1) == Counter(s2)

def XchooseN(x, n):
    if x == n:
        return 1
    assert x > n, "x must be larger than or equal to n"
    return factorial(x)/ (factorial(n) * factorial(x - n))

def reverse_number(num):
    return int(str(num)[::-1])

def is_palindrome(num):
    return num == reverse_number(num)

def sum_digits(num):
    # Convert the number to a string to be able to iterate over the digits
    num_str = str(num)
    
    # Use a list comprehension to convert each digit back to an integer and sum them
    return sum(int(digit) for digit in num_str)

def count_digits(num):
    return len(str(num))

# Steiner Lima's answer here: https://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))