import time

start = time.time()


def tokenize(filename):
    f = open(filename)
    string = f.readline().strip()
    string *= 10 ** 4
    return list(map(int, list(string)))


def tokenize_str(string):
    string = string.strip()
    string *= 10**4
    return list(map(int, list(string)))


def gen_pattern(base, digit):
    new_pattern = [[k, digit] for k in base]
    # print(new_pattern)
    return new_pattern


def offseting(data):
    offset = int(''.join(str(c) for c in data[:7]))
    return data[offset:], offset


def part1(data, pattern, loop):
    print(f'data length: {len(data)}')
    data, offset = offseting(data)
    print(f'data length: {len(data)}')
    print(offset - len(data))
    # for digit in range(1, len(data) + 1):
    #     new_pattern = gen_pattern(pattern, digit + offset)
    #     mem.append(new_pattern)
    #     print(len(data), len(mem))
    print(offset)
    ans = data[:]
    for i in range(loop):
        print(f'loop: {i}')
        new_data = []
        for digit in range(len(data)):
            if digit == 0:
                acc = sum(ans[digit:])
            else:
                acc = new_data[digit - 1] - ans[digit - 1]
            new_data.append(acc)
            # new_data.append(abs(acc) % 10)
            # print(len(data), len(new_data))
        new_data = [abs(acc) % 10 for acc in new_data]
        ans = new_data[:]
    return ''.join(str(c) for c in ans)


filename = '16/input.txt'
data = tokenize(filename)

# data = tokenize_str('03036732577212944063491565474664')  # 84462026
# data = tokenize_str('02935109699940807407585447034323')  # 78725270
# data = tokenize_str('03081770884921959731165446850517')  # 53553731

pattern = [1, 0, -1, 0]
# print(data)
# print(len(data))
# print(f'part1: {part1(data,pattern,4)}')
print(f'part2: {part1(data,pattern,100)[:8]}')
print(f'time used: {time.time() - start}')
