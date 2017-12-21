# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
# from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
# Similarly we can work from right to left: 3797, 379, 37, and 3.

# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

# 1.35s, could be improved

import utilities as u
timer = u.Timer()


def is_truncatable(prime):
    prime = str(prime)
    for i in range(1, len(prime)):          # Remove digits from the left
        if not u.is_prime(int(prime[i:])):
            return False
    for i in range(len(prime), 0, -1):      # If none of the above checks fail, remove digits from the right
        if not u.is_prime(int(prime[:i])):
            return False
    return True         # We only reach this is we pass through both truncation directions


primes = u.e_sieve(1000000)[4:]      # Ignore primes noted in NOTE
truncatable_primes = []

for p in primes:
    if is_truncatable(p):
        truncatable_primes.append(p)

print(truncatable_primes)
print(sum(truncatable_primes))
print(timer.end())
