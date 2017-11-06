# The following iterative sequence is defined for the set of positive integers:
# n -> n/2 (if n is even)
# n -> 3n+1 (if n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Which starting number, under one million, produces the longest chain?
# 84.7s
# O(n*(length_of_Collatz(n)), lots of room for improvement

# Thoughts: check if term is a power of two, use logarithm to get chain length
# faster

import time
start_time = time.time()


def get_next(n):
    if n % 2 == 0:          # If n is divisible by two
        return int(n / 2)
    return int((3 * n) + 1)

start_num = 2               # 1 can't be the longest chain
longest_chain = 0
best_starting_num = 0

while start_num < 1000000:
    chain_length = 1
    term = start_num        # Number currently under consideration
    while term != 1:        # While we're not at the end of a chain
        term = get_next(term)
        chain_length += 1
    if chain_length > longest_chain:
        longest_chain = chain_length
        best_starting_num = start_num
    start_num += 1

print(best_starting_num)
print(time.time() - start_time)
