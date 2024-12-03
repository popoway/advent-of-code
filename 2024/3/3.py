'''
read of lines from input.txt that formats like:
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
'''

sum = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()
    # for each line, find all matches of mul(a,b) where a and b are each 1-3 digit numbers
    for line in lines:
        import re
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        for match in matches:
            a, b = map(int, match)
            sum += a * b

print(sum)


'''
The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
'''

sum = 0
mul_enabled = True

with open('input.txt', 'r') as f:
    lines = f.readlines()
    # for each line, find all matches of 
    # do()
    # don't()
    # mul(a,b) where a and b are each 1-3 digit numbers 
    # in the same order as they appear in the line
    for line in lines:
        import re
        matches = re.findall(r'((mul)\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))', line)
        '''
        ('mul(2,4)', 'mul', '2', '4', '', '')
        ('', '', '', '', '', "don't()")
        ('mul(5,5)', 'mul', '5', '5', '', '')
        ('mul(11,8)', 'mul', '11', '8', '', '')
        ('', '', '', '', 'do()', '')
        ('mul(8,5)', 'mul', '8', '5', '', '')
        '''
        for match in matches:
            # print(match)
            if match[1] == 'mul' and mul_enabled:
                a, b = map(int, match[2:4])
                sum += a * b
            elif match[4] == 'do()':
                mul_enabled = True
            elif match[5] == 'don\'t()':
                mul_enabled = False

print(sum)