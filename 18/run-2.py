from PIL import Image, ImageColor
from pprint import pprint
from time import sleep,time
from copy import deepcopy

im = Image.new('RGB', (100, 100))
mem = {}

def save_graph(data):
    x = y = 0
    pos = []
    graph = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                continue
            graph[(x, y)] = {'value': data[y][x], 'adj': []}
            if data[y][x] == '@':
                graph[(x, y)]['value'] = '.'
                pos.append((x, y))
    return graph, pos

def connect(graph):
    for x, y in graph:
        if (x, y-1) in graph:  # N
            graph[(x, y)]['adj'].append((x, y-1))
        if (x, y+1) in graph:  # S
            graph[(x, y)]['adj'].append((x, y+1))
        if (x+1, y) in graph:  # W
            graph[(x, y)]['adj'].append((x+1, y))
        if (x-1, y) in graph:  # E
            graph[(x, y)]['adj'].append((x-1, y))

def draw(graph, pos, width=17, height=10):
    sleep(0.5)
    for y in range(height):
        for x in range(width):
            if (x,y) == pos:
                print('@', end='')
            elif graph.get((x,y)):
                print(graph[(x, y)]['value'], end='')
            else:
                print('#',end='')
        print()
    print()


def draw2(graph, pos):
    for (x, y), v in graph.items():
        if v['value'] == '.':  # ground
            im.putpixel((x, y), ImageColor.getrgb('gray'))
        elif v['value'].isupper():  # door
            im.putpixel((x, y), ImageColor.getrgb('blue'))
        elif v['value'].islower():  # key
            im.putpixel((x, y), ImageColor.getrgb('red'))
    for p in pos:
        im.putpixel(p, ImageColor.getrgb('yellow'))
    im.save('map.png')


def get_keys_cost(graph, pos):
    if pos in mem:
        # print('small help')
        return mem[pos]
    queue = [(pos, 0, [])]
    visited = [pos]
    keys = []

    while queue:
        node, cost, doors = queue.pop(0)
        # visited.append(node)
        adj = graph[node]['adj']
        if graph[node]['value'].isupper():
            doors.append(graph[node]['value'])
        if graph[node]['value'].islower():
            key = {'pos': node, 'cost': cost, 'doors': doors}
            keys.append(key)
        for new_node in adj:
            if not new_node in visited:
                visited.append(new_node)
                new_cost = cost + 1
                new_doors = doors[:]
                queue.append((new_node, new_cost, new_doors))
    mem[pos] = keys
    # print_keys(graph, keys)
    return keys


# def grab_key(graph, pos, key):
#     pos, cost = key
#     door = graph[pos]['value'].upper()
#     for k in graph:
#         if graph[k]['value'] == door:
#             graph[k]['value'] = '.'
#     graph[pos]['value'] = '.'
#     return pos, cost

def print_keys(graph, keys):
    result = []
    for key in keys:
        result.append(graph[key['pos']]['value'])
    print(result)

def count_keys(graph):
    c = 0
    for (x, y), v in graph.items():
        if v['value'].islower():
            c += 1
    return c

def len_sublist(l):
    result = 0
    for i in l:
        result += len(i)
    return result

def part2(graph,pos_s,opened_doors):
    # print(pos_s)
    if (tuple(pos_s),tuple(opened_doors)) in mem:
        return mem[(tuple(pos_s),tuple(opened_doors))]
    ans = float('inf')
    keys_4 = []
    for pos in pos_s:
        keys_4.append(get_keys_cost(graph, pos))
    # print(keys_4)
    if len_sublist(keys_4) > len(opened_doors):
        for i in range(4):
            keys = keys_4[i]
            for key in keys:
                if set(key['doors']) <= opened_doors and graph[key['pos']]['value'].upper() not in opened_doors:
                    # print(graph[key['pos']]['value'])
                    new_pos_s = pos_s[:]
                    new_pos_s[i] = key['pos']
                    new_opened = opened_doors.copy()
                    new_opened.add(graph[key['pos']]['value'].upper())
                    ans = min(ans,part2(graph,new_pos_s,new_opened) + key['cost'])
        mem[(tuple(pos_s),tuple(opened_doors))] = ans
        return ans
    else:
        mem[(tuple(pos_s),tuple(opened_doors))] = 0
        return 0


def run(data):
    height = len(data)
    width = len(data[0])
    # print(height,width)
    graph, pos_s = save_graph(data)
    connect(graph)
    draw2(graph, pos_s)
    opened_doors = set()
    print(f'all_keys: {count_keys(graph)}')
    ans = part2(graph,pos_s,opened_doors)
    print(ans)


for i in range(1, 5):
    ans = [6,24,32,72]
    print(ans)
    # f = open(f'example2-{i}.txt')
    f = open(f'input2.txt')
    start = time()
    mem = {}
    data = list(map(lambda x: x.strip(), f.readlines()))
    run(data)
    print(f'time used: {time() - start}')
    break
