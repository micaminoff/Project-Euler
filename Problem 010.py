# Find the sum of all the primes below two million.
# 1.15s
# O(something), send a pull request with explanation if you want to

import time
start_time = time.time()


def e_sieve(limit):                     # Standard sieve of Erastosthenes
    limit += 1
    not_prime = set()
    e_primes = []

    for i in range(2, limit):
        if i in not_prime:
            continue
        for j in range(i*2, limit, i):
            not_prime.add(j)

        e_primes.append(i)

    return e_primes

print(sum(e_sieve(2000000)))
print(time.time() - start_time)
