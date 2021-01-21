start = [8,13,1,0,18,9]

last_said = None
history = {}

def say(num, turn_no):
    print(f'turn {i}\tsay {num}')

for i in range(30000000):
    if i < len(start):
        num = start[i]
    else:
        # print(f'turn {i}  last said {last_said} {history}')
        if last_said in history:
            # print('in')
            num = i - history[last_said] - 1
        else:
            num = 0
        # print(history)

    if last_said is not None:
        history[last_said] = i - 1
    # say(num, i)
    if i % 1000000 == 0: print(i, num)
    last_said = num
print(i, num)