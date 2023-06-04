from collections import Counter

def have_common_elements(list1, list2):
    return any(element in set(list2) for element in list1)

def are_permutations(s1, s2):
    return Counter(s1) == Counter(s2)
