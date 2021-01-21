import numpy as np
import matplotlib.pyplot as plt
import sys
np.set_printoptions(threshold=sys.maxsize)
np.set_printoptions(edgeitems=30, linewidth=100000, 
    formatter=dict(float=lambda x: "%.3g" % x))
data = np.load('image.npy')

pat = np.array([0 if c == " " else 1 for c in 
'''                  # #    ##    ##    ### #  #  #  #  #  #   '''.lstrip('\n')]).reshape((3, 20))

def choices(b):
    yield b
    yield np.rot90(b)
    yield np.rot90(b, 2)
    yield np.rot90(b, 3)
    yield np.fliplr(b)
    yield np.rot90(np.fliplr(b))
    yield np.rot90(np.fliplr(b), 2)
    yield np.rot90(np.fliplr(b), 3)

from skimage.util import view_as_windows

for k, choice in enumerate(choices(data)):
    windows = view_as_windows(choice, (3, 20))
    for j, row in enumerate(windows):
        for i, win in enumerate(row):
            if np.all((win & pat) == pat):
                print(f'{k} found at {j},{i}')
                win[(win == 1) & (pat == 1)] = 2

print(np.sum(data == 1))
