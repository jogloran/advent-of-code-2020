from bisect import insort, bisect_left
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

rom = list(map(str.rstrip, open('d8.txt')))
pc = 0
a = 0
visited = []

while True:
    if index(visited, pc) != -1: 
        print(a)
        break

    insort(visited, pc)
    op, arg = rom[pc].split(' '); arg = int(arg)
    if op == 'acc':
        a += arg
    elif op == 'jmp':
        pc += arg
        continue
    
    pc += 1