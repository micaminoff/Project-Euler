# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2. For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
# 27s
# O(n^3), Horrendous performance. Needs to be improved

import time

start_time = time.time()


def is_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2        # Return true if the condition is satisfied

for x in range(1, 1000):
    # test a
    for y in range(x, 1000 - x):
        # test b
        for z in range(y, 1000 - y):
            # test c
            if is_triplet(x, y, z) and x + y + z == 1000:
                print(x * y * z)
                print(time.time() - start_time)
                exit()
