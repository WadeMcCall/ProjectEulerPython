class Primes:
    def __init__(self, x):
        self.primes = []
        self.max_sieved = 0
        self.sieve_of_eratosthenes(x)
        
    def _grow(self):
        new_max = max(2 * self.max_sieved, self.primes[-1] * 2 or 1)
        self.sieve_of_eratosthenes(new_max)
        self.max_sieved = new_max

    # don't use unless you are using the rest of this class and need to generate primes. Use the lone function below!
    def isPrime(self, x):
        while(x > max(self.primes)):
            self._grow()
        return x in self.primes
    
    def getNextPrimeGenerator(self, x = 0):
        index = 0
        while (max(self.primes) < x):
            self._grow()
        while self.primes[index] < x:
            index += 1
        while True:
            if index == len(self.primes):
                self._grow()
            yield self.primes[index]
            index += 1
            
    def sieve_of_eratosthenes(self, n):
        """Find all primes less than or equal to n using the Sieve of Eratosthenes."""
        # Initialize a new array from max_sieved to n
        primesArr = [True for _ in range(self.max_sieved, n+1)]
        
        for p in self.primes:
            if p * p > n:
                break
            start = max(p * p, (self.max_sieved // p) * p)
            if start < self.max_sieved:
                start = start + p
            for i in range(start, n+1, p):
                primesArr[i - self.max_sieved] = False
    
        p = max(2, self.max_sieved)
        while p * p <= n:
            if primesArr[p - self.max_sieved] is True:
                for i in range(p * p, n+1, p):
                    primesArr[i - self.max_sieved] = False
                self.primes.append(p)
            p += 1
    
        for i in range(max(p, self.max_sieved), n+1):
            if primesArr[i - self.max_sieved]:
                self.primes.append(i)
        
        self.max_sieved = n

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
