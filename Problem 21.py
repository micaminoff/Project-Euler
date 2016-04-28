import time
start_time = time.time()


def sum_of_divisors(num):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i
    return result

amicable_sum = 0
for j in range(1, 10000):
    a = sum_of_divisors(j)
    b = sum_of_divisors(a)
    if j == b and j != a:
        amicable_sum += j
print(amicable_sum)
print(time.time() - start_time)
