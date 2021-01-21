from copy import copy
grid = {}

for y, line in enumerate(map(str.rstrip, open('d17.txt'))):
    for x, c in enumerate(line):
        if c == '#':
            grid[(x, y, 0)] = 1

print(grid)

def neighbours(x, y, z):
    return sum(
        int((x + dx, y + dy, z + dz) in grid)
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        for dz in [-1, 0, 1]
        if not (dx == 0 and dy == 0 and dz == 0))

# step
def step():
    global grid
    grid_ = copy(grid)
    for (x, y, z), v in grid.items():
        if v == 0: continue
        
        nbs = neighbours(x, y, z)
        # print(f'nbs({x} {y} {z}) = {nbs}')
        if not (nbs == 2 or nbs == 3):
            del grid_[(x, y, z)]
        
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                for dz in [-1, 0, 1]:
                    if (x + dx, y + dy, z + dz) not in grid:
                        nbs = neighbours(x + dx, y + dy, z + dz)
                        if nbs == 3:
                            # print(f'adding {x+dx} {y+dy} {z+dz}')
                            grid_[(x + dx, y + dy, z + dz)] = 1

    grid = grid_

for _ in range(6):
    step()
    print(grid)
print(len(grid))