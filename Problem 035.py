# The number, 197, is called a circular prime because all rotations of the digits:
# 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

# 3.47s, too slow

from math import sqrt
from utilities import e_sieve, Timer

timer = Timer()
primes_under_mill = e_sieve(999999)         # Uses sieve of Erastosthenes, check utilities.py for implementation


def is_not_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:                    # If num is evenly divisible by any number 2-sqrt(num) it cannot be prime
            return True
    return False


def is_circular_prime(number):
    number = str(number)
    rotations = {number[x:] + number[:x] for x in range(len(number))}   # Generates rotations
    for p in rotations:
        if is_not_prime(int(p)):            # If any rotation is not prime, number is not a circular prime
            return False
    return True


circular_primes = set()
for prime in primes_under_mill:             # Check which prime is a circular prime
    if is_circular_prime(prime):
        circular_primes.add(prime)

print(circular_primes)
print(len(circular_primes))

print(timer.end())
