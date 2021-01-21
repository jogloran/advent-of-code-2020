from more_itertools import split_at
grps = split_at(map(str.rstrip, open('d22.txt')), pred=lambda e: e == '')
grps = list(grps)
grp1 = list(map(int, grps[0][1:]))
grp2 = list(map(int, grps[1][1:]))

while grp1 and grp2:
    if grp1[0] < grp2[0]:
        # p2 wins
        grp2.append(grp2[0])
        grp2.append(grp1[0])
    else:
        # p1 wins
        grp1.append(grp1[0])
        grp1.append(grp2[0])
    del grp1[0]
    del grp2[0]

winner = grp2 if not grp1 else grp1
print(sum((len(winner) - pos) * val for pos, val in enumerate(winner)))