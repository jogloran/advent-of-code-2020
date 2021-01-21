from more_itertools import *
import functools
v = 0
for grp in split_at(open('d6.txt'), lambda e: e == '\n'):
    d = map(set, map(str.rstrip, grp))
    s = set.intersection(*d)
    v += len(s)
print(v)