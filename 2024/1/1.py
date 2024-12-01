'''
read 2 pairs of integers from input.txt that formats like:
17633   15737
79440   47531
'''
with open('input.txt', 'r') as f:
    lines = f.readlines()

a = []
b = []

for line in lines:
    a.append(int(line.split()[0]))
    b.append(int(line.split()[1]))

# sort a and b
a.sort()
b.sort()

total_distance = 0
for i in range(len(a)):
    total_distance += abs(a[i] - b[i])

print(total_distance)

total_similarity_score = 0

for i in range(len(a)):
    occurrence = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            occurrence += 1
    total_similarity_score += occurrence * a[i]

print(total_similarity_score)