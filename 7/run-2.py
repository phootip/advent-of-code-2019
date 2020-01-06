from computer import Computer
import threading
import time
# f = open('example3.txt')
# f = open('example2.txt')
f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))


def cal(phase):
    # phase = [9, 8, 7, 6, 5]
    print(phase)
    result = 0
    Amps = []
    threads = []
    for value in phase:
        A = Computer(program[:], [value], value)
        thread = threading.Thread(target=A.execute)
        thread.start()
        threads.append(thread)
        Amps.append(A)
    time.sleep(1)
    for i in range(5):
        while Amps[i].inputs:
            pass
        Amps[i].inputs = Amps[i-1].outputs
    Amps[0].input(0)
    threads[-1].join()
    result = Amps[-1].outputs[0]
    return result


current_max = -1000

for i in range(5, 10):
    for j in range(5, 10):
        for k in range(5, 10):
            for l in range(5, 10):
                for m in range(5, 10):
                    phase = [i, j, k, l, m]
                    if len(phase) == len(set(phase)):
                        result = cal(phase)
                        current_max = max(result, current_max)
                        print(result)
print(current_max)
