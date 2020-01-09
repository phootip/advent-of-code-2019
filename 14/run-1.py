import math
import time
from copy import deepcopy


def cal(filename, stock):
    f = open(filename)
    data = {}
    for line in f:
        line = line.strip().replace(',', '').split(' ')
        line.pop(-3)
        total_gcd = int(line[0])
        for i in range(0, len(line), 2):
            line[i] = int(line[i])
        product = line[-2:]
        cost = line[:-2]
        cost = [[cost[i], cost[i+1]] for i in range(0, len(cost), 2)]
        # data[product[1]] = {'value': product[0],
        #                     'cost': cost[::2], 'mat': cost[1::2]}
        data[product[1]] = {'value': product[0],
                            'cost': cost}

    def get_mat(l):
        for i in range(len(l)):
            if l[i][1] != 'ORE':
                return l.pop(i)
        return -1

    def get_fuel(data, left_over):
        fuel = data['FUEL']
        final_react = deepcopy(fuel['cost'])
        while len(final_react) > 1:
            mat = get_mat(final_react)
            reaction = deepcopy(data[mat[1]])
            mul = math.ceil(mat[0]/reaction['value'])
            reaction['value'] *= mul
            left_over[mat[1]] += reaction['value'] - mat[0]
            for current_mat in reaction['cost']:
                current_mat[0] *= mul
            for current_mat in reaction['cost']:
                current_mat[0] -= left_over[current_mat[1]]
                if current_mat[0] < 0:
                    print('error')
                    return -1
                left_over[current_mat[1]] = 0
                if current_mat[1] in [a[1] for a in final_react]:
                    for final_mat in final_react:
                        if final_mat[1] == current_mat[1]:
                            final_mat[0] += current_mat[0]
                else:
                    final_react.append(current_mat)
            # print(f'reaction: {reaction}')
            # print(left_over)
            # print(fuel)
        return final_react[0][0]
    left_over = {k: 0 for k in data}
    left_over['ORE'] = 0
    ore = 0
    state = []
    ans = 0
    while ore < stock:
        ans += 1
        ore += get_fuel(data, left_over)
        # print(ore)
        # c_state = [left_over[k] for k in left_over]
        # c_state.pop(5)
        # c_state.pop(1)
        # c_state.pop(-2)
        # c_state.pop(3)
        # print(c_state)
        print(stock - ore)
        # if all([s == 0 for s in c_state]):
        #     return [ore, ans]
        #     break
        break
    print(f'ore used: {ore}')
    print(f'fuel get: {ans}')
    print(left_over)
    return [ore, ans, left_over]
    # print(ore)

    # print(fuel)
    # for k in left_over:
    #     if left_over[k] > 0:
    #         print(k, left_over[k])


for i in range(3, 4):
    start = time.time()
    f = f'example{i}.txt'
    ore, ans, left_over = cal(f, 10 ** 12)
    print(f'time used: {time.time() - start}')
    lap = math.floor(10 ** 12 / ore)
    print(f'big lap: {lap}')
    print(f'ore used: {lap * ore}')
    print(f'fuel get {lap * ans}')
    # for
    # ore_left = 10**12 - lap*ore
    # print(f'ore left: {ore_left}')
    # ore, ans = cal(f, ore_left)
    # print(ans - 1)
# f = 'input.txt'
# cal(f)
# print(math.floor(10 ** 12 / ore) * ans)
