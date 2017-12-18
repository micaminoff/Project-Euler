# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
# and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# 0.24s, could be improved
# No clue on time complexity

import time
from itertools import permutations

start_time = time.time()


def is_pandigital(x, y, prod):
    string = str(x) + str(y) + str(prod)  # cast input to string
    if len(string) != 9:                  # If string is not 9 chars long it cannot be pandigital
        return False
    check_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in check_array:
        if str(num) not in string:        # If a digit is missing the number can't be pandigital
            return False
    return True


def has_no_doubles(number):
    my_dict = {}
    for char in str(number):
        if char in my_dict.keys():  # If we've already found one occurrence of a digit, the number can't be pandigital
            return False            # because of the length=9 constraint
        else:
            my_dict[char] = 1
    return True


def generate_multiplicands(number):
    list_of_tuples = []             # List for storing tuples, e.g. [0] = (1, 2345),[3] = (1234, 5)
    perms = [''.join(p) for p in permutations(str(number))]
    for p in perms:                 # Find all possible substrings of each permutation, kind of
        for i in range(1, len(p)):
            list_of_tuples.append((p[0:i], p[i:]))
    return list_of_tuples


def generate_input_list():
    valid_inputs = []
    for i in range(12345, 98765):
        if "0" in str(i):           # Numbers containing 0 can't be pandigital
            continue
        if has_no_doubles(i):
            i = sorted(str(i))      # Sort i to find permutations quickly
            i = int(''.join(i))     # Join the chararray to a string and cast to int
            if i not in valid_inputs:
                valid_inputs.append(i)
    return valid_inputs


input_list = generate_input_list()
multiplicand_list = []              # Note that this will be a list of lists of tuples
pandigital_products = []

for inp in input_list:
    multiplicand_list.append(generate_multiplicands(inp))

for perm_list in multiplicand_list:  # For each list in our list
    for tup in perm_list:            # For each tuple in that list
        x, y = int(tup[0]), int(tup[1])
        product = x*y
        if is_pandigital(x, y, product) and product not in pandigital_products:
            pandigital_products.append(product)

print(pandigital_products)
print(sum(pandigital_products))
print(time.time()-start_time)
