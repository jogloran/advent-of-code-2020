jolts = list(map(int, map(str.rstrip, open('d10.txt'))))
jolts.sort()
jolts.insert(0, 0)

diffs = [b - a for (a, b) in zip(jolts, jolts[1:])]
print(diffs.count(1))
print(diffs.count(3) + 1)