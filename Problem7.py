from Utilities import Sieve

sieve = Sieve(200000)
prime_list = list(sieve._primes)
prime_list.sort()
print(prime_list[10000])