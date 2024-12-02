'''
read of integers from input.txt that formats like:
9 12 14 16 17 18 15
86 88 91 94 95 95
15 18 20 21 23 25 28 32
'''
with open('input.txt', 'r') as f:
    lines = f.readlines()

safe_count = 0

for line in lines:
    numbers = list(map(int, line.strip().split()))
    decreasing = False
    increasing = False
    increment = True
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            increment = False
            break
        if numbers[i] > numbers[i-1]:
            increasing = True
        if numbers[i] < numbers[i-1]:
            decreasing = True
        if abs(numbers[i] - numbers[i-1]) > 3:
            increment = False
            break
        if increasing and decreasing:
            increment = False
            break
    if increment:
        safe_count += 1

print(safe_count)


with open('input.txt', 'r') as f:
    lines = f.readlines()

safe_count = 0

for line in lines:
    numbers = list(map(int, line.strip().split()))
    decreasing = False
    increasing = False
    increment = True
    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i-1]:
            increment = False
            break
        if numbers[i] > numbers[i-1]:
            increasing = True
        if numbers[i] < numbers[i-1]:
            decreasing = True
        if abs(numbers[i] - numbers[i-1]) > 3:
            increment = False
            break
        if increasing and decreasing:
            increment = False
            break
    if increment:
        safe_count += 1
    else:
        num_count = len(numbers)
        for i in range(0, num_count):
            # create a new list with the ith element removed
            new_numbers = numbers[:i] + numbers[i+1:]
            decreasing = False
            increasing = False
            increment = True
            for i in range(1, len(new_numbers)):
                if new_numbers[i] == new_numbers[i-1]:
                    increment = False
                    break
                if new_numbers[i] > new_numbers[i-1]:
                    increasing = True
                if new_numbers[i] < new_numbers[i-1]:
                    decreasing = True
                if abs(new_numbers[i] - new_numbers[i-1]) > 3:
                    increment = False
                    break
                if increasing and decreasing:
                    increment = False
                    break
            if increment:
                safe_count += 1
                break

print(safe_count)


