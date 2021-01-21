from more_itertools import windowed, first_true
data = map(int, open('d9.txt'))
windowed_data = windowed(data, 26)
def sum2(window, target):
    return all(e1 + e2 != target for e1 in window for e2 in window)
def pred(datum):
    *window, target = datum
    return sum2(window, target)
print(first_true(windowed_data, pred=pred)[-1])