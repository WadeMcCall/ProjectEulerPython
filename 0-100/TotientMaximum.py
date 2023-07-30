from lib.primes import getNextPrimeGenerator

def main():
    gen = getNextPrimeGenerator()
    n = 1
    for x in gen:
        product = n * x
        if product > 1000000:
            break
        n = product
    print(n) 
    
if __name__ == '__main__':
    main()