import time
import math
start_time = time.time()

result = 0
for digit in str(math.factorial(100)):
    result += int(digit)
print(result)

print(time.time() - start_time)
