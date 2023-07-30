
sigFigures = 10000000000
sum = 0

def main():
    global sum
    for n in range(1, 1000):
        if(n%10 == 0):
            continue
        sum += n**n % sigFigures
    print(sum)

if __name__ == "__main__":
    main()