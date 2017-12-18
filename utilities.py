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
