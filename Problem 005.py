# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# 5.57s
# O(n), but small optimizations probably still possible

import time

start_time = time.time()


def is_divisible(num):
    for i in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:  # Removed all factors that are already included
        if num % i != 0:                                # in larger factors
            return False
    return True

a = 9699690  # product of all primes < 20

while True:
    if a % 20 == 0:     # Find a good starting point
        break
    a += 19
print(a)

while True:
    if a > 232792560:
        print("Sanity check failed.")
        break
    if is_divisible(a):
        print(a)
        break
    a += 20

print(time.time() - start_time)
