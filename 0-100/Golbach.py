from lib.primes import Primes 

primes = Primes(10000)

def followsGoldbach(n):
    if(n in primes.primes):
        return None
    k = 1
    twiceSquare = 2 * (k ** 2)
    while(twiceSquare < n):
        if (n - twiceSquare) in primes.primes:
            return True
        k += 1
        twiceSquare = 2 * (k ** 2)
    return False

def main():
    n = 9
    while(n < max(primes.primes)):
        while(n in primes.primes):
            n += 2
        if not followsGoldbach(n):
            print(n)
            return
        n += 2

if __name__ == "__main__":
    main()