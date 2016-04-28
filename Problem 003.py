import time
import math
start_time = time.time()
num = 600851475143
primes = [2, 3, 5, 7, 11, 13]
i = 3


def is_prime(test):
    for prime in primes:
        if test % prime == 0:
            print(test, prime)
            return False
        else:
            continue
    if test not in primes:
        primes.append(test)
    print("PRIME! ", test)
    return True

while i <= num:
    if num % i == 0:
        while is_prime(i):
            num = math.ceil(num / i)
            print(i, num)
    i += 2

print(i - 2)
print(time.time() - start_time)
