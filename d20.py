from more_itertools import split_at, distinct_combinations
import numpy as np
from collections import Counter

def convert(row):
    return [1 if c == "#" else 0 for c in row]

def to_sig(row):
    return row.dot(2**np.arange(row.size)[::-1])

signatures = {}
signatures_f = {}
all_sigs = Counter()
for grp in split_at(map(str.rstrip, open("d20.txt")), lambda e: e == ""):
    tile_id = int(grp[0][-5:-1])
    bitmap = np.array([convert(row) for row in grp[1:]])

    signatures[tile_id] = [
        to_sig(bitmap[0, :]), # l
        to_sig(bitmap[:, 0]), # t
        to_sig(bitmap[-1, :]), # r
        to_sig(bitmap[:, -1]), # b
    ]
    signatures[-tile_id] = [
        to_sig(bitmap[0, :][::-1]),
        to_sig(bitmap[:, 0][::-1]),
        to_sig(bitmap[-1, :][::-1]),
        to_sig(bitmap[:, -1][::-1]),
    ]
    
    all_sigs.update(signatures[tile_id])
    all_sigs.update(signatures[-tile_id])

print(signatures)
def solve():
    # start with a corner tile
    # as a heuristic, find the pair of tiles with the largest pairwise intersection and start with those
    best = None
    nmatches = 0
    for id1, i in signatures.items():
        for id2, j in signatures.items():
            if id1 == id2: continue
            isect = set(i) & set(j) 
            if len(isect) > nmatches:
                best = (id1, id2)
                nmatches = len(isect)
    print(best, nmatches)
    # probably needs exhaustive search

def solve2():
    for centre_id, centre in signatures.items():
        print('considering', centre_id)
        best = None
        nmatches = 0
        for combo in distinct_combinations(signatures.items(), 4):
            ids = [e[0] for e in combo]
            if centre_id in ids: continue
            if any(e in ids and -e in ids for e in ids): continue
            if any(e == -centre_id for e in ids): continue
            sets = [set(e[1]) for e in combo]
            isecs = [set.intersection(set(centre), s) for s in sets]
            if len(max(isecs, key=len)) > nmatches:
                best = [e[0] for e in combo]
                nmatches = len(isecs)
        print('centre', centre_id, best, nmatches)

def solve3():
    for id1, i in signatures.items():
        # If an edge isn't found anywhere else in another tile, then it's on the border
        nbord = 0
        untouched_edges = []
        for edge_idx, sig in enumerate(i):
            if all_sigs[sig] == 1:
                nbord += 1
                untouched_edges.append(edge_idx)
        if nbord == 2:
            print(f'tile {id1} border edges {nbord} indices {untouched_edges}')

print(all_sigs)
solve3()

print(signatures[3539])

# to solve a row
# start with the leftmost (remove it from consideration)
# look at signature index 2 (R direction)
# find another tile containing that signature
# rotate it so that the signature is in position 0 (L), remove it from consideration
#   (remember the rotation)
# do this for the entire row

def tile_with_signature(seeking, disallowed):
    for id, sig in signatures.items():
        if id in disallowed: continue
        if seeking in sig: yield id

def rotations_such_that(tile, seeking):
    sigs = signatures[tile]
    return sigs.index(seeking)

def solve_row(leftmost, starting_rot):
    solution = [(leftmost, starting_rot)]
    disallowed = {leftmost}
    tile = leftmost
    while len(solution) < 12:
        print('>',solution)
        sigs = signatures[tile]
        seeking = sigs[(starting_rot + 2) % 4]
        print(f'looking for tiles containing {seeking}')
        # find another tile containing the signature "seeking"
        candidate_tiles = list(tile_with_signature(seeking, disallowed))
        print('cands',candidate_tiles)
        tile = candidate_tiles[0]
        print(f'found {tile} {signatures[tile]}')
        starting_rot = rotations_such_that(tile, seeking)
        solution.append((tile, starting_rot))
        disallowed.add(tile)

    return solution

# sol = solve_row(leftmost=3709, starting_rot=0)
# print(sol)
# sol = solve_row(leftmost=2693, starting_rot=2)
# print(sol)

tile_id = 2693
starting_rot = 2
for i in range(12):
    print(i, 'solve_row(', tile_id, ',', starting_rot, ')')
    sol = solve_row(leftmost=tile_id, starting_rot=starting_rot)
    print(i, sol)
    first_tile_id, first_rot = sol[0]
    print('signatures', signatures[first_tile_id])
    seeking = signatures[first_tile_id][(first_rot + 2) % 4]
    print('seeking', seeking)
    cand = list(tile_with_signature(seeking, {e[0] for e in sol}))
    rot = rotations_such_that(cand[0], seeking)

    tile_id = cand[0]
    starting_rot = rot

# find top-left of next row
# print(signatures[2693][0])
# print(list(tile_with_signature(480, {2693})))

# sol = solve_row(leftmost=1571, starting_rot=3)
# print(sol)