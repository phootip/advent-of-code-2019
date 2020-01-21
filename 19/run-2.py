from computer import Computer
import time

class Robot():
    def __init__(self,program):
        self.com = Computer(program)
    
    def deploy(self,x,y):
        self.com.input(x)
        self.com.input(y)
        self.com.execute()
        result = self.com.outputs.pop(0)
        return result

def draw(graph):
    for y in range(100):
        c = 0
        p = 0
        for x in range(100):
            print(graph[(x,y)],end='')
            c += graph[(x,y)]
            if not p and graph[(x,y)]:
                p = (x,y)
        print(f'  {c}, {p}')

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

def find_first(program,graph, prev_first):
    x, y = prev_first
    y += 1
    while True:
        robot = Robot(program)
        graph[(x,y)] = robot.deploy(x,y)
        if graph[(x,y)]:
            return (x,y)
        x += 1

def find_last(program,graph, prev_last):
    x, y = prev_last
    x += 1
    y += 1
    while True:
        robot = Robot(program)
        graph[(x,y)] = robot.deploy(x,y)
        if not graph[(x,y)]:
            return (x-1,y)
        x += 1

def check_ans(graph,program, first, last):
    # print("checking")
    amount_1 = last[0] - first[0] + 1
    # print(f'amount_1: {amount_1}')
    for i in range(amount_1 - 99):
        print(i)
        for y in range(100):
            # print(f'front: {graph.get((first[0]+i, first[1]-y))}')
            # print(f'back: {graph.get((last[0]+i, last[1]-y))}')
            if not check_pos(graph,program, first[0]+i, first[1]-y) or not check_pos(graph,program,first[0]+i+99, first[1]-y):
                # print('not pass')
                return False
    print('pass!!')
    return True

def check_pos(graph,program,x,y):
    # print(f'checking pos: {(x,y)}')
    if graph.get((x,y)):
        return graph[(x,y)]
    else:
        robot = Robot(program)
        graph[(x,y)] = robot.deploy(x,y)
        return graph[(x,y)]

def part2(program,graph):
    first = last = (12,9)
    # prev_first = prev_last = (2,2)
    while True:
        first = find_first(program,graph, first)
        last = find_last(program,graph, last)
        amount_1 = last[0] - first[0] + 1
        print(f'first,last: {first}, {last}, {amount_1}')
        if amount_1 >= 100:
            if check_ans(graph,program,first,last):
                return
        # time.sleep(0.5)
    # draw(graph)

f = open('input.txt')
graph = {}
program = list(map(int, f.readline().strip().split(',')))
# robot = Robot(program)
# robot.deploy(0,1)
print(1018*10000 + 825-99)
part2(program,graph)
