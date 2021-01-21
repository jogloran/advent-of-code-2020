rom = list(map(str.rstrip, open('d8.txt')))

def run(rom, patch):
    pc = 0
    a = 0
    nsteps = 0
    while pc < len(rom) and nsteps < len(rom):
        nsteps += 1
        op, arg = rom[pc].split(' '); arg = int(arg)
        if pc == patch:
            if op == 'jmp': op = 'nop'
            elif op == 'nop': op = 'jmp'
        # print(f'{pc:4} ({a:3}): {op} {arg}')
        if op == 'acc':
            a += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
            continue
        elif op == 'nop':
            pc += 1

    return pc == len(rom), a

for cur_pc, line in enumerate(rom):
    terminated, a = run(rom, patch=cur_pc)
    if terminated:
        print(f'found {cur_pc} {a}')
        break