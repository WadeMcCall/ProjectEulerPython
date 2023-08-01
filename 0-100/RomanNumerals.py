from lib.RomanNumeral import RomanNumeral

def main():
    f = open("../data/roman.txt", "r")
    sum = 0
    for line in f:
        r = RomanNumeral(line.strip())
        if r.minimal != r.roman:
            sum += len(r.roman) - len(r.minimal)

    print(sum)
    return

if __name__ == '__main__':
    main()