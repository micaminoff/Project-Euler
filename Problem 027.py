import time

start_time = time.time()


def e_sieve(limit):
    limit += 1
    not_prime = set()
    e_primes = []

    for i in range(2, limit):
        if i in not_prime:
            continue
        for j in range(i*2, limit, i):
            not_prime.add(j)

        e_primes.append(i)

    return e_primes


def is_prime(num):
    i = 0
    while primes[i] <= num:
        if primes[i] == num:
            return True
        i += 1
    return False


def evaluate_function(n, a, b):
    return n**2 + a*n + b


def amount_of_primes(a, b):
    primes_found = 0
    for n in range(100):
        if not is_prime(evaluate_function(n, a, b)):
            break
        else:
            primes_found += 1
    return primes_found


def iterate_functions():
    best_pair = -999, -1000
    best_primes = 0
    for a in range(-999, 1000):
        for b in range(-999, 1000, 2):
            if a != 0 and b != 0:
                woo_primes = amount_of_primes(a, b)
                if woo_primes > best_primes:
                    best_pair = a, b
                    best_primes = woo_primes
    return best_pair

primes = e_sieve(evaluate_function(99, 999, 1000))

print(iterate_functions())

print(time.time() - start_time)
