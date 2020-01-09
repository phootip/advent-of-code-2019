from computer import Computer
from PIL import Image, ImageColor
import threading
import time

f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))


class Arcade():
    def __init__(self, program):
        self.com = Computer(program)
        self.map = {}
        self.im = Image.new('RGB', (50, 50))
        self.ball = 0
        self.paddle = 0
        self.score = 0

    def step(self):
        # print(self.com.inputs)
        # print(self.com.need_input)
        while (len(self.com.inputs) > 0) and not self.com.halted:
            # print(self.com.halted)
            # print(self.com.inputs)
            pass
        while (not self.com.need_input) and not self.com.halted:
            # print(self.com.halted)
            # print(self.com.need_input)
            # print(self.com.outputs)
            pass
        self.load_output()
        # print(self.com.inputs)
        # print(self.com.need_input)

    def load_output(self):
        while len(self.com.outputs) % 3 != 0:
            pass
        data = [tuple(self.com.outputs[i:i+3])
                for i in range(0, len(self.com.outputs), 3)]
        for x, y, v in data:
            # print((x, y), v)
            self.map[(x, y)] = v
            if v == 4:
                self.ball = x
            elif v == 3:
                self.paddle = x
            if (x, y) == (-1, 0):
                self.score = v
        self.com.outputs = []

    def draw(self):
        for (x, y), v in self.map.items():
            if (x, y) == (-1, 0):
                # self.score = v
                # print(self.score)
                pass
            else:
                self.im.putpixel((x, y), ImageColor.getrgb(self.get_color(v)))
        self.im.save('map.png')

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
        elif v == 3:  # paddle
            return 'yellow'
        elif v == 4:  # ball
            return 'red'
        else:
            print(f'error {v}')

    def check_dup(self):
        c_map = self.map[:]
        while c_map:
            point = c_map.pop(0)
            if point in c_map:
                print(f'duplicate point is: {point}')

    def move(self):
        # value = int(input('move join? >>'))
        if self.ball < self.paddle:
            self.com.input(-1)
        elif self.ball == self.paddle:
            self.com.input(0)
        elif self.ball > self.paddle:
            self.com.input(1)

    def run(self):
        thread = threading.Thread(target=self.com.execute)
        thread.start()
        time.sleep(2)
        self.load_output()
        while not self.com.halted:
            # print('start game')
            self.move()
            # time.sleep(0.1)
            # self.load_output()
            self.step()
            self.draw()


program[0] = 2
a = Arcade(program)
start = time.time()
print(start)
a.run()
print(f'time: {time.time() - start}')
print(a.score)
