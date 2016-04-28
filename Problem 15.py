# I had to cheat on this one, credits to code.jasonbhill.com
import time
start_time = time.time()


def routes(grid_size):
    result = [1] * grid_size
    for i in range(grid_size):
        for j in range(i):
            result[j] += result[j - 1]
        result[i] = 2 * result[i - 1]
    return result[grid_size - 1]

print(routes(20))

print(time.time() - start_time)
