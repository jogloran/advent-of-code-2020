import math
import numpy as np

f = open("d13.txt")
timestamp = int(next(f))
buses = [(i, int(e)) for i, e in enumerate(next(f).split(",")) if e != "x"]
print(buses)


def gcd(a, b):
    x_, x = 1, 0
    y_, y = 0, 1
    while b:
        q = a // b
        x, x_ = x_ - q * x, x
        y, y_ = y_ - q * y, y
        a, b = b, a % b
    return a, x_, y_


# buses = [(0, 7), (1,13), (4,59), ( 6,31), ( 7,19)]
buses = [(-a % b, b) for a, b in buses]
print(buses)

from functools import reduce
import operator


def mul(L, key):
    return reduce(operator.mul, map(key, L), 1)

# Chinese remainder theorem
N = mul(buses, key=lambda v: v[1])
a = [buses[i][0] for i in range(len(buses))]
n = [buses[i][1] for i in range(len(buses))]

y = [N // n_i for n_i in n]
z = [gcd(y_i, n_i)[1] for (y_i, n_i) in zip(y, n)]
x = [a_i * y_i * z_i for (a_i, y_i, z_i) in zip(a, y, z)]

print(sum(x) % N)