from computer import Computer

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

def part1(graph):
    ans = 0
    for y in range(50):
        for x in range(50):
            if graph[(x,y)]:
                ans += 1
    print(ans)

f = open('input.txt')
graph = {}
program = list(map(int, f.readline().strip().split(',')))
# robot = Robot(program)
# robot.deploy(0,1)
for y in range(100):
    for x in range(100):
        print((x,y))
        robot = Robot(program)
        graph[(x,y)] = robot.deploy(x,y)
draw(graph)
# part1(graph)
