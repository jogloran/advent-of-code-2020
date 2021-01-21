from more_itertools import split_at, distinct_combinations
import numpy as np
np.core.arrayprint._line_width = 160
from collections import Counter

def convert(row):
    return [1 if c == "#" else 0 for c in row]

def to_sig(row):
    return row.dot(2**np.arange(row.size)[::-1])

signatures = {}
signatures_f = {}
all_sigs = Counter()

class Tile:
    def __init__(self, tile_id, bitmap, ori):
        self.tile_id = tile_id
        self.bitmap = bitmap
        self.ori = ori

    def choices(self):
        yield self.bitmap
        yield np.rot90(self.bitmap)
        yield np.rot90(self.bitmap, 2)
        yield np.rot90(self.bitmap, 3)
        yield np.fliplr(self.bitmap)
        yield np.rot90(np.fliplr(self.bitmap))
        yield np.rot90(np.fliplr(self.bitmap), 2)
        yield np.rot90(np.fliplr(self.bitmap), 3)

    def __repr__(self): return '% 4s(%d)' % (self.tile_id, self.ori)

from collections import Counter
all_sigs = Counter()
tiles = {}
for grp in split_at(map(str.rstrip, open("d20.txt")), lambda e: e == ""):
    tile_id = int(grp[0][-5:-1])
    bitmap = np.array([convert(row) for row in grp[1:]])

    tiles[tile_id] = Tile(tile_id, bitmap, 0)

corners = [
    (3539, 0), # top left
    (2693, 2), # top right
    (1549, 0), # bottom right
    (3709, 0), # bottom left
]

UP, RIGHT = 0, 1
def compatible(a1, a2, dir):
    if dir == RIGHT:
        return np.all(a1[:, -1] == a2[:, 0])
    elif dir == UP:
        return np.all(a1[-1, :] == a2[0, :])

def find_compatible(left_tile, dir=RIGHT):
    for tile in tiles.values():
        if tile.tile_id == left_tile.tile_id: continue

        for j, choice in enumerate(tile.choices()):
            if compatible(left_tile.bitmap, choice, dir=dir):
                # print(f'{left_tile.tile_id} {left_tile.bitmap[:, -1]} compatible with {tile.tile_id} {choice[:, 0]}')
                yield choice, tile.tile_id, j

    # return None, -1

solution = np.empty((12, 12), dtype=np.object)
solution[0, 0] = tiles[3539]
solution[-1, 0] = tiles[3709]
# solution[0, -1] = tiles[2693].rotate(2)
# solution[-1, -1] = tiles[1549]
disallowed = {3539, 3709}
i = 1

for i in range(1, 12):
    for tile in tiles.values():
        if tile.tile_id in disallowed: continue

        compats = list(find_compatible(solution[0, i-1]))
        if compats:
            found_compatible, tile_id, j = compats[0]
            solution[0, i] = Tile(tile_id, found_compatible, j)
            disallowed.add(tile_id)
            break

for j in range(1, 12):
    for i in range(0, 12):
        for tile in tiles.values():
            if tile.tile_id in disallowed: continue

            compats = list(find_compatible(solution[j-1, i], dir=UP))
            if compats:
                found_compatible, tile_id, k = compats[0]
                solution[j, i] = Tile(tile_id, found_compatible, k)
                disallowed.add(tile_id)
                break

print(np.array2string(solution, max_line_width=np.inf))

solution_matrix = np.stack((e.bitmap for e in solution.ravel())) # (144, 10, 10)
unframed = solution_matrix[:, 1:-1, 1:-1].reshape((12, 12, 8, 8))
print(unframed.shape) # (12, 12, 8, 8)

image = np.zeros((96, 96), dtype=np.int)
for row in range(12):
    for col in range(12):
        image[8*row:8*(row+1), 8*col:8*(col+1)] = unframed[row, col]

np.save('image.npy', image)
# import matplotlib.pyplot as plt
# plt.figure()
# f, ar = plt.subplots(2)
# ar[0].imshow(image)
# ar[1].imshow(solution[0, -1].bitmap)
# plt.show()