from more_itertools import *
fields = {
"byr",
"iyr",
"eyr",
"hgt",
"hcl",
"ecl",
"pid",
# "cid",
}
valid = 0
lines = open('d4.txt')
for grp in split_at(lines, lambda e: e == '\n'):
    g = ' '.join(map(str.rstrip, grp))
    if (all((f+':') in g for f in fields)):
        valid += 1
print(valid)