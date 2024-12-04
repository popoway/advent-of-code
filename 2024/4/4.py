'''
read of lines from input.txt that formats like:
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

input = []
discard = []

# store them in a 2D list

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        input.append(list(line.strip()))

# print the 2D list
# for line in input:
#     print(''.join(line))

# initialize the discard list with 2D list of True
for i in range(len(input)):
    discard.append([])
    for j in range(len(input[0])):
        discard[i].append(True)

# loop through the 2D list and check the pattern
# 1. XMAS
# 2. SAMX
# 3. X
#    M
#    A
#    S
# 4. S
#    A
#    M
#    X
# 5. X
#     M
#      A
#       S
# 6. S
#     A
#      M
#       X
# 7.    X
#      M
#     A
#    S
# 8.    S
#      A
#     M
#    X

count = 0

for i in range(len(input)):
    for j in range(len(input[0])):
        # Case 1
        if j + 3 < len(input[0]) and input[i][j] == 'X' and input[i][j+1] == 'M' and input[i][j+2] == 'A' and input[i][j+3] == 'S':
            discard[i][j] = False
            discard[i][j+1] = False
            discard[i][j+2] = False
            discard[i][j+3] = False
            count += 1
        # Case 2
        if j + 3 < len(input[0]) and input[i][j] == 'S' and input[i][j+1] == 'A' and input[i][j+2] == 'M' and input[i][j+3] == 'X':
            discard[i][j] = False
            discard[i][j+1] = False
            discard[i][j+2] = False
            discard[i][j+3] = False
            count += 1
        # Case 3
        if i + 3 < len(input) and input[i][j] == 'X' and input[i+1][j] == 'M' and input[i+2][j] == 'A' and input[i+3][j] == 'S':
            discard[i][j] = False
            discard[i+1][j] = False
            discard[i+2][j] = False
            discard[i+3][j] = False
            count += 1
        # Case 4
        if i + 3 < len(input) and input[i][j] == 'S' and input[i+1][j] == 'A' and input[i+2][j] == 'M' and input[i+3][j] == 'X':
            discard[i][j] = False
            discard[i+1][j] = False
            discard[i+2][j] = False
            discard[i+3][j] = False
            count += 1
        # Case 5
        if i + 3 < len(input) and j + 3 < len(input[0]) and input[i][j] == 'X' and input[i+1][j+1] == 'M' and input[i+2][j+2] == 'A' and input[i+3][j+3] == 'S':
            discard[i][j] = False
            discard[i+1][j+1] = False
            discard[i+2][j+2] = False
            discard[i+3][j+3] = False
            count += 1
        # Case 6
        if i + 3 < len(input) and j + 3 < len(input[0]) and input[i][j] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j+2] == 'M' and input[i+3][j+3] == 'X':
            discard[i][j] = False
            discard[i+1][j+1] = False
            discard[i+2][j+2] = False
            discard[i+3][j+3] = False
            count += 1
        # Case 7
        if i + 3 < len(input) and j - 3 >= 0 and input[i][j] == 'X' and input[i+1][j-1] == 'M' and input[i+2][j-2] == 'A' and input[i+3][j-3] == 'S':
            discard[i][j] = False
            discard[i+1][j-1] = False
            discard[i+2][j-2] = False
            discard[i+3][j-3] = False
            count += 1
        # Case 8
        if i + 3 < len(input) and j - 3 >= 0 and input[i][j] == 'S' and input[i+1][j-1] == 'A' and input[i+2][j-2] == 'M' and input[i+3][j-3] == 'X':
            discard[i][j] = False
            discard[i+1][j-1] = False
            discard[i+2][j-2] = False
            discard[i+3][j-3] = False
            count += 1

# update the 2D list with the discard list
for i in range(len(input)):
    for j in range(len(input[0])):
        if discard[i][j]:
            input[i][j] = '.'

# print the updated 2D list
for line in input:
    print(''.join(line))

print(count)



## Part 2


input = []
discard = []

# store them in a 2D list

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        input.append(list(line.strip()))

# print the 2D list
# for line in input:
#     print(''.join(line))

# initialize the discard list with 2D list of True
for i in range(len(input)):
    discard.append([])
    for j in range(len(input[0])):
        discard[i].append(True)

# loop through the 2D list and check the pattern
# 1. M S
#     A
#    M S
# 2. S M
#     A
#    S M
# 3. M M
#     A
#    S S
# 4. S S
#     A
#    M M

count = 0

for i in range(len(input)):
    for j in range(len(input[0])):
        # Case 1
        if i + 2 < len(input) and j + 2 < len(input[0]) and input[i][j] == 'M' and input[i][j+2] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j] == 'M' and input[i+2][j+2] == 'S':
            discard[i][j] = False
            discard[i][j+2] = False
            discard[i+1][j+1] = False
            discard[i+2][j] = False
            discard[i+2][j+2] = False
            count += 1
        # Case 2
        if i + 2 < len(input) and j + 2 < len(input[0]) and input[i][j] == 'S' and input[i][j+2] == 'M' and input[i+1][j+1] == 'A' and input[i+2][j] == 'S' and input[i+2][j+2] == 'M':
            discard[i][j] = False
            discard[i][j+2] = False
            discard[i+1][j+1] = False
            discard[i+2][j] = False
            discard[i+2][j+2] = False
            count += 1
        # Case 3
        if i + 2 < len(input) and j + 2 < len(input[0]) and input[i][j] == 'M' and input[i][j+2] == 'M' and input[i+1][j+1] == 'A' and input[i+2][j] == 'S' and input[i+2][j+2] == 'S':
            discard[i][j] = False
            discard[i][j+2] = False
            discard[i+1][j+1] = False
            discard[i+2][j] = False
            discard[i+2][j+2] = False
            count += 1
        # Case 4
        if i + 2 < len(input) and j + 2 < len(input[0]) and input[i][j] == 'S' and input[i][j+2] == 'S' and input[i+1][j+1] == 'A' and input[i+2][j] == 'M' and input[i+2][j+2] == 'M':
            discard[i][j] = False
            discard[i][j+2] = False
            discard[i+1][j+1] = False
            discard[i+2][j] = False
            discard[i+2][j+2] = False
            count += 1

# update the 2D list with the discard list
for i in range(len(input)):
    for j in range(len(input[0])):
        if discard[i][j]:
            input[i][j] = '.'

# print the updated 2D list
for line in input:
    print(''.join(line))

print(count)