import time
import math
start_time = time.time()

biggest_tri_num = 1
most_factors = 0
iterator = 2


def get_primes(num):
    factors = 0
    sqrt = int(math.sqrt(num))
    for i in range(1, sqrt):
        if num % i == 0:
            factors += 2
        if i * i == num:
            factors -= 1
    return factors

while most_factors < 500:
    print("Biggest Triangle number = ", biggest_tri_num)
    print("Most Factors = ", most_factors)
    print("Iterator", iterator)
    result = get_primes(biggest_tri_num)
    if result > most_factors:
        most_factors = result
    if most_factors >= 500:
        break
    biggest_tri_num += iterator
    iterator += 1
print(biggest_tri_num, most_factors)
print(time.time() - start_time)
