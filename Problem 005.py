import time

start_time = time.time()


def is_divisible(num):
    for i in [7, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        if num % i != 0:
            return False
    return True

a = 9699690  # product of all primes < 20

while True:
    if a % 20 == 0:
        break
    a += 19
print(a)

while True:
    if a > 232792560:
        print("Ni har tänkt fel.")
        break
    if is_divisible(a):
        print(a)
        break
    a += 20

print(time.time() - start_time)
