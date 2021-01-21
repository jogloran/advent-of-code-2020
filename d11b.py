import numpy as np

def munge(line): return ' '.join('1.0' if c == 'L' else '0.0' for c in line.rstrip())
d = np.loadtxt(munge(line) for line in open('d11.txt')).astype(np.int)
floor = d == 0.0

n = np.zeros_like(d)
def calculate_neighbours():
    n.fill(0)
    r, c = d.shape
    for j in range(r):
        for i in range(c):
            for k in [(-1, -1), (-1, 0), (-1, +1),
                      ( 0, +1), (+1, +1), (+1, 0),
                      (+1, -1), (0, -1)]:
                n[j, i] += occupied(j, i, k, c, r)
    return n

def occupied(j, i, k, c, r):
    # d[j, i] = 1 denotes occupied
    # d[j, i] = 0 denotes floor or unoccupied
    dx, dy = k
    j += dy # skip over the current tile (j,i) itself
    i += dx
    while 0 <= j < r and 0 <= i < c:
        if d[j, i] == 1:
            return 1
        # not occupied and not floor => unoccupied seat
        if d[j, i] == 0 and not floor[j, i]:
            return 0
        j += dy
        i += dx
    return 0

while True:
    neighbours = calculate_neighbours()
    d_ = np.copy(d)
    d_[neighbours >= 5] = 0
    d_[neighbours == 0] = 1
    d_[floor] = 0
    if np.all(d == d_):
        print('stable')
        break
    d = d_
print(np.sum(d))