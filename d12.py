x = y = 0
hx, hy = 1, 0
def mv(dx, dy):
    def _(value):
        global x, y
        x += value * dx
        y += value * dy
    return _
def rot90(clockwise):
    global hx, hy
    if clockwise: hx, hy = hy, -hx
    else: hx, hy = -hy, hx
def rot(clockwise):
    def _(deg):
        nrots = deg // 90
        for _ in range(nrots):
            rot90(clockwise)
    return _
def fwd(value):
    global x, y, hx, hy
    x += hx * value
    y += hy * value
hs = {
    'N': mv(dx=0, dy=1),
    'S': mv(dx=0, dy=-1),
    'E': mv(dx=1, dy=0),
    'W': mv(dx=-1, dy=0),
    'L': rot(clockwise=False),
    'R': rot(clockwise=True),
    'F': fwd,
}
for inst in map(str.rstrip, open('d12.txt')):
    cmd, arg = inst[0], int(inst[1:])
    hs[cmd](arg)
print(abs(x) + abs(y))