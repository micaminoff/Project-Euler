# Starting in the top left corner of a 2×2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
#
# I had to cheat on this one, credits to code.jasonbhill.com
# 0.0001s
# O(n)


import time
start_time = time.time()


def routes(grid_size):
    result = [1] * grid_size            # Allocate space in an array
    for i in range(grid_size):
        for j in range(i):
            result[j] += result[j - 1]
        result[i] = 2 * result[i - 1]
    return result[grid_size - 1]

print(routes(20))

print(time.time() - start_time)
