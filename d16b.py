import re
import numpy as np
from functools import partial, reduce
from operator import mul

valid_for = []
f = open('d16f.txt')
for i, line in enumerate(f):
    groups = re.match(r'([^:])+: (\d+)-(\d+) or (\d+)-(\d+)', line)
    if not groups: break

    field, *vals = groups.groups()
    a, b, c, d = map(int, vals)
    valid_for.append(partial(lambda v,a,b,c,d: 
        ((v >= a) & (v <= b)) | ((v >= c) & (v <= d)),
        a=a,b=b,c=c,d=d))

# gather data into table
data = np.loadtxt('d16b.txt', dtype=int, delimiter=',')

consts = [None] * 20
for j, column in enumerate(data.T):
    fields = [i for i in range(20) if np.all(valid_for[i](column))]
    
    print('column', j, 'consistent with', fields)
    consts[j] = fields

def argmin(L, key):
    best_value = 1 << 32
    best_index = -1
    for i, e in enumerate(L):
        if key(e) < best_value and key(e) > 0:
            best_index = i
            best_value = key(e)
    return best_index

def elim(consts, val):
    for vals in consts:
        if val in vals:
            vals.remove(val)

def deduce(consts):
    # start with const c => fs which has fewest elements,
    # assign c => fs
    solution = {}
    while len(solution) < 20:
        best_index = argmin(consts, key=len)
        print(f'best index: {best_index}')
        if len(consts[best_index]) == 1:
            solution[best_index] = consts[best_index][0]
            elim(consts, solution[best_index])
    return solution
        
        
soln = deduce(consts)
print(soln)