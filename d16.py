import re
x = [False] * 1000
f = open('d16.txt')
for line in f:
    groups = re.match(r'[^:]+: (\d+)-(\d+) or (\d+)-(\d+)', line)
    if not groups: break

    a, b, c, d = map(int, groups.groups())
    for i in range(a, b+1):
        x[i] = True
    for i in range(c, d+1):
        x[i] = True

next(f)
next(f)
next(f)
next(f)

err = 0 
with open('d16b.txt', 'w') as out:
    for fields in f:
        valid = True
        bits = map(int, fields.split(','))
        for bit in bits:
            if not x[bit]: 
                valid = False
                err += bit
        if valid:
            out.write(fields)

print(err)