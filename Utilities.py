class Sieve:

    def __init__(self, limit):
        self._limit = limit
        self._primes = set(range(limit))
        self._primes.remove(0)
        self._primes.remove(1)
        for x in range(2, limit):
            if x in self._primes:
                factor = x**2
                while factor < limit:
                    if factor in self._primes:
                        self._primes.remove(factor)
                    factor = factor + x

    def print_primes(self):
        for num in self._primes:
            print(num)

    def is_prime(self, num):
        if num > self._limit:
            print("limit is too low for this sieve")
        elif num in self._primes:
            return True
        else:
            return False