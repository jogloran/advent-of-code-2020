import re
from collections import defaultdict
next_id = 0
def id_updater():
    global next_id
    next_id += 1
    return next_id - 1
bag_id = defaultdict(id_updater)

graph = defaultdict(set)

pat = re.compile(r'(\w+ \w+) bags contain (.+).')
bag = re.compile(r'(\d+) (\w+ \w+) bags?')
for line in open('d7.txt'):
    match = pat.findall(line)
    if not match: continue
    lhs, rhs = match[0]
    lhs_id = bag_id[lhs]
    if rhs == 'no other bags':
        graph[lhs_id] = set()
    else:
        def transform(tup): return (int(tup[0]), bag_id[tup[1]])
        bits = [transform(bag.findall(bit)[0]) for bit in rhs.split(', ')]
        # graph[lhs_id] = bits
        for quantity, rhs_id in bits:
            graph[rhs_id].add(lhs_id)

def dfs(src_id):
    visited = set()
    stk = [src_id]
    while stk:
        node = stk.pop(0)
        if node in visited: continue

        visited.add(node)
        for neighbour_id in graph[node]:
            stk.append(neighbour_id)
    return visited

visited = dfs(bag_id['shiny gold'])
print(len(visited) - 1)