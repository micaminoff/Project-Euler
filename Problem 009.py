# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2. For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 0.13s
# O(n^2), bad performance. Could be improved

import time
start_time = time.time()


def is_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2        # Return true if the condition is satisfied


def find_pythagorean_triplet(sum_to_find):
    for a in range(1, sum_to_find):
        for b in range(a, sum_to_find - a):  # a and b are interchangeable so no need to check all values of b
            c = sum_to_find - a - b          # a+b+c has to equal sum_to_find
            if is_triplet(a, b, c):
                return a, b, c

triplet = find_pythagorean_triplet(1000)
print(triplet[0]*triplet[1]*triplet[2])     # Calculate and output product of triplet
print(time.time() - start_time)
