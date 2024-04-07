from itertools import combinations

def getSets():
    file = open("../data/sets.txt", "r")
    for set in file:
        set = set.strip()
        set = set.split(",")
        set = [int(x) for x in set]
        set.sort()
        yield set

def isSpecialSumSet(set):
    if not testAxiom2(set):
        return False
    if not testAxiom1(set):
        return False
    return True

# assumes axiom 2 is true
# 1. S(B) != S(A) for any disjoint non-empty subsets A, B.
def testAxiom1(set):
    def sharesElements(subset1, subset2):
        for x in subset1:
            if x in subset2:
                return True
        return False
    max = len(set) // 2
    for i in range(2, max + 1):
        subsets = combinations(set, i)
        combos = combinations(list(subsets), 2)
        n = 0
        for subset1, subset2 in combos:
            if sharesElements(subset1, subset2):
                continue
            n += 1
            if sum(subset1) == sum(subset2):
                print(subset1, subset2, "failed axiom 1.")
                return False
        print(i, n)
    print(set, f"passed axiom 1. n = {n}")
    return True


# 2. If B contains more elements than C then S(B) > S(C).
def testAxiom2(set):
    for i in range(1, (len(set) - 1) // 2 + 1):
        subset1 = set[:i+1]
        subset2 = set[-i:]
        endSum = sum(subset2)
        beginningSum = sum(subset1)
        if beginningSum < endSum:
            print(subset1, subset2, "failed axiom 2")
            return False
    return True

def main():
    sets = getSets()
    val = 0
    for set in sets:
        if isSpecialSumSet(set):
            val += sum(set)
    print(val)
    return

def test():
    set = [21, 33, 34, 35, 37, 40, 46]
    set.sort()
    isSpecialSumSet(set)
    return

if __name__ == '__main__':
    test()