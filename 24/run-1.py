from time import time, sleep

# f = open('example1.txt')
f = open('input.txt')
data = list(map(lambda x: list(x.strip()), f.readlines()))
mem = []

def draw():
    for y in range(5):
        for x in range(5):
            print(data[y][x], end='')
        print()
    print()

def is_infested(x,y):
    if x < 0 or y < 0 or x > 4 or y > 4:
        return 0
    else:
        return 1 if data[y][x] == '#' else 0

draw()
while True:
    if data in mem:
        draw()
        break
    else:
        mem.append([[data[i][j] for j in range(5)] for i in range(5)])
    next_data = [[data[i][j] for j in range(5)] for i in range(5)]
    for y in range(5):
        for x in range(5):
            c_state = data[y][x]
            adj_bugs = 0
            adj_bugs += is_infested(x-1,y)
            adj_bugs += is_infested(x+1,y)
            adj_bugs += is_infested(x,y-1)
            adj_bugs += is_infested(x,y+1)
            if c_state == '#' and adj_bugs != 1:
                next_data[y][x] = '.'
            elif c_state == '.' and (adj_bugs == 1 or adj_bugs == 2):
                next_data[y][x] = '#'
    data = next_data
    draw()
    # sleep(0.5)
        
ans = p = 0
for y in range(5):
    for x in range(5):
        if data[y][x] == '#':
            ans += 2**p
        p += 1
print(ans)
