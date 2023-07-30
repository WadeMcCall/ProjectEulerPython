# 28433 * 2 ^ 7830457 + 1

modulo = 10 ** 10

def stepExponent(num):
    return (num * 2) % modulo

def main():
    num = 1
    for _ in range(7830457):
        num = stepExponent(num)
    num = (num * 28433) % modulo
    num += 1
    print(num)
    return

if __name__ == '__main__':
    main()