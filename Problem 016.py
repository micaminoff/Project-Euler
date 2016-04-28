import time
start_time = time.time()
big_number = str(2**1000)
result = 0
for i in range(len(big_number)):
    result += int(big_number[i])
print(result)
print(time.time() - start_time)
