from computer import Computer
from collections import defaultdict
from time import time, sleep
from node import Node
from PIL import Image, ImageColor

class Robot():
    def __init__(self, program):
        self.com = Computer(program)
        self.graph = {}
        self.buffer = ''
        self.x = self.y = 0
        self.c_x = self.c_y = 0
        self.im = Image.new('RGB', (50, 50))
        self.direc = [0,-1]

    def run(self):
        self.load_graph()
        self.draw((self.x,self.y))
        # self.think()
        while not self.com.halted:
            self.load_graph()
        print('end while')
        ans = sorted(self.com.mem)[-1]
        print(ans)

    def think(self):
        print('thinking...')
        unvisited = list(self.graph.keys())
        route = []
        direc = (0,-1)
        routes = self.get_routes(unvisited,(self.x,self.y),direc,route)
        print(len(routes))
        print(routes)
        
    def get_routes(self,unvisited,pos,direc,route,last_pos=None):
        routes = []
        while unvisited: 
            self.draw(pos)
            # sleep(0.1)
            adjacent = self.graph[pos]
            if self.count_adj(pos,unvisited) == 0:
                unvisited.remove(pos)
                if not unvisited:
                    return route
                return None
            elif self.count_adj(pos,unvisited) <= 2:
                unvisited.remove(pos)
                for dest in adjacent: 
                    if dest in unvisited and dest != last_pos:
                        direc, route = self.move(pos,dest,direc,route)
                        last_pos = pos
                        pos = dest
                        break
            else:
                print('this is intersection')
                dest = (pos[0] + direc[0],pos[1] + direc[1])
                direc, route = self.move(pos,dest,direc,route)
                last_pos = pos
                pos = dest
        routes.append(route)
        print(len(routes))
        return routes


    def move(self,pos,dest,direc,route):
        new_route = route[:]
        if (pos[0] + direc[0], pos[1] + direc[1]) == dest:
            new_route[-1] += 1
            return direc, new_route
        else: # turn
            if new_route:
                new_route[-1] = str(new_route[-1])
            new_direc = (dest[0] - pos[0], dest[1] - pos[1])
            if new_direc[0] == -direc[0]:
                # new_route.append('L')
                # new_route.append('L')
                return False, False
            elif (new_direc[0] == direc[1] and direc[1] != 0) or (new_direc[1] == -direc[0] and direc[0] != 0): # 0,-1 -> -1,0 -> 0,1 -> 1,0
                new_route.append('L')
            elif (new_direc[0] == -direc[1] and direc[1] != 0) or (new_direc[1] == direc[0] and direc[0] != 0):
                new_route.append('R')
            new_route.append(1)
            return new_direc, new_route

    def load_graph(self):
        # print('loading...')
        while not self.com.need_input and not self.com.halted:
            self.com.execute()
            self.load_outputs()
            if self.buffer[-2:] == '\n\n':
                print(self.buffer)
                # print(self.x, self.y)
                self.buffer = ''
                self.c_x = self.c_y = 0
                break
        for x,y in self.graph:
            if self.graph.get((x,y-1)): # N
                self.graph[(x,y)][0] = (x,y-1)
            if self.graph.get((x,y+1)): # S
                self.graph[(x,y)][1] = (x,y+1)
            if self.graph.get((x+1,y)): # W
                self.graph[(x,y)][2] = (x+1,y)
            if self.graph.get((x-1,y)): # E
                self.graph[(x,y)][3] = (x-1,y)
            # print((x,y), self.graph[(x,y)])
    
    def check_route(self,route):
        route = 'R,8,R,8,R,4,R,4,R,8,L,6,L,2,R,4,R,4,R,8,R,8,R,8,L,6,L,2' # test
        route = route.split(',')
        print(route)  
        if len(route) > 11 * 11:
            return False
        # think

        print(len(self.graph))            
        return False

    def draw(self,pos):
        for (x, y), v in self.graph.items():
            self.im.putpixel(
                (x, y), ImageColor.getrgb('blue'))
        self.im.putpixel(pos,
                         ImageColor.getrgb('yellow'))
        self.im.save('map.png')

    def load_outputs(self):
        while self.com.outputs:
            c = self.com.get_output()
            if c > 1000:
                print(c)
                print(chr(c))
            if c == 94: # ord(c) == '^'
                self.x = self.c_x
                self.y = self.c_y
            if c == 35 or c == 94:  # 35 means '#', 46 means '.', 10 means 'new_line'
                self.graph[(self.c_x, self.c_y)] = [-1,-1,-1,-1] # N, S, W, E

            self.c_x += 1
            
            if c == 10:
                self.c_x = 0
                self.c_y += 1
            self.buffer += chr(c)

    def part1(self):
        ans = 0
        for point in self.graph:
            if self.graph[point] == 35 and self.is_intersect(point):
                print(f'point : {point}')
                print(f'mul(point) : {point[0] * point[1]}')
                ans += point[0] * point[1]
        return ans

    def is_intersect(self, point):
        x, y = point
        n = self.graph.get((x, y-1)) != None
        s = self.graph.get((x, y+1)) != None
        e = self.graph.get((x+1, y)) != None
        w = self.graph.get((x-1, y)) != None
        return all([n, s, e, w])

    def count_adj(self, point, unvisited):
        x, y = point
        n = unvisited.count((x, y-1))
        s = unvisited.count((x, y+1))
        e = unvisited.count((x+1, y))
        w = unvisited.count((x-1, y))
        return n+s+e+w 

    def str_to_ascii(self, string):
        if len(string) > 20:
            print(f'''Error too long didn't read : {len(string)}''')
        result = []
        for char in string:
            result.append(ord(char))
        result.append(10)
        return result


# f = open('17/input.txt')
f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))
program[0] = 2
robot = Robot(program)
# robot.run()
# print(f'part1 : {robot.part1()}')

main_routine = robot.str_to_ascii('A,C,C,B,A,C,B,A,C,B')
func_A = robot.str_to_ascii('L,6,R,12,L,4,L,6')
func_B = robot.str_to_ascii('L,6,L,10,L,10,R,6')
func_C = robot.str_to_ascii('R,6,L,6,R,12')
command = main_routine + func_A + func_B + func_C
get_feed = robot.str_to_ascii('n')
command += get_feed
robot.com.inputs += command
robot.run()

# robot.check_route('test')
