from itertools import count
from tqdm import tqdm

C_pk = 16915772
D_pk = 18447943

C_key = None
D_key = None

found = 0
for e in tqdm(count(start=1)):
    v = pow(7, e, 20201227)
    if v == D_pk:
        print('D', e)
        found += 1
        C_key = e
        if found == 2: break
    if v == C_pk:
        print('C', e)
        found += 1
        D_key = e
        if found == 2: break

print(pow(7, C_key * D_key, 20201227))