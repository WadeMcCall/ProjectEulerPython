from math import isqrt
from itertools import combinations, permutations

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def getNumsFromPermutation(perm, anagram):
    perm = list(perm)
    word1 = anagram[0]
    letterValues = {}
    for letter in word1:
        if letter in letterValues:
            continue
        letterValues[letter] = perm.pop()
    nums = []

    for word in anagram:
        for letter in word:
            word = word.replace(letter, str(letterValues[letter]))
        if word[0] == '0':
            continue
        nums.append(int(word))

    return nums

def getCombinationsForAnagram(anagrams):
    n = getNumDifferentLetters(anagrams[0])
    combs = list(combinations(digits, n))
    
    perms = []
    for comb in combs:
        # generate permutations of the combination without leading 0's
        perms.append(list(permutations(comb)))
    return perms

def isSquare(n):
    return isqrt(n) ** 2 == n

def findAnagrams(word, words):
    anagrams = []
    for word2 in words:
        if word == word2:
            continue
        if sorted(word) == sorted(word2):
            anagrams.append(word2)
    return anagrams

def getNumDifferentLetters(word):
    letters = []
    for letter in word:
        if letter not in letters:
            letters.append(letter)
    return len(letters)

def getWords():
    file = open("../data/words.txt", "r")
    words = file.read().split(",")
    #remove quotes
    words = [word[1:-1] for word in words]
    return words

def sortWordsIntoLengthGroups(words):
    lengthGroups = []
    i = 0
    for word in words:
        if len(word) > i:
            lengthGroups.append([])
            i += 1
        lengthGroups[-1].append(word)
    return lengthGroups

def removeWordsWithMoreThan10DifferentLetters(words):
    for word in words:
        if getNumDifferentLetters(word) > 10:
            words.remove(word)
    return words

def main():
    words = getWords()
    words = removeWordsWithMoreThan10DifferentLetters(words)
    words.sort(key=len)
    words = sortWordsIntoLengthGroups(words)
    words.reverse()

    for group in words:
        for word in group:
            anagrams = findAnagrams(word, group)
            if len(anagrams) == 0:
                continue
            anagrams.append(word)
            for word in anagrams:
                group.remove(word)
            combinations = getCombinationsForAnagram(anagrams)
            print(anagrams)
            for combination in combinations:
                for perm in combination:
                    nums = getNumsFromPermutation(perm, anagrams)
                    if len(nums) < 2:
                        continue
                    nums = [num for num in nums if isSquare(num)]
                    if len(nums) < 2:
                        continue
                    print(max(nums))
                    return
    return

if __name__ == '__main__':
    main()