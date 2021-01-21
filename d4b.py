from more_itertools import *
import re
def validate_hgt(v):
    try:
        if v.endswith('cm'):
            return 150 <= int(v[:-2]) <= 193
        elif v.endswith('in'):
            return 59 <= int(v[:-2]) <= 76
    except ValueError:
        pass
    return False
validator = {
"byr": lambda v: 1920 <= int(v) <= 2002,
"iyr": lambda v: 2010 <= int(v) <= 2020,
"eyr": lambda v: 2020 <= int(v) <= 2030,
"hgt": validate_hgt,
"hcl": lambda v: re.match(r'#[0-9a-f]{6}$', v) is not None,
"ecl": lambda v: v in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
"pid": lambda v: re.match(r'\d{9}$', v) is not None
# "cid",
}

def validated(fields):
    for f, v in fields.items():
        if f in validator:
            val = validator[f]
            print(f, v, val(v))
            if not val(v):
                return False
    return True

valid = 0
lines = open('d4.txt')
for grp in split_at(lines, lambda e: e == '\n'):
    g = ' '.join(map(str.rstrip, grp))
    if not all((f+':') in g for f in validator.keys()):
        continue
    fields = dict(bits.split(':') for bits in g.split(' '))
    cur_valid = True
    if validated(fields):
        valid += 1
    
print(valid)