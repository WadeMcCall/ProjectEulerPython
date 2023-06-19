from collections import Counter
from math import factorial

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
