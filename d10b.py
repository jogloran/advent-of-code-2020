import numpy as np

jolts = list(map(int, map(str.rstrip, open('d10.txt'))))
jolts.sort()
jolts.insert(0, 0)
jolts.append(jolts[-1] + 3)

memo = {}

def compute(L, key=0):
    if len(L) <= 1: return 1
    if key in memo: 
        return memo[key]

    head, *rest = L
    candidates = [r for r in rest if r - head <= 3]
    value = sum(compute(L[L.index(cand):], key + L.index(cand)) for cand in candidates)
    memo[key] = value
    return value

_ = compute(jolts)
print(_)