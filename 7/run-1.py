from computer import Computer

# f = open('example.txt')
f = open('input.txt')
program = list(map(int, f.readline().strip().split(',')))


def cal(phase):
    result = 0
    for value in phase:
        A = Computer(program, [value, result])
        A.execute()
        result = A.outputs[0]
    return result


current_max = -1000

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(5):
                    phase = [i, j, k, l, m]
                    if len(phase) == len(set(phase)):
                        result = cal(phase)
                        current_max = max(result, current_max)
print(current_max)
