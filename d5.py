def seat_id(line):
    row = int(''.join('0' if c == "F" else '1' for c in line[:7]), 2)
    col = int(''.join('1' if c == "R" else '0' for c in line[7:]), 2)
    return row*8+col
print(max(seat_id(line) for line in map(str.rstrip, open('d5.txt'))))