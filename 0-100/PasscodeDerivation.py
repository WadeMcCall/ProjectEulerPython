def readFile():
    f = open("data/keylog.txt", "r")
    passcodes = []
    for code in f:
        passcodes.append(code.strip())
    passcodes= list(set(passcodes))
    return passcodes

def main():
    passcodes = readFile()
    reconstructedPassword = ""
    while len(passcodes) > 0:
        firstCodes = []
        secondCodes = []
        thirdCodes = []
        for code in passcodes:
            firstCodes.append(code[0])
            if len(code) >= 2:
                secondCodes.append(code[1])
            if len(code) >= 3:
                thirdCodes.append(code[2])
        firstCodes = list(set(firstCodes))
        secondCodes = list(set(secondCodes))
        thirdCodes = list(set(thirdCodes))
        firstDigits = [i for i in firstCodes if i not in secondCodes and i not in thirdCodes]
        for i in firstDigits:
            reconstructedPassword += i
            newCodes = [x[1:] for x in passcodes if x[0] == i and len(x) >= 2]
            passcodes = [x for x in passcodes if x[0] != i]
            passcodes += newCodes
    print(reconstructedPassword)

if __name__ == '__main__':
    main()