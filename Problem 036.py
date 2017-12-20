# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

# 1.2s, can probably be improved
# TODO: Split is_palindrome() to preparation and comparison

import time
from math import floor, ceil
start_time = time.time()


def is_palindrome(num):
    num = str(num)              # Convert input to string
    num = num.lstrip('0')       # Strip 0 from 0b... binary representation of int
    num = num.lstrip('b')       # Strip b from 0b... --"--
    num = num.lstrip('0')       # Strip all possible leading zeroes
    reversed_str = list(reversed(num))  # Reverse num for faster second half checking
    if len(num) == 1:
        return True             # len(1) num must be palindrome
    if len(num) % 2 != 0:
        first_half = num[0:ceil(len(num)/2)]    # Get halfway
        second_half = ''.join(reversed_str[0:ceil(len(num) / 2)])   # Get halfway in reversed string
    else:
        first_half = num[0:floor(len(num)/2)]
        second_half = ''.join(reversed_str[0:floor(len(num) / 2)])
    return first_half == second_half    # Returns true if the first half of num == reversed second half of num


double_base_palindromes = []

for i in range(1, 1000000, 2):  # Step 2, since binary numbers ending in 0 cannot be palindrome if leading 0 disallowed
    if is_palindrome(i) and is_palindrome(bin(i)):
        double_base_palindromes.append(i)

print(double_base_palindromes)
print(sum(double_base_palindromes))

print(time.time()-start_time)
