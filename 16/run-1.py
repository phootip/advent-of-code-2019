import time


def tokenize(filename):
    f = open(filename)
    return list(map(int, list(f.readline().strip())))


def gen_pattern(base, digit, length):
    new_pattern = []
    while True:
        for k in base:
            for l in range(digit):
                new_pattern.append(k)
                if len(new_pattern) >= length + 1:
                    new_pattern.pop(0)
                    return new_pattern


def part1(data, pattern, loop):
    mem = []
    for digit in range(1, len(data) + 1):
        new_pattern = gen_pattern(pattern, digit, len(data))
        mem.append(new_pattern)
    ans = data[:]
    for i in range(loop):
        print(f'loop: {i}')
        new_data = []
        for digit in range(len(data)):
            acc = 0
            c_pattern = mem[digit]
            for j in range(len(data)):
                acc += ans[j] * c_pattern[j]
            new_data.append(abs(acc) % 10)
        ans = new_data[:]
    return ''.join(str(c) for c in ans)


filename = '16/input.txt'
# filename = '16/example1.txt'
# filename = '16/example2.txt'
# filename = '16/example3.txt'
# filename = '16/example4.txt'

data = tokenize(filename)
pattern = [0, 1, 0, -1]
print(data)
# print(len(data))
# print(f'part1: {part1(data,pattern,4)}')
start = time.time()
print(f'part1: {part1(data,pattern,100)[:8]}')
print(f'time used: {time.time() - start}')
