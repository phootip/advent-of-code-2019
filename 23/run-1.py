from computer import Computer
from time import time, sleep

f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))

computers = []
buffer = {}
def gen_computers():
    for i in range(50):
        computers.append(Computer(program,[i],i))
        buffer[i] = []

def simulate():
    while True:
        for i in range(50):
            com = computers[i]
            if not buffer[i]:
                com.input(-1)
            else:
                com.inputs += buffer[i]
                buffer[i] = []
                # print(com.need_input)
            while not com.need_input:
                com.execute()
                if len(com.outputs) == 1:
                    com.execute()
                    com.execute()
            com.need_input = False

            while com.outputs:
                addr, x, y = [com.get_output() for j in range(3)]
                # print(addr,x,y)
                if addr == 255:
                    return y
                buffer[addr].append(x)
                buffer[addr].append(y)
            # break
        print(buffer)
        sleep(0.5)
        # break


gen_computers()
ans = simulate()
print(ans)
