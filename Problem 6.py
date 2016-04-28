import time

start_time = time.time()
sum_of_squares = 0
helper = 0

for i in range(1, 101):
    sum_of_squares += i * i
    helper += i

square_of_sums = helper * helper

print(square_of_sums - sum_of_squares)
print(time.time() - start_time)
