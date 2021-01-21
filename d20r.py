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

class Tile:
    def __init__(self, tile_id, rot, flipped):
        self.tile_id = tile_id
        self.rot = rot
        self.flipped = flipped

    def __repr__(self): return '% 4d@%d%s' % (self.tile_id, self.rot, 'f' if self.flipped else '')

from collections import Counter
all_sigs = Counter()
tiles = {}
for grp in split_at(map(str.rstrip, open("d20.txt")), lambda e: e == ""):
    tile_id = int(grp[0][-5:-1])
    bitmap = np.array([convert(row) for row in grp[1:]])

    # signatures maps from a sig value to a Tile configuration consistent with that value
    sigs = (to_sig(bitmap[0, :]), # l
        to_sig(bitmap[:, 0]), # t
        to_sig(bitmap[-1, :]), # r
        to_sig(bitmap[:, -1]), # b
        to_sig(bitmap[0, :][::-1]), # l'
        to_sig(bitmap[:, 0][::-1]), # t'
        to_sig(bitmap[-1, :][::-1]), # r'
        to_sig(bitmap[:, -1][::-1])) # b'
    for i, sig in enumerate(sigs):
        signatures[sig] = Tile(tile_id, )

corners = [
    (3539, 0), # top left
    (2693, 2), # top right
    (1549, 0), # bottom right
    (3709, 0), # bottom left
]

solution = np.empty((12, 12), dtype=np.object)
solution[0, 0] = tiles[3539]
solution[0, -1] = tiles[2693].rotate(2)
solution[-1, 0] = tiles[3709]
solution[-1, -1] = tiles[1549]
print(solution)

