import math
import numpy as np
f = open('d13.txt')
timestamp = int(next(f))
buses = [int(e) for e in next(f).split(',') if e != 'x']
L = [math.ceil(timestamp / p) * p for p in buses]
arg = np.argmin(L)
time_to_wait = min(L) - timestamp
print(buses[arg] * time_to_wait)