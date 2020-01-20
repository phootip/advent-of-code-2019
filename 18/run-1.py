from PIL import Image, ImageColor
from pprint import pprint
from time import sleep,time
from copy import deepcopy

im = Image.new('RGB', (100, 100))
mem = {}

def save_graph(data):
    x = y = 0
    pos = ()
    graph = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == '#':
                continue
            graph[(x, y)] = {'value': data[y][x], 'adj': []}
            if data[y][x] == '@':
                graph[(x, y)]['value'] = '.'
                pos = (x, y)
    for x, y in graph:
        if graph.get((x, y-1)):  # N
            graph[(x, y)]['adj'].append((x, y-1))
        if graph.get((x, y+1)):  # S
            graph[(x, y)]['adj'].append((x, y+1))
        if graph.get((x+1, y)):  # W
            graph[(x, y)]['adj'].append((x+1, y))
        if graph.get((x-1, y)):  # E
            graph[(x, y)]['adj'].append((x-1, y))
    return graph, pos


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
    im.putpixel(pos, ImageColor.getrgb('yellow'))
    im.save('map.png')


def reachable_keys(graph, pos):
    queue = [(pos, 0)]
    visited = []
    keys = []

    while queue:
        node, cost = queue.pop(0)
        visited.append(node)
        adj = graph[node]['adj']
        for new_node in adj:
            if not new_node in visited and not graph[new_node]['value'].isupper():
                new_cost = cost + 1
                queue.append((new_node, new_cost))
                if graph[new_node]['value'].islower():
                    keys.append((new_node, new_cost))
    return keys


def grab_key(graph, pos, key):
    pos, cost = key
    door = graph[pos]['value'].upper()
    for k in graph:
        if graph[k]['value'] == door:
            graph[k]['value'] = '.'
    graph[pos]['value'] = '.'
    return pos, cost

def count_keys(graph):
    c = 0
    for (x, y), v in graph.items():
        if v['value'].islower():
            c += 1
    return c

def part1(graph,pos):
    # if mem.get((graph,pos)):
    #     return mem[(graph,pos)]
        
    ans = float('inf')
    if any(v['value'].islower() for (x, y), v in graph.items()):
        # sleep(0.5)
        keys = reachable_keys(graph, pos)
        if mem.get((tuple(keys),pos)):
            # print('this help')
            return mem[(tuple(keys),pos)]
        for key in keys:
            if pos == (40,40):
                print(len(keys))
                print(f'cal key: {key}')
            new_graph = deepcopy(graph)
            new_pos, cost = grab_key(new_graph, pos, key)
            ans = min(ans,part1(new_graph,new_pos) + cost)
            # print(ans)
        mem[(tuple(keys),pos)] = ans
        return ans
        # ending
    # draw(graph, pos)
    # draw2(graph, pos)
    # print(ans)
    else:
        # mem[(deepcopy(graph),pos)] = 0
        return 0


def run(data):
    height = len(data)
    width = len(data[0])
    # print(height,width)
    graph, pos = save_graph(data)
    draw2(graph, pos)
    print(pos)
    ans = part1(graph,pos)
    print(ans)


for i in range(1, 6):
    # if i == 4:
    #     continue
    f = open(f'example{i}.txt')
    # f = open(f'input.txt')
    start = time()
    mem = {}
    data = list(map(lambda x: x.strip(), f.readlines()))
    run(data)
    print(f'time used: {time() - start}')
    # break
