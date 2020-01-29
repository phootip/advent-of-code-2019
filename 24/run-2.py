from time import time, sleep
from copy import deepcopy

# f = open('24/example1.txt')
# f = open('example1.txt')
f = open('input.txt')
data = list(map(lambda x: list(x.strip()), f.readlines()))
mem = {}
next_mem = {}
data[2][2] = '?'
mem[0] = data

def draw(level, mem):
    data = mem[level]
    print(f'level: {level}')
    for y in range(5):
        for x in range(5):
            print(data[y][x], end='')
        print()
    print()

def is_infested(level,x,y):
    if not mem.get(level):
        # next_mem[level] = [['.' for i in range(5)] for j in range(5)]
        return 0
    if (x,y) == (2,2):
        return 0
    elif x < 0 or y < 0 or x > 4 or y > 4:
        if x < 0:
            return is_infested(level-1,1,2)
        elif x > 4:
            return is_infested(level-1,3,2)
        elif y < 0:
            return is_infested(level-1,2,1)
        elif y > 4:
            # print(f'think {is_infested(level-1,3,2)}')
            return is_infested(level-1,2,3)
        return 0
    else:
        return 1 if mem[level][y][x] == '#' else 0

def count_adj(level,x,y):
    adj_bugs = 0
    adj_bugs += is_infested(level,x-1,y)
    adj_bugs += is_infested(level,x+1,y)
    adj_bugs += is_infested(level,x,y-1)
    adj_bugs += is_infested(level,x,y+1)
    if (x,y) == (1,2):
        for i in range(5):
            adj_bugs += is_infested(level+1,0,i)
    elif (x,y) == (3,2):
        for i in range(5):
            adj_bugs += is_infested(level+1,4,i)
    elif (x,y) == (2,1):
        for i in range(5):
            adj_bugs += is_infested(level+1,i,0)
    elif (x,y) == (2,3):
        for i in range(5):
            adj_bugs += is_infested(level+1,i,4)
    return adj_bugs

def has_bugs(data):
    for y in range(5):
        for x in range(5):
            if x == 2 and y == 2:
                continue
            elif data[y][x] == '#':
                return True
    return False

def expand(mem):
    levels = sorted(list(mem.keys()))
    low = levels[0]
    high = levels[-1]
    if has_bugs(mem[low]):
        mem[low-1] = [['.' for i in range(5)] for j in range(5)]
        mem[low-1][2][2] = '?'
    if has_bugs(mem[high]):
        mem[high+1] = [['.' for i in range(5)] for j in range(5)]
        mem[high+1][2][2] = '?'
    

draw(0, mem)
mins = 200
while mins > 0:
    mins -= 1
    expand(mem)
    next_mem = deepcopy(mem)
    for level in mem:
        data = mem[level]
        next_data = [[data[i][j] for j in range(5)] for i in range(5)]
        for y in range(5):
            for x in range(5):
                if x == 2 and y == 2:
                    continue
                c_state = data[y][x]
                adj_bugs = count_adj(level,x,y)
                if c_state == '#' and adj_bugs != 1:
                    next_data[y][x] = '.'
                elif c_state == '.' and (adj_bugs in [1,2]):
                    next_data[y][x] = '#'
        next_mem[level] = next_data
    mem = next_mem

ans = 0
for level in sorted(mem.keys()):
    # draw(level,mem)
    data = mem[level]
    for y in range(5):
        for x in range(5):
            if data[y][x] == '#':
                ans +=1
print(ans)
