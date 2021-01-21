cups = list('463528179')
cups = list(map(int, cups))

cur_index = -1

def remove_slice(L, start, end):
    result = []
    for i in range(start, end):
        result.append(L[i % len(L)])
    # Removing a slice that goes off the end of the array
    # [1,2,3,4,5] remove_slice(3,6) should remove three elements 4,5,1
    while start < end:
        L[start % len(L)] = None
        start += 1
    try:
        while True:
            L.remove(None)
    except ValueError: pass

    return result

def get_dest(L, cur):
    max_index = max(L)
    cur -= 1
    if cur < 0: cur = max_index
    while True:
        if cur in L: return L.index(cur)

        cur -= 1
        if cur < 0: cur = max_index


def insert_at(cups, cur, pickup):
    cups[cur:cur] = pickup

for round in range(100):
    if cur_index != -1:
        cur_index = (cups.index(cur) + 1) % len(cups)
        print('looking for neighbour of value', cur, '-> index', cups.index(cur), 'value', cups[cur_index])
    else:
        cur_index = 0
    cur = cups[cur_index]
    print('before removing', cups)
    pickup = remove_slice(cups, cur_index + 1, cur_index + 4)
    print('after removing', cups)
    print('pickup', pickup, cups)
    dest_idx = get_dest(cups, cur)
    print('dest idx', dest_idx, 'value', cups[dest_idx])
    insert_at(cups, dest_idx + 1, pickup)
    print(round, cups)
    print()
