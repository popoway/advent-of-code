'''
read of lines from input.txt that formats like:

47|53
97|13
97|61
97|47
75|29
61|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47

The first section specifies the page ordering rules, one per line. The first rule, 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53. (47 doesn't necessarily need to be immediately before 53; other pages are allowed to be between them.)

The second section specifies the page numbers of each update. Because most safety manuals are different, the pages needed in the updates are different too. The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.
'''

# an 2D list that specifies the page numbers of each update
input = []

# dict to store the page ordering rules
rule = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if '|' in line:
            a, b = line.strip().split('|')
            # if the page ordering rule is already in the dict, append the new page number to the existing list
            if a in rule:
                rule[a].append(b)
            # if the page ordering rule is not in the dict, create a new list
            else:
                rule[a] = [b]
        elif ',' in line:
            input.append(line.strip().split(','))
        else:
            continue

# print the page ordering rules
# print(rule)

# for each update, check if the page ordering rules are not satisfied
# if not satisfied, do not add the update to the answer list
# if satisfied, add the update to the answer list

answer = []
incorrect_answer = []

for update in input:
    is_incorrect = False
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in rule and update[i] in rule[update[j]]:
                incorrect_answer.append(update)
                is_incorrect = True
                break
        if is_incorrect:
            break
    if not is_incorrect:
        answer.append(update)
    
    # Alternative way to check if the page ordering rules are not satisfied, without using the is_incorrect variable
    # for i in range(len(update)):
    #     for j in range(i+1, len(update)):
    #         if update[j] in rule and update[i] in rule[update[j]]:
    #             incorrect_answer.append(update)
    #             break
    #     else:
    #         continue
    #     break
    # else:
    #     answer.append(update)

# print the answer list
for update in answer:
    print(','.join(update))

sum = 0
# find the sum of middle page numbers for each update
# (amount of middle page numbers is always odd)
for update in answer:
    # find the middle page number
    sum += int(update[len(update)//2])

print(sum)

# --- Part Two ---

# print the incorrect answer list
# for update in incorrect_answer:
#     print(','.join(update))

# For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order.
for update in incorrect_answer:
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[j] in rule and update[i] in rule[update[j]]:
                update[i], update[j] = update[j], update[i]
    print(','.join(update))

sum = 0
# find the sum of middle page numbers for each update
# (amount of middle page numbers is always odd)
for update in incorrect_answer:
    # find the middle page number
    sum += int(update[len(update)//2])

print(sum)