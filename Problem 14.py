import time
start_time = time.time()


def get_next(n):
    if n % 2 == 0:
        return int(n / 2)
    return int((3 * n) + 1)
start_num = 2
longest_sequence = 0
best_starting_num = 0

while start_num < 1000000:
    sequence = 1
    term = start_num
    while term != 1:
        term = get_next(term)
        sequence += 1
    if sequence > longest_sequence:
        longest_sequence = sequence
        best_starting_num = start_num
    start_num += 1
print(best_starting_num)
print(time.time() - start_time)
