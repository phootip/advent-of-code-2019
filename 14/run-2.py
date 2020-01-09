import copy


def tokenize(filename):
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
        data[product[1]] = {'value': product[0], 'cost': cost}
    return data


def produce(stock, mat, amount):
    if mat == 'ORE':
        return True
    if stock[mat] >= amount:
        return False
    ans = 0
    while stock[mat] - amount < 0:
        # print(stock['FUEL'])
        # print(stock['ORE'])
        reaction = data[mat]
        for need_amount, need_mat in reaction['cost']:
            if stock[need_mat] < need_amount:
                stop = produce(stock, need_mat, need_amount)
                if stop:
                    return stop
            stock[need_mat] -= need_amount
        stock[mat] += reaction['value']
        if mat == 'FUEL':
            if checker(stock):
                break
            pass
    return False


old_state = []


def checker(stock):
    # state = [stock[k] for k in stock]
    # state.pop(-1)
    # state.pop(2)
    # state.pop(4)
    state = []
    for k in stock:
        if k != 'FUEL' and k != 'ORE':
            state.append(stock[k])

    # if state in old_state:
    #     print(state)
    #     print(old_state.index(state))
    #     return True
    # else:
    #     old_state.append(state)
    #     return False
    print(stock['ORE'])
    print(state)
    check = [s < 10 for s in state]
    # print(check)
    if all(check):
        return state
    else:
        return False


filename = 'example3.txt'
# filename = 'input.txt'
data = tokenize(filename)
stock = {k: 0 for k in data}
cap = 10**12
stock['ORE'] = cap
produce(stock, 'FUEL', 1)
ore_used = cap - stock["ORE"]
state = copy.deepcopy(stock)
while stock["ORE"] > 10 ** 6:
    produce(stock, 'FUEL', float('inf'))
    print(f'ore left: {stock["ORE"]}')
    print(f'ore used: {ore_used}')
    print(f'FUEL produced: {stock["FUEL"]}')
    # lap = stock["ORE"] // ore_used
    lap = 1000000
    stock["FUEL"] += lap
    stock["ORE"] -= lap * ore_used
    for k in stock:
        if k != 'FUEL' and k != 'ORE':
            stock[k] += state[k] * lap
    checker(stock)
# print(stock["ORE"] > 10 ** 6)
# print(stock["ORE"])
# print('end loop')
# # print(stock)
# checker(stock)
# produce(stock, 'FUEL', float('inf'))
# ore_used = cap - stock["ORE"]
# print(f'ore left: {stock["ORE"]}')
# print(f'ore used: {ore_used}')
# print(f'FUEL produced: {stock["FUEL"]}')
