from lib.primes import Primes
primes = Primes(100)

generator = primes.getNextPrimeGenerator(1000)
for prime in generator:
    if(prime > 5000):
        break
    print(prime)