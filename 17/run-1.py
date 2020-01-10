from computer import Computer
from collections import defaultdict


class Robot():
    def __init__(self, program):
        self.com = Computer(program)
        self.map = {}

    def run(self):
        self.get_map()
        # while True:
        # while not self.com.need_input:

    def get_map(self):
        x = y = 0
        for i in range(2059):
            self.com.execute()
            print(len(self.com.outputs))
        while self.com.outputs:
            c = self.com.get_output()
            if c != 10:  # 35 means '#', 46 means '.', 10 means 'new_line'
                self.map[(x, y)] = c
                x += 1
            else:
                x = 0
                y += 1
            print(chr(c), end='')

    def part1(self):
        ans = 0
        for point in self.map:
            if self.map[point] == 35 and self.is_intersect(point):
                print(f'point : {point}')
                print(f'mul(point) : {point[0] * point[1]}')
                ans += point[0] * point[1]
        return ans

    def is_intersect(self, point):
        x, y = point
        n = self.map.get((x, y-1)) == 35
        s = self.map.get((x, y+1)) == 35
        e = self.map.get((x+1, y)) == 35
        w = self.map.get((x-1, y)) == 35
        return all([n, s, e, w])


f = open('17/input.txt')
program = list(map(int, f.readline().strip().split(',')))
robot = Robot(program)
robot.run()
print(f'part1 : {robot.part1()}')
