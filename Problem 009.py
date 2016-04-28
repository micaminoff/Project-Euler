import time

start_time = time.time()


def is_triplet(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return True
    return False

for x in range(1, 1000):
    print("x = ", x)
    # test a
    for y in range(x, 1000 - x):
        print("y = ", y)
        # test b
        for z in range(y, 1000 - y):
            print("z = ", z)
            # test c
            if is_triplet(x, y, z) and x + y + z == 1000:
                print(x * y * z)
                exit()
print(time.time() - start_time)
