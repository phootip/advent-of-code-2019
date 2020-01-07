from computer import Computer
import time
import threading
from PIL import Image, ImageColor


class Robot():
    def __init__(self, program):
        self.dir = [0, -1]
        self.x = self.y = 0
        self.path = {}
        self.path[self.pos()] = 1
        self.com = Computer(program)

    def pos(self):
        return (self.x, self.y)

    def read(self):
        if self.pos() not in self.path:
            self.path[self.pos()] = 0
        return self.path[self.pos()]

    def turn(self, value):
        if value == 0:
            self.turn_left()
        elif value == 1:
            self.turn_right()

    def turn_left(self):
        if self.dir[0] == 0:
            self.dir = [self.dir[1], self.dir[0]]
        else:
            self.dir = [self.dir[1], -self.dir[0]]

    def turn_right(self):
        if self.dir[0] == 0:
            self.dir = [-self.dir[1], self.dir[0]]
        else:
            self.dir = [self.dir[1], self.dir[0]]

    def walk(self):
        self.x += self.dir[0]
        self.y += self.dir[1]

    def paint(self, color):
        self.path[self.pos()] = color

    def draw(self):
        im = Image.new('1', (250, 250))  # create the Image of size 1 pixel
        for point in self.path:
            x, y = point
            if self.path[point] == 1:
                color = 'white'
            else:
                color = 'black'
            im.putpixel((x, y), ImageColor.getcolor(color, '1'))
        im.save('simplePixel.png')

    def execute(self):
        thread = threading.Thread(target=self.com.execute)
        thread.start()
        while not self.com.halted or self.com.outputs:
            self.com.input(self.read())
            while len(self.com.outputs) < 2:
                # print(self.com.outputs)
                pass
            color = self.com.get_output()
            turn = self.com.get_output()
            self.paint(color)
            self.turn(turn)
            self.walk()
            # print(color, turn)
            print(len(self.path))
        return len(self.path)


f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))
robot = Robot(program)
ans = robot.execute()

# print(robot.read())
print(ans)
robot.draw()
