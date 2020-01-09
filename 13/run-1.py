from computer import Computer
from PIL import Image, ImageColor
import time

f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))


class Arcade():
    def __init__(self, program):
        self.com = Computer(program)
        self.map = []

    def gen_map(self):
        self.com.execute()
        self.map = self.com.outputs
        self.map = [tuple(self.map[i:i+3]) for i in range(0, len(self.map), 3)]

    def draw(self):
        im = Image.new('RGB', (50, 50))  # create the Image of size 1 pixel
        for x, y, v in self.map:
            print(x, y, self.get_color(v), ImageColor.getrgb(self.get_color(v)))
            im.putpixel((x, y), ImageColor.getrgb(self.get_color(v)))
        im.save('map.png')

    def count(self, value):
        ans = 0
        ans = sum(value == v for x, y, v in self.map)
        return ans

    def get_color(self, v):
        if v == 0:
            return 'black'
        elif v == 1:
            return 'brown'
        elif v == 2:
            return 'blue'
        elif v == 3:
            return 'yellow'
        elif v == 4:
            return 'red'

    def check_dup(self):
        c_map = self.map[:]
        while c_map:
            point = c_map.pop(0)
            if point in c_map:
                print(f'duplicate point is: {point}')


a = Arcade(program)
a.gen_map()
# a.check_dup()
a.draw()
print(a.count(2))
