import numpy as np
from scipy.signal import convolve2d

def munge(line): return ' '.join('1.0' if c == 'L' else '0.0' for c in line.rstrip())
d = np.loadtxt(munge(line) for line in open('d11.txt')).astype(np.int)
floor = d == 0.0
kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
while True:
    neighbours = convolve2d(d, kernel, mode='same')
    d_ = np.copy(d)
    d_[neighbours >= 4] = 0
    d_[neighbours == 0] = 1
    d_[floor] = 0
    if np.all(d == d_):
        print('stable')
        break
    d = d_
print(np.sum(d))