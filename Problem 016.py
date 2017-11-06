# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 21000?
# 0.0003s
# O(n)

import time
start_time = time.time()
big_number = str(2**1000)           # Cast 2^1000 to string
result = 0
for i in range(len(big_number)):    # Go through all digits in big_num
    result += int(big_number[i])    # Cast the digit to int and add to result

print(result)
print(time.time() - start_time)
