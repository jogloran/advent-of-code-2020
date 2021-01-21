import sys; from more_itertools import windowed, first_true
orig_data = list(map(int, open('d9.txt')))
data = orig_data[:]
target = 32321523
for i, e in enumerate(data):
    if i == 0: continue
    data[i] = data[i - 1] + data[i]

for i in range(len(data)):
    for j in range(i):
        if data[i] - data[j] == target:
            print(j, i, 'inclusive')
            print(min(orig_data[j:i+1]) + max(orig_data[j:i+1]))
            sys.exit()