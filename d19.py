import re
f = map(str.rstrip, open('d19.txt'))
prod3 = re.compile(r'(\d+): (\d+) (\d+) (\d+)')
prod2 = re.compile(r'(\d+): (\d+) \| (\d+)')
prod = re.compile(r'(\d+): (\d+)(?: (\d+)(?: \| (\d+) (\d+))?)?')
char = re.compile(r'(\d+): "(.)"')
rules = {}

class Prod:
    def __init__(self, rule_id, a, b):
        self.rule_id = rule_id
        self.a, self.b = a, b
    def __call__(self, s):
        ok, pos = rules[self.a](s)
        ok2, pos2 = rules[self.b](s[pos:])
        return ok and ok2, pos + pos2

class Prod3:
    def __init__(self, rule_id, a, b, c):
        self.rule_id = rule_id
        self.a, self.b, self.c = a, b, c
    def __call__(self, s):
        ok, pos = rules[self.a](s)
        if ok:
            ok2, pos2 = rules[self.b](s[pos:])
            if ok2:
                ok3, pos3 = rules[self.c](s[(pos + pos2):])
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
        if not ok:
            ok, pos = Prod('_', self.c, self.d)(s)
        return ok, pos


class Char:
    def __init__(self, rule_id, c):
        self.rule_id = rule_id
        self.c = c
    def __call__(self, s):
        try:
            ok = s.startswith(self.c)
            pos = s.index(self.c) + len(self.c)
            return ok, pos
        except ValueError:
            return False, -1   

def accepts0(s):
    ok, pos = rules['0'](s)
    return ok and pos >= len(s)

while True:
    line = next(f)
    if line == '': break

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

# # print(rules)
msgs = list(f)
accepts = 0
for msg in msgs:
    if accepts0(msg):
        accepts += 1

print(accepts, len(msgs))
