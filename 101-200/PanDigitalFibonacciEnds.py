def isPandigital(n):
    n = str(n)
    for i in range(1, 10):
        if str(i) not in n:
            return False
    return True

def fibGen():
    fibs = [(1, 1), (1, 1)]
    while True:
        fib1x, fib1y = fibs[-1]
        fib2x, fib2y = fibs[-2]
        x, y = fib1x + fib2x, fib1y + fib2y
        if len(str(x)) > 20:
            xlen = len(str(x))
            pows = (xlen - 20)
            x = x // 10 ** pows
            fibs[-2] = (fibs[-2][0] // 10 ** pows, fibs[-2][1])
            fibs[-1] = (fibs[-1][0] // 10 ** pows, fibs[-1][1])
        if len(str(y)) > 9:
            y = int(str(y)[-9:])
        fibs.append((x, y))
        yield (fibs[-1])

def main():
    fibs = fibGen()
    k = 3
    for x, y in fibs:
        if len(str(x)) > 9:
            leng = (len(str(x)))
            x = x // 10 ** (leng - 9)
        if isPandigital(y) and isPandigital(x):
            print(k)
            break
        k += 1

if __name__ == '__main__':
    main()