import re

pat = re.compile(r'(\d+)-(\d+) (\w): (\w+)')

valid = 0
for line in open('d2.txt', 'r'):
    matches = pat.match(line)
    min, max, char, pwd = matches.groups()
    min, max = int(min), int(max)
    if (pwd[min-1] + pwd[max-1]).count(char) == 1:
        valid += 1
print(valid)