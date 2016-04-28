import time

start_time = time.time()

letter_values = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7,
                 "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14,
                 "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21,
                 "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26}
total_name_score = 0

# Handle input
with open("prob_22_inp", "r") as file:
    names = file.readline().split(",")
names.sort()

# Iterate through all names
for i in range(len(names)):
    name_score = 0
    # Iterate through every character
    for char in names[i].strip('"'):
        name_score += letter_values[char]
    # Multiply by position in list, then add to total value
    name_score *= i + 1
    total_name_score += name_score
    # Debug line
    print(names[i], name_score)
    
print(total_name_score)
print(time.time() - start_time)
