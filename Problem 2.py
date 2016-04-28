num1 = 1
num2 = 1
fib = 0
sum = 0

while fib < 4000000:
    fib = num1 + num2
    if fib % 2 == 0:
        sum += fib

    num1 = num2
    num2 = fib

print(sum)
