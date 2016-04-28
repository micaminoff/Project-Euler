import time
start_time = time.time()


def sum_of_divisors(num):
    limit = int(num / 2) + 1
    result = 0
    for i in range(1, limit):
        if num % i == 0:
            result += i
    return result

# Populate list of abundant integers
abunds = []
for a in range(1, 28123):
    if sum_of_divisors(a) > a:
        abunds.append(a)
print("Got abunds")
# Calculate sums of abundant pairs
sums = []
for a in range(len(abunds)):
    for b in range(a, len(abunds)):
        result = abunds[a] + abunds[b]
        if result > 28123:
            break
        if result not in sums:
            sums.append(result)
        print("Working at b=", b)
    print("Working at a=", a)
print("Got sums")
# Sum all integers not in sums
answer = 0
for a in range(1, 28124):
    if a not in sums:
        answer += a

print(answer)
print(time.time() - start_time)
