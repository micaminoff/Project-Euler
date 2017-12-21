# Find the sum of all the multiples of 3 or 5 below 1000
# 0.0005006790161132812 seconds
# O(n), could probably be optimized but is fast enough for current input

from utilities import Timer

timer = Timer()
sum = 0

for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

print(timer.end())
