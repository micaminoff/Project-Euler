import time

start_time = time.time()
primes = [2, 3]
prime_sum = 5
i = 5


def is_prime(test):
    for prime in primes:
        if test % prime == 0:
            return False
        else:
            continue
    if test not in primes:
        primes.append(test)
    return True

while i < 2000000:
    if is_prime(i):
        prime_sum += i
        print(i, prime_sum)
    i += 2

print(prime_sum)
print(time.time() - start_time)
