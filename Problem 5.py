import time

start_time = time.time()


def is_divisible(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

a = 22
while True:
    if is_divisible(a):
        print(a)
        break
    a += 2

print(time.time() - start_time)
