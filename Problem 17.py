import time
start_time = time.time()
# For readability:
hundred = 7
thousand = 8

# Vars
test_num = 15
length = 0
three = [1, 2, 6, 9, 10]
four = [4, 5, 9]
five = [3, 7, 8, 40, 50, 60]
six = [11, 12, 20, 30, 80, 90]
seven = [15, 16, 70]
eight = [13, 14, 19]
nine = [18]


for i in range(1, test_num + 1):
    if i == 1000:
        length += 3 + thousand
        break
    string = str(test_num)
    if len(string) == 3:
        a = string[0]
        b = string[1]
        c = string[2]
        # Check largest digit
        if a in three:
            length += 3
        elif a in four:
            length += 4
        elif a in five:
            length += 5
        length += hundred
        # "One hundred" case
        if b == 0 and c == 0:
            continue


print(test_num, length)
print(time.time() - start_time)
