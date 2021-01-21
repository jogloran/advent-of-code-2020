import operator
import functools
lines = list(map(str.rstrip, open('d3.txt', 'r')))
width = len(lines[0])

def f(x_inc, y_inc):
    i = 0
    tree = 0
    for y, line in enumerate(lines):
        if y % y_inc != 0: continue
        if line[i % width] == '#':
            tree += 1
        i += x_inc
    return tree
print(f(1,1)*f(3,1)*f(5,1)*f(7,1)*f(1,2))