def seat_id(line):
    row = int(''.join('0' if c == "F" else '1' for c in line[:7]), 2)
    col = int(''.join('1' if c == "R" else '0' for c in line[7:]), 2)
    return row*8+col
all_ids = sorted(list(seat_id(line) - 8 for line in map(str.rstrip, open('d5.txt'))))
for i, e in enumerate(all_ids):
    if i != e:
        print(i + 8)
        break