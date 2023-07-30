from lib.convenience import factorial

def digit_factorial(n):
    return sum([factorial(int(i)) for i in str(n)])

def find_chain(n):
    chain = [n]
    while True:
        next = digit_factorial(chain[-1])
        if next in chain:
            return chain
        chain.append(next)

def main():
    sum = 0
    for i in range(1000000):
        if i % 100000 == 0:
            print("Progress: " + str(int(i/100000)) + "0%")
        if (len(find_chain(i)) == 60):
            sum += 1
    print(sum)

if __name__ == '__main__':
    main()