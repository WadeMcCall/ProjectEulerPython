from lib.Partitions import p

def main():
    n = 1
    while True:
        if p(n) % 1000000 == 0:
            print(n)
            break
        n += 1

if __name__ == '__main__':
    main()