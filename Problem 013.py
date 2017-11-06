# Work out the first ten digits of the sum of the following one-hundred
# 50-digit numbers. (see prob_13_inp for the numbers)
# 0.0004s
# O(n), could probably be improved by ignoring part of the 100-digit nums


import time
start_time = time.time()
inp = ""
sum = 0
with open("prob_13_inp", "r") as file:  # Store the 100-digit numbers
    inp = file.readlines()

for i in range(len(inp)):
    sum += int(inp[i].rstrip())         # Add all numbers to sum

print(str(sum)[0:10])                   # Print first ten digits
print(time.time() - start_time)
