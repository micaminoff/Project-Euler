# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
import time
start_time = time.time()

digit_fifth_powers = []

for i in range(10000, 1000000000):
    s = 0
    for digit in str(i):
        s += int(digit)**5
    if s == i:
        digit_fifth_powers.append(i)

print(digit_fifth_powers)
print(sum(digit_fifth_powers))
print(time.time() - start_time)