from more_itertools import *

v = 0
for grp in split_at(open('d6.txt'), lambda e: e == '\n'):
    all_chars = ''.join(map(str.rstrip, grp))
    v += len(set(all_chars))
print(v)