# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# 0.4s, can probably be improved
# TODO: Split is_palindrome() to preparation and comparison

from utilities import Timer
timer = Timer()


def is_palindrome(num):
    num = str(num)              # Convert input to string
    num = num.lstrip('0b')      # Strip 0b from 0b... binary representation of int
    return num == num[::-1]     # Check if the number is the same after it's reversed.


double_base_palindromes = []

for i in range(1, 1000000, 2):  # Step 2, since binary numbers ending in 0 cannot be palindrome if leading 0 disallowed
    if int(str(i)[0]) % 2 == 0:
        continue
    if is_palindrome(i) and is_palindrome(bin(i)):
        double_base_palindromes.append(i)

print(double_base_palindromes)
print(sum(double_base_palindromes))

print(timer.end())
