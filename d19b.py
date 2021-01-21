import re
f = map(str.rstrip, open('d19b.txt'))
prod5 = re.compile(r'(\d+): (\d+) (\d+) \| (\d+) (\d+) (\d+)')
prod4 = re.compile(r'(\d+): (\d+) \| (\d+) (\d+)')
prod3 = re.compile(r'(\d+): (\d+) (\d+) (\d+)')
prod2 = re.compile(r'(\d+): (\d+) \| (\d+)')
prod = re.compile(r'(\d+): (\d+)(?: (\d+)(?: \| (\d+) (\d+))?)?')
char = re.compile(r'(\d+): "(.)"')
rules = {}

class Plus:
    def __init__(self, rule_id, a):
        self.rule_id = rule_id
        self.a = Singleton("_", a)

    def __call__(self, s):
        at_least_one_ok, pos = self.a(s)
        last_pos = pos
        ok = True
        while ok and last_pos < len(s):
            print(ok, last_pos)
            ok, pos2 = self.a(s[last_pos:])
            if ok:
                last_pos += pos2
            else:
                break
        return at_least_one_ok, last_pos

class Prod5:
    def __init__(self, rule_id, a, b, c, d, e):
        self.rule_id = rule_id
        self.a, self.b, self.c, self.d, self.e = a, b, c, d, e
    def __call__(self, s):
        ok, pos = Prod('_', self.a, self.b)(s)
        if not ok:
            ok, pos = Prod3('_', self.c, self.d, self.e)(s)
        return ok, pos

class Prod4:
    def __init__(self, rule_id, a, b, c):
        self.rule_id = rule_id
        self.a, self.b, self.c = a, b, c
    def __call__(self, s):
        ok, pos = rules[self.a](s)
        if not ok:
            ok, pos = Prod('_', self.b, self.c)(s)
        return ok, pos

class Prod:
    def __init__(self, rule_id, a, b):
        self.rule_id = rule_id
        self.a, self.b = a, b
    def __call__(self, s):
        ok, pos = rules[self.a](s)
        # print(self, self.a, self.b, s, pos)
        ok2, pos2 = rules[self.b](s[pos:])
        return ok and ok2, pos + pos2

class Prod3:
    def __init__(self, rule_id, a, b, c):
        self.rule_id = rule_id
        self.a, self.b, self.c = a, b, c
    def __call__(self, s):
        ok, pos = rules[self.a](s)
        # print(self, self.a, self.b, s, pos)
        if ok:
            ok2, pos2 = rules[self.b](s[pos:])
            if ok2:
                ok3, pos3 = rules[self.c](s[(pos + pos2):])
                # print('X -> A B C', self.rule_id,'returning',ok,ok2,ok3, pos + pos2 + pos3)
                return ok3, pos + pos2 + pos3
        return False, -1

class Singleton:
    def __init__(self, rule_id, a):
        self.rule_id = rule_id
        self.a = a
    def __call__(self, s):
        return rules[self.a](s)

class OrProd1:
    def __init__(self, rule_id, a, b):
        self.rule_id = rule_id
        self.a, self.b = a, b
    def __call__(self, s):
        ok, pos = rules[self.a](s)
        if not ok:
            ok, pos = rules[self.b](s)
        return ok, pos

class OrProd:
    def __init__(self, rule_id, a, b, c, d):
        self.rule_id = rule_id
        self.a, self.b, self.c, self.d = a, b, c, d
    def __call__(self, s):
        ok, pos = Prod('_', self.a, self.b)(s)
        # print('X -> A B | C D', self.rule_id, '1', ok, pos, s)
        if not ok:
            ok, pos = Prod('_', self.c, self.d)(s)
            # print('X -> A B | C D', self.rule_id, '2', ok, pos, s)
        # print('X -> A B | C D', self.rule_id, 'returning',ok,pos)
        return ok, pos


class Char:
    def __init__(self, rule_id, c):
        self.rule_id = rule_id
        self.c = c
    def __call__(self, s):
        try:
            ok = s.startswith(self.c)
            pos = s.index(self.c) + len(self.c)
            # print('char', self.rule_id,'returning', ok,pos,s)
            return ok, pos
        except ValueError:
            return False, -1   

def accepts0(s):
    # at all split points
    # if any split point causes both sides to accept, then accept
    for i in range(1, len(s)-1):
        s1, s2 = s[:i], s[i:]
        print(f'testing split point {i} {s1=} {s2=}')
        
        cur = 0
        ok = True
        m = 0
        while cur < len(s1):
            ok, pos = rules['42'](s1[cur:])
            print(f'{ok=} {pos=} {s1[cur:]=}')
            if not ok: break
            m += 1
            cur += pos
        
        cur = 0
        ok2 = True
        n = 0
        while cur < len(s2):
            ok2, pos = rules['31'](s2[cur:])
            print(f'{ok2=} {pos=} {s2[cur:]=}')
            if not ok2: break
            n += 1
            cur += pos

        if ok and ok2 and m > n:
            return True
    return False

    # ok, pos = rules['0'](s)
    # print(s, ok, pos)
    # return ok and pos >= len(s)

while True:
    line = next(f)
    if line == '': break

    matches = prod5.match(line)
    if matches:
        X, a, b, c, d, e = matches.groups()
        rules[X] = Prod5(X, a, b, c, d, e)
        continue
    
    matches = prod4.match(line)
    if matches:
        X, a, b, c = matches.groups()
        rules[X] = Prod4(X, a, b, c)
        continue

    matches = prod3.match(line)
    if matches:
        X, a, b, c = matches.groups()
        rules[X] = Prod3(X, a, b, c)
        continue

    matches = prod2.match(line)
    if matches:
        X, a, b = matches.groups()
        rules[X] = OrProd1(X, a, b)
        continue

    matches = prod.match(line)
    if matches:
        X, a, b, c, d = matches.groups()
        if b is None:
            rules[X] = Singleton(X, a)
        elif c is None and d is None:
            rules[X] = Prod(X, a, b)
        else:
            rules[X] = OrProd(X, a, b, c, d)
    else:
        matches = char.match(line)
        X, ch = matches.groups()
        rules[X] = Char(X, ch)

# rules['8'] = Prod4('8', '42', '42', 'α')
# rules['α'] = Prod4('α', '42', '42', '42')
# rules['11'] = Prod5('11', '42', '31',  '42', 'β', '31')
# rules['β'] = Prod('β', '42', '31')

msgs = list(f)
accepts = 0
for msg in msgs:
    if accepts0(msg):
        accepts += 1

# 141 is too low
# 272 is incorrect
# 329 is too high
print(accepts, len(msgs)) # 253 is correct

# print(rules['4'])
# rules['998'] = Plus('998', '997')
# rules['997'] = OrProd1('997', '54', '117')
# print(rules['998']('abbab'))