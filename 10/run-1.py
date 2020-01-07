import os
import itertools
import math
answer = [[(3, 4), 8], [(5, 8), 33], [(1, 2), 35],
          [(6, 3), 41], [(11, 13), 210]]
print(answer)

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
                mem[(x, y)] = []
            x += 1
        y += 1
    for pair in itertools.combinations(mem, 2):
        [(x1, y1), (x2, y2)] = pair
        dy = y2 - y1
        dx = x2 - x1
        gcd = math.gcd(dy, dx)
        m = (dx/gcd, dy/gcd)
        if m not in mem[(x1, y1)]:
            mem[(x1, y1)].append(m)
            mem[(x2, y2)].append((-m[0], -m[1]))

    current_key = list(mem.keys())[0]
    for key in mem:
        if(len(mem[key]) > len(mem[current_key])):
            current_key = key
    print(current_key, len(mem[current_key]))


for i in range(1, 8):
    rel_path = f"example{i}.txt"
    find_ans(rel_path)

rel_path = 'input.txt'
find_ans(rel_path)
