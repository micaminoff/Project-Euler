# Find the largest palindrome made from the product of two 3-digit numbers.
# 0.41s
# O(n^2), a lot of room for improvement

import time
start_time = time.time()

a = 999
b = 999
biggest_palindrome = 0


def test_palindrome(num):                   # Checks if input is a palindrome
    string = str(num)
    i = 0
    o = len(string) - 1
    if o % 2 == 0:                          # We need two approaches depending on if the palindrome is
        while string[i] == string[o - i]:   # of odd or even length
            if i == o - 1:                  # While items equally far away from start and end are the same
                return True                 # If we're at the middle, return True
            i += 1
    else:
        while string[i] == string[o - i]:
            if i == o - 2:
                return True
            i += 1
    return False

while a > 99:                               # We're only concerned with 3-digit numbers
    b = 999
    while b > 99:
        if test_palindrome(a * b):
            if a * b > biggest_palindrome:
                biggest_palindrome = a * b
            break
        b -= 1                              # We're working downward
    a -= 1
    if test_palindrome(a * b):
        if a * b > biggest_palindrome:
            biggest_palindrome = a * b

print(biggest_palindrome)
print(time.time() - start_time)
