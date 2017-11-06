# Find the maximum total [path] from top to bottom of the triangle below:
# Should refactor this into a separate file input
# 0.0002s
# O(n) I think


import time
start_time = time.time()

row1 = [75]
row2 = [95, 64]
row3 = [17, 47, 82]
row4 = [18, 35, 87, 10]
row5 = [20, 4, 82, 47, 65]
row6 = [19, 1, 23, 75, 3, 34]
row7 = [88, 2, 77, 73, 7, 63, 67]
row8 = [99, 65, 4, 28, 6, 16, 70, 92]
row9 = [41, 41, 26, 56, 83, 40, 80, 70, 33]
row10 = [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
row11 = [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
row12 = [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
row13 = [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
row14 = [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
row15 = [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
matrix = [row1, row2, row3, row4, row5, row6, row7, row8, row9, row10, row11,
          row12, row13, row14, row15]

# Start from row 14 and iterate toward top
i = 13
while i >= 0:  # i = row
    for j in range(len(matrix[i])):  # j = column
        left_step = matrix[i][j] + matrix[i + 1][j]
        right_step = matrix[i][j] + matrix[i + 1][j + 1]
        # Replace each value in current row with the sum of the old value and
        # the better option in the next row
        matrix[i][j] = max(left_step, right_step)
    i -= 1

# We end up with the max value in matrix[0][0]
print(matrix[0][0])
print(time.time() - start_time)
