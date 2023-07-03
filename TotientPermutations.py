from lib.TotientFunctions import findAllPhiUnderX
from lib.convenience import are_permutations

def main():
    arr = findAllPhiUnderX(10 ** 7)
    min = 10 ** 7
    for num in range(2, 10 ** 7):
        ratio = num/arr[num - 2]
        if ratio < min:
            if are_permutations(str(num), str(arr[num - 2])):
                print(num)
                min = ratio

if __name__ == '__main__':
    main()