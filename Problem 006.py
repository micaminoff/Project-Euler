# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.
# <0.001s
# O(n), can easily be O(1) with formula for square of sums and sum of squares

import time

start_time = time.time()
sum_of_squares = 0
helper = 0

for i in range(1, 101):         # Just brute force since it's a small problem
    sum_of_squares += i * i
    helper += i

square_of_sums = helper * helper

print(square_of_sums - sum_of_squares)
print(time.time() - start_time)
