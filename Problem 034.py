# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# 0.12s,
# O(n) since the amount of calculations ultimately depends on the largest i's digits' factorial calculation

import time
from math import factorial


start_time = time.time()

digit_factorials = []
for i in range(10, 50000):      # I need to motivate this upper bound somehow
    sum_of_digit_factorials = 0
    digits = list(str(i))       # For easy manipulation of the digits
    for digit in digits:
        sum_of_digit_factorials += factorial(int(digit))
    if sum_of_digit_factorials == i:
        digit_factorials.append(sum_of_digit_factorials)

print(sum(digit_factorials))

print(time.time() - start_time)
