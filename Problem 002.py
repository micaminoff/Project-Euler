# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.
# <0.001s
# O(n), no optimization needed

from utilities import Timer

timer = Timer()
num1 = 1
num2 = 1
fib = 0
sum = 0

while fib < 4000000:
    fib = num1 + num2   # find next element in fib sequence
    if fib % 2 == 0:    # if found element is even, add to sum
        sum += fib

    num1 = num2         # remember "previous" fib number
    num2 = fib          # this is an unnecessary variable but I'm lazy

print(sum)
print(timer.end())
