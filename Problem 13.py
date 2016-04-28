import time
start_time = time.time()
inp = ""
sum = 0
with open("prob_13_inp", "r") as file:
    inp = file.readlines()

for i in range(len(inp)):
    inp[i] = inp[i].rstrip()

for val in inp:
    sum += int(val)

print(sum)
print(time.time() - start_time)
