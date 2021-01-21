import re

Xpos = 0
mask = 0

mem = {}

def interpret_mask(spec):
    global Xpos, mask
    mask = int(spec.replace('X', '0'), 2)
    Xpos = int(spec.replace('1', '0').replace('X', '1'), 2)

pat = re.compile(r'mem\[(\d+)\] = (\d+)')
for line in map(str.rstrip, open('d14.txt')):
    if line.startswith('mask = '):
        mask = line[7:]
        interpret_mask(mask)
    else:
        groups = pat.match(line).groups()
        loc, val = map(int, groups)
        mem[loc] = (val & Xpos) | mask

print(sum(mem.values()))