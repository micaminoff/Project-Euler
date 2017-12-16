# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
# for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
# and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity
# can be written as a 1 through 9 pandigital.

# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

import time

start_time = time.time()


def check_pan(x, y, prod):
    string = ""+x + ""+y + ""+prod  # cast input to string
    if len(string != 9):            # If string is not 9 chars long it cannot be pandigital
        return False
    check_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in check_array:
        if str(num) not in string:
            return False
    return True


def has_no_doubles(number):
    my_dict = {}
    for char in str(number):
        if char in my_dict.keys():
            return False
        else:
            my_dict[char] = 1
    return True


def generate_input_list():
    valid_inputs = []
    for i in range(12, 98766):
        if "0" in str(i):
            continue
        if has_no_doubles(i):
            valid_inputs.append(i)
    return valid_inputs


print(generate_input_list())

# def generate_multiplicands(product):
#     possible_mults = []
#     for i in range(1, 9):
#         if i not in str(product):
#             possible_mults.append(i)
#
#
# for product in range(1234, 100000):
#     = generate_multiplicands(product)

print(time.time()-start_time)
