dirs = frozenset({"sw", "se", "nw", "ne"})
def segment(l):
    cur = 0
    while cur < len(l):
        if any(l[cur:].startswith(c) for c in dirs):
            yield l[cur:cur+2]
            cur += 2
        else:
            yield l[cur]
            cur += 1


cmds = {
    "e": lambda x, y: (x + 1, y),
    "w": lambda x, y: (x - 1, y),
    "ne": lambda x, y: (x, y + 1),
    "nw": lambda x, y: (x - 1, y + 1),
    "se": lambda x, y: (x + 1, y - 1),
    "sw": lambda x, y: (x, y - 1),
}


from collections import defaultdict, Counter

# false = white side up
grid = defaultdict(lambda: False)  # if something's not in the grid, it defaults to 0
ctr = Counter()
for line in map(str.rstrip, open("d24t.txt")):
    x, y = 0, 0
    for instr in segment(line):
        x, y = cmds[instr](x, y)
        # grid[(x, y)] = not grid[(x, y)]
    print(f'flipping {x} {y}: {grid[(x,y)]} -> {not grid[(x,y)]}')
    grid[(x, y)] = not grid[(x, y)]
    ctr[(x, y)] += 1
print(ctr)
print([g for g, is_black in grid.items() if is_black])
print(sum(e for e in grid.values() if e))