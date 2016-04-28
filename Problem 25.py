import time
start_time = time.time()

num1 = 1
num2 = 1
fib = 0
counter = 2

while len(str(fib)) < 1000:
    fib = num1 + num2
    num1 = num2
    num2 = fib
    counter += 1

print(counter)
print(time.time() - start_time)
