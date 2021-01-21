import re
from more_itertools import powerset

Xpos = 0
mask = 0

mem = {}

def interpret_mask(spec):
    global Xpos, mask
    mask = int(spec.replace('X', '0'), 2)
    Xpos = int(spec.replace('1', '0').replace('X', '1'), 2)

def gen_fseq(Xpos):
    # wherever 1 is set in Xpos, that is a position which has to vary
    # e.g. Xpos = 0b10101
    # we need to generate 8 possibilities:
    # 10101, 10100, 10001, 10000, 00101, 00100, 00001, 00000
    set_bits = []
    for i in range(36):
        if Xpos & (1 << i): set_bits.append(i)
    
    def to_set_bits(combo):
        s = 0
        for c in combo:
            s |= 1 << c
        return s

    for combo in powerset(set_bits):
        yield to_set_bits(combo)

pat = re.compile(r'mem\[(\d+)\] = (\d+)')
for line in map(str.rstrip, open('d14.txt')):
    if line.startswith('mask = '):
        mask = line[7:]
        interpret_mask(mask)
    else:
        groups = pat.match(line).groups()
        loc, val = map(int, groups)
        masked = (loc & ~Xpos) | mask
        for fseq in gen_fseq(Xpos):
            mem[masked | fseq] = val

print(sum(mem.values()))