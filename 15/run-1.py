from computer import Computer
from PIL import Image, ImageColor
from collections import deque
import time


class Robot():
    def __init__(self, program):
        self.com = Computer(program)
        self.x = 0
        self.y = 0
        self.map = {(0, 0): 1}
        self.graph = {(0, 0): [-1, -1, -1, -1]}  # up down left right
        self.im = Image.new('RGB', (100, 100))
        self.unexplored = []
        self.unexplored.append((0, 0))
        self.route = deque()

    def run(self):
        while not self.com.halted:
            if not self.unexplored:
                print('map explored')
                return
            self.move()
            self.com.execute()
            status = self.com.outputs.pop(0)
            self.update(status)
            # self.draw()
            # print((self.x, self.y))
            # print(self.graph)
            # print(self.unexplored)
            # time.sleep(0.1)
            # break

    def move(self):
        # self.last_move = int(input('give me a command >> '))  # 1,2,3,4
        self.last_move = self.get_move()
        if self.last_move < 1 or self.last_move > 4:
            print(f'Move Error: {self.last_move}')
            exit()
        self.com.input(self.last_move)

    def get_move(self):
        # dest = self.unexplored[0]
        dest = self.unexplored[-1]
        if (self.x, self.y) == dest:
            return self.graph[dest].index(-1) + 1
        elif not self.route:
            self.route = self.shortest_path((self.x, self.y), dest)
        return self.route.pop(0)

    def shortest_path(self, pos, dest):
        queue = []
        visited = []
        queue.append({'pos': pos, 'route': []})

        while queue:
            node = queue.pop(0)
            pos = node['pos']
            route = node['route']
            visited.append(pos)
            for i in range(4):
                next_pos = self.graph[pos][i]
                new_route = route[:]
                new_route.append(i+1)
                if next_pos != -1 and next_pos != 0 and next_pos not in visited:
                    if next_pos == dest:
                        return new_route
                    else:
                        queue.append(
                            {'pos': next_pos, 'route': new_route})

    def update(self, status):
        old_x = self.x
        old_y = self.y
        if self.last_move == 1:  # N
            self.y -= 1
        elif self.last_move == 2:  # S
            self.y += 1
        elif self.last_move == 3:  # E
            self.x += 1
        elif self.last_move == 4:  # W
            self.x -= 1
        else:
            print(f'Error : {status}')

        self.graph[(old_x, old_y)][self.last_move - 1] = (self.x, self.y)
        self.map[(self.x, self.y)] = status
        if status == 0:
            self.x = old_x
            self.y = old_y
            self.graph[(old_x, old_y)][self.last_move - 1] = 0
        else:
            if (self.x, self.y) not in self.unexplored and (self.x, self.y) not in self.graph:
                # self.unexplored.insert(0, (self.x, self.y))
                self.unexplored.append((self.x, self.y))
                self.graph[(self.x, self.y)] = [-1, -1, -1, -1]
            if self.last_move % 2 == 0:
                self.graph[(self.x, self.y)][self.last_move -
                                             2] = (old_x, old_y)
            else:
                self.graph[(self.x, self.y)][self.last_move] = (old_x, old_y)
            # 1 -> 1
            # 2 -> 0
            # 3 -> 3
            # 4 -> 2
        if (old_x, old_y) in self.unexplored and all(value != -1 for value in self.graph[(old_x, old_y)]):
            self.unexplored.remove((old_x, old_y))

    def draw(self):
        for (x, y), v in self.map.items():
            self.im.putpixel(
                (x+50, y+50), ImageColor.getrgb(self.get_color(v)))
        self.im.putpixel((self.x+50, self.y+50),
                         ImageColor.getrgb(self.get_color(3)))
        self.im.save('map.png')

    def get_color(self, v):
        if v == 0:
            return 'brown'
        elif v == 1:
            return 'gray'
        elif v == 2:
            return 'blue'
        elif v == 3:  # robot
            return 'yellow'
        else:
            print(f'error {v}')

    def part1(self):
        dest = None
        for pos in self.map:
            if self.map[pos] == 2:
                dest = pos
        return len(self.shortest_path((0, 0), dest))

    def part2(self):
        oxygen = None
        for pos in self.map:
            if self.map[pos] == 2:
                oxygen = pos
                break

        queue = []
        new_queue = []
        visited = []
        queue.append(oxygen)

        mins = 0
        while queue or new_queue:
            if not queue:
                mins += 1
                queue = new_queue[:]
                new_queue = []
            pos = queue.pop(0)
            visited.append(pos)
            for i in range(4):
                next_pos = self.graph[pos][i]
                if next_pos != -1 and next_pos != 0 and next_pos not in visited:
                    self.map[next_pos] = 2
                    # if all(self.map[k] == 2 for k in self.map):
                    # break
                    new_queue.append(next_pos)
            # self.draw()
        return mins


start = time.time()
# f = open('input.txt')
f = open('15/input.txt')
program = list(map(int, f.readline().strip().split(',')))
# print(program)
robot = Robot(program)
robot.run()
print(f'part1: {robot.part1()}')
print(f'time used: {time.time() - start}')
print(f'part1: {robot.part2()}')
print(f'time used: {time.time() - start}')
