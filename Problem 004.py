import time
start_time = time.time()

a = 999
b = 999
biggest_palindrome = 0


def test_palindrome(num):
    string = str(num)
    i = 0
    o = len(string) - 1
    if o % 2 == 0:
        while string[i] == string[o - i]:
            if i == o - 1:
                return True
            i += 1
    else:
        while string[i] == string[o - i]:
            if i == o - 2:
                return True
            i += 1
    return False

while a > 99:
    b = 999
    while b > 99:
        if test_palindrome(a * b):
            if a * b > biggest_palindrome:
                biggest_palindrome = a * b
            break
        b -= 1
    a -= 1
    if test_palindrome(a * b):
        if a * b > biggest_palindrome:
            biggest_palindrome = a * b

print(biggest_palindrome)
print(time.time() - start_time)
