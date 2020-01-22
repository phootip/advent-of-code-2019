from time import time
from PIL import Image, ImageColor
from collections import defaultdict

im = Image.new('RGB', (100, 100))

def save_graph(data, width, height):
    x = y = 0
    inner_left = inner_right = None
    pos = ()
    graph = {}
    for y in range(len(data)):
        for x in range(len(data[0])):
            if data[y][x] == ' ' and x > 1 and x < width-2 and y > 1 and not inner_left:
                inner_left = (x,y)
            if data[y-1][x] == ' ' and x > 1 and x < width-2 and y < height-2 :
                inner_right = (x,y-1)
            if data[y][x] == '#' or data[y][x] == ' ':
                continue
            graph[(x, y)] = {'value': data[y][x], 'adj': []}
            if data[y][x] == '@':
                graph[(x, y)]['value'] = '.'
                pos = (x, y)
    return graph, inner_left, inner_right

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

def get_portals(graph, width, height, inner_left, inner_right):
    inner_left, inner_top = inner_left
    inner_right, inner_bottom = inner_right
    portals = defaultdict(lambda: [])
    for x in range(2,width-2): # vertical
        save_portal_v(graph,portals,x,0,2)
        save_portal_v(graph,portals,x,height-2,-1)
        save_portal_v(graph,portals,x,inner_top,-1)
        save_portal_v(graph,portals,x,inner_bottom-1,2)
    for y in range(2,height-2):
        save_portal_h(graph,portals,0,y,2)
        save_portal_h(graph,portals,width-2,y,-1)
        save_portal_h(graph,portals,inner_left,y,-1)
        save_portal_h(graph,portals,inner_right-1,y,2)
    
    return portals

def connect_portals(graph, width, height, inner_left, inner_right):
    portals = get_portals(graph, width, height, inner_left, inner_right)
    start = dest = None
    for portal, points in portals.items():
        if portal == 'AA':
            start = points[0]
        elif portal == 'ZZ':
            dest = points[0]
        else:
            graph[points[0]]['adj'].append(points[1])
            graph[points[1]]['adj'].append(points[0])
    return start, dest


def save_portal_v(graph,portals,x,y,offset):
    if graph.get((x,y)):
        if graph[(x,y)]['value'].isupper():
            portal = graph[(x,y)]['value'] + graph[(x,y+1)]['value']
            portals[portal].append((x,y+offset))
        
def save_portal_h(graph,portals,x,y,offset):
    if graph.get((x,y)):
        if graph[(x,y)]['value'].isupper():
            portal = graph[(x,y)]['value'] + graph[(x+1,y)]['value']
            portals[portal].append((x+offset,y))

def check_portals(portals):
    for k,v in portals.items():
        if len(v) != 2:
            print(k)

def draw(graph, pos):
    for (x, y), v in graph.items():
        if v['value'] == '.':  # ground
            im.putpixel((x, y), ImageColor.getrgb('gray'))
    im.putpixel(pos, ImageColor.getrgb('yellow'))
    im.save('map.png')

def shortest_path(graph,start,dest):
    queue = [(start,0)]
    visited = [start]

    while queue:
        node,cost = queue.pop(0)
        if node == dest:
            return cost
        adj = graph[node]['adj']
        for new_node in adj:
            if new_node not in visited:
                visited.append(new_node)
                queue.append((new_node,cost+1))
        

def part1(data):
    width = len(data[0])
    height = len(data)
    print(width,height)
    graph,inner_left,inner_right = save_graph(data,width,height)
    print(f'inner_left, inner_right: {inner_left}, {inner_right}')
    start,dest = connect_portals(graph,width,height, inner_left, inner_right)
    graph = {k:v for k,v in graph.items() if v['value'] == '.'}
    connect(graph)
    ans = shortest_path(graph,start,dest)
    print(ans)
    # draw(graph,pos)

for i in range(1, 3):
    # f = open(f'example{i}.txt')
    f = open(f'input.txt')
    start = time()
    mem = {}
    data = list(map(lambda x: x[:-1], f.readlines()))
    part1(data)
    print(f'time used: {time() - start}')
    break
