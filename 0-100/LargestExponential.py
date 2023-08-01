import math

# return the number of digits in the evaluated expression
def findMagnitude(base, exp):
    return (exp * math.log10(base)) + 1

def main():
    file = open("../data/base_exp.txt", "r")
    max = 0
    maxline = 0
    i = 1
    for line in file:
        words = line.split(",")
        base = int(words[0])
        exp = int(words[1])
        magnitude = (findMagnitude(base, exp))
        if magnitude >= max:
            max = magnitude
            maxline = i
        i += 1
    print(maxline)
    return

if __name__ == '__main__':
    main()