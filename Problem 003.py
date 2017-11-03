# What is the largest prime factor of the number 600851475143?
# 0.0005s
# Could be improved with modified prime test. Sieve of Eratosthenes is simple but I'm too lazy

import time
import math
start_time = time.time()
num = 600851475143
primes = [2, 3, 5, 7, 11, 13]
i = 3


def is_prime(test):
    for prime in primes:
        if test % prime == 0:       # For a number to be prime it can have no prime factors
            return False
        else:
            continue
    if test not in primes:
        primes.append(test)         # If this is a new prime, we add it to our list for future reference
    return True

while i <= num:
    if num % i == 0:
        while is_prime(i):
            num = math.ceil(num / i)  # Shrink the problem space if we find a prime
            print(i, num)
    i += 2

print(i - 2)                        # Since the last factor considers is 1 it also increases i by two, so ignore that
print(time.time() - start_time)
