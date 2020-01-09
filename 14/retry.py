from collections import defaultdict
from math import ceil


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
        data[product[1]] = {'serving': product[0], 'recipes': cost}
    return data


def make_fuel(reactions, amount):
    orders = [{'material': 'FUEL', 'amount': amount}]
    ore_needed = 0
    leftover = defaultdict(int)

    while orders:
        order = orders.pop(0)
        if order['material'] == 'ORE':
            ore_needed += order['amount']
        elif leftover[order['material']] >= order['amount']:
            leftover[order['material']] -= order['amount']
        else:
            amount_needed = order['amount'] - leftover[order['material']]
            reaction = reactions[order['material']]
            multiplier = ceil(amount_needed / reaction['serving'])
            for recipe in reaction['recipes']:
                orders.append(
                    {'material': recipe[1], 'amount': recipe[0] * multiplier})
            leftover[order['material']] = reaction['serving'] * \
                multiplier - amount_needed
    return ore_needed


def binary_search(lower, upper, target, reactions):
    if lower + 1 == upper:
        return lower
    mid = ((upper - lower) // 2) + lower
    ore_needed = make_fuel(reactions, mid)
    print(f'lower: {lower}')
    print(f'upper: {upper}')
    print(f'mid: {mid}')
    # return
    if ore_needed > target:
        return binary_search(lower, mid - 1, target, reactions)
    else:
        return binary_search(mid, upper, target, reactions)


# for i in range(1, 6):
#     filename = f'example{i}.txt'
#     reactions = tokenize(filename)
#     ans = make_fuel(reactions, 1)
#     print(ans)


# filename = '14/input.txt'
filename = 'input.txt'
reactions = tokenize(filename)
ans = make_fuel(reactions, 1)
print(f'part1: {ans}')
ans2 = make_fuel(reactions, 2690795)
# ans2 = binary_search(0, 10**12, 10**12, reactions)
# ans2 = binary_search(0, 100000, 10**12, reactions)
print(f'part2: {ans2}')
print(f'ore_left: {10**12 - ans2}')
