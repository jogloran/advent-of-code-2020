import re

class N(object):
    def __init__(self, n):
        self.n = n
    def __truediv__(self, other):
        return N(self.n + other.n)
    def __add__(self, other):
        return N(self.n * other.n)
def evaluate(line):
    line = line.replace('+', '/').replace('*', '+')
    line = re.sub(r'(\d+)', r'N(\1)', line)
    return eval(line).n

print(evaluate('1+2*3+4*5+6'))
s = 0
for line in map(str.rstrip, open('d18.txt')):
    s += evaluate(line)
print(s)
    
