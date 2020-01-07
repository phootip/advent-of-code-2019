import os
import itertools
import math
script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in


def find_ans(rel_path):
    file = os.path.join(script_dir, rel_path)
    f = open(file)
    mem = {}
    x = y = 0
    for line in f:
        x = 0
        for point in line.strip():
            if point == '#':
                mem[(x, y)] = {}
            x += 1
        y += 1
    for pair in itertools.combinations(mem, 2):
        [(x1, y1), (x2, y2)] = pair
        dy = y2 - y1
        dx = x2 - x1
        gcd = math.gcd(dy, dx)
        m = (dx/gcd, dy/gcd)
        dx /= gcd
        dy /= gcd
        if dx == 0:
            dy = 1 if dy > 0 else -1
        elif dy == 0:
            dx = 1 if dx > 0 else -1
        m = (dx, dy)
        # print(m)
        if m not in mem[(x1, y1)]:
            mem[(x1, y1)][m] = [(x2, y2)]
        else:
            mem[(x1, y1)][m].append((x2, y2))

        if (-m[0], -m[1]) not in mem[(x2, y2)]:
            mem[(x2, y2)][(-m[0], -m[1])] = [(x1, y1)]
        else:
            mem[(x2, y2)][(-m[0], -m[1])].append((x1, y1))

    current_key = list(mem.keys())[0]
    for key in mem:
        if(len(mem[key]) > len(mem[current_key])):
            current_key = key
    print(current_key, len(mem[current_key]))
    print(mem[current_key])
    data = mem[current_key]
    # print(sorted(data.items()))
    data = {k: v for k, v in sorted(data.items(), key=custom_sort)}
    degree = math.radians(-90)

    print(data)
    c = 0
    start = False
    for m in data:
        print(m, math.atan2(m[1], m[0]))
        if math.atan2(m[1], m[0]) >= degree:
            start = True
        if start:
            point = data[m].pop(0)
            mem.pop(point)
            c += 1
    while len(mem) > 1:
        for m in data:
            if len(data[m]) == 0:
                continue
            else:
                point = data[m].pop(0)
                mem.pop(point)
                c += 1
            if c == 200:
                return point


def custom_sort(item):
    m = item[0]
    dx, dy = m
    print(math.atan2(dy, dx))
    # return math.atan2(dy, dx) + math.radians(-90)
    return math.atan2(dy, dx)


# rel_path = 'example5.txt'
# rel_path = 'example6.txt'
# rel_path = 'example7.txt'
rel_path = 'input.txt'
print(find_ans(rel_path))
