cups = list('389125467')
cups = list(map(int, cups))# + list(range(len(cups), 1000000 + 1))

max_index = max(cups)

cur_index = -1

def remove_slice(L, start, end):
    result = []
    N = len(L)
    for i in range(start, end):
        result.append(L[i % N])

    if end > N:
        del L[start:]
        del L[:(end % N)]
    else:
        del L[start:end]

    return result

def get_dest(L, cur):
    # max_index = max(L)
    cur -= 1
    if cur < 0: cur = max_index
    while True:
        if cur in L: return L.index(cur)

        cur -= 1
        if cur < 0: cur = max_index


def insert_at(cups, cur, pickup):
    cups[cur:cur] = pickup

for round in range(1000000):
    if cur_index != -1:
        cur_index = (cups.index(cur) + 1) % len(cups)
    else:
        cur_index = 0
    cur = cups[cur_index]
    pickup = remove_slice(cups, cur_index + 1, cur_index + 4)
    print('after remove:', cups)
    dest_idx = get_dest(cups, cur)
    # print(str(cur_index) + " ", end='')
    # cur_index is periodic with cycle length 242
    insert_at(cups, dest_idx + 1, pickup)
    print(f'{round:4} cur [{cur_index}] = {cur}, dest [{dest_idx}] {cups}')
print()
cup1_idx = cups.index(1)
print(cups[(cup1_idx - 1) % len(cups)])
print(cups[(cup1_idx - 2) % len(cups)])
