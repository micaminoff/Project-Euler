import time
import math


def e_sieve(limit):
    """
    Generates and returns all primes below limit as a list
    :param limit:
    :return: a list of primes
    """
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
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:                    # If num is evenly divisible by any number 2-sqrt(num) it cannot be prime
            return False
    return True


class Timer:

    def __init__(self):
        self.start_time = time.time()

    def end(self):
        secs, ms = divmod((time.time()-self.start_time)*1000, 1000)
        mins, secs = divmod(secs, 60)
        hrs, mins = divmod(mins, 60)
        return '%01d:%02d:%02d:%03d' % (hrs, mins, secs, ms)
