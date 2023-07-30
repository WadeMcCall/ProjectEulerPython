import time

sqDigits = {1: 1, 89: 89}

def squareDigits(x):
    strX = str(x)
    sum = 0
    for digit in strX:
        sum += int(digit)**2
    return sum

def findDigitChain(x):
    global sqDigits
    chain = [x]
    while True:
        if chain[-1] in sqDigits:
            chain.append(sqDigits[chain[-1]])
            return chain
        chain.append(squareDigits(chain[-1]))


def main():
    global sqDigits
    sum = 0
    for i in range(1, 10000000):
        # progress bar
        if i % 1000000 == 0:
            prinstr = "[" + "■" * (i // 1000000) + " " * (10 - (i // 1000000)) + "]"
            print(prinstr, end="\r")
        chain = findDigitChain(i)
        if chain[-1] == 89:
            sum += 1
        for num in chain:
            sqDigits[num] = chain[-1]
    print()
    print(sum)
    return

if __name__ == '__main__':
    main()