from copy import copy
grid = {}

for y, line in enumerate(map(str.rstrip, open('d17.txt'))):
    for x, c in enumerate(line):
        if c == '#':
            grid[(x, y, 0, 0)] = 1

print(grid)

def neighbours(x, y, z, w):
    return sum(
        int((x + dx, y + dy, z + dz, w + dw) in grid)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        for dz in [-1, 0, 1]
        for dw in [-1, 0, 1]
        if not (dx == 0 and dy == 0 and dz == 0 and dw == 0))

# step
def step():
    global grid
    grid_ = copy(grid)
    for (x, y, z, w), v in grid.items():
        if v == 0: continue
        
        nbs = neighbours(x, y, z, w)
        # print(f'nbs({x} {y} {z}) = {nbs}')
        if not (nbs == 2 or nbs == 3):
            del grid_[(x, y, z, w)]
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    for dw in [-1, 0, 1]:
                        if (x + dx, y + dy, z + dz, w + dw) not in grid:
                            nbs = neighbours(x + dx, y + dy, z + dz, w + dw)
                            if nbs == 3:
                                # print(f'adding {x+dx} {y+dy} {z+dz}')
                                grid_[(x + dx, y + dy, z + dz, w + dw)] = 1

    grid = grid_

for _ in range(6):
    step()
    print(grid)
print(len(grid))