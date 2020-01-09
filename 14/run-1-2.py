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
        stock['ORE'] = amount
        return amount
    if stock[mat] >= amount:
        return
    ans = 0
    while stock[mat] - amount < 0:
        reaction = data[mat]
        for need_amount, need_mat in reaction['cost']:
            if stock[need_mat] < need_amount:
                ans += produce(stock, need_mat, need_amount)
            stock[need_mat] -= need_amount
        stock[mat] += reaction['value']
    return ans


# filename = 'example3.txt'
filename = 'input.txt'
data = tokenize(filename)
stock = {k: 0 for k in data}
stock['ORE'] = 0
ans = produce(stock, 'FUEL', 1)
print(ans)
# print(stock)
