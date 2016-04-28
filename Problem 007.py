import time

start_time = time.time()

primes = [2, 3, 5, 7, 11, 13]
i = 6
largest_prime = 17


def is_prime(test):
    for prime in primes:
        if test % prime == 0:
            return False
        else:
            continue
    if test not in primes:
        primes.append(test)
    return True

while i < 10001:
    if is_prime(largest_prime):
        if i == 10001:
            print(largest_prime)
            exit()
        i += 1
    largest_prime += 1

print(largest_prime)
print(time.time() - start_time)
