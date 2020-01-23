from time import time

def tokenize(data):
    inst = list(map(lambda x: x.strip().split(),data))
    return inst

def gen_deck(size):
    return list(range(size))

def deal_n(pos,deck_size,value,n):
    # new_pos = (n * pos) % deck_size
    x = 0
    while (n * x) % deck_size != pos:
        x += 1
    return x
# 0 1 2 3 4 5 6 7 8 9
# 0 3 6 . 2 5 . 1 4 .
# (7 * 3) % 10 => 1
# (7 * 2) % 10 => 4
# (7 * 1) % 10 => 7
# (3 * _) % 10 => 2
def shuffle(pos,deck_size,inst):
    value = pos
    while inst:
        order = inst.pop(0)
        if order[:2] == ['deal','into']:
            value = deck_size - value - 1
        elif order[:2] == ['deal','with']:
            n = int(order[-1])
            value = deal_n(pos,deck_size,value,n)
        elif order[0] == 'cut':
            n = int(order[-1])
            value = value + n
        print(f'value: {value}')
        # break
    return value
    
def part2(pos, deck_size,inst):
    # for i in range(101741582076661):
    #     print(i)
    #     deck = shuffle(deck,inst)
    print(pos, deck_size)
    pos = shuffle(pos,deck_size,inst)
    print(pos)
    return

start = time()

# f = open('example1.txt')
f = open('example2.txt')
# f = open('input.txt')
data = f.readlines()
inst = tokenize(data)
deck_size = 10
pos = 0
# deck_size = 10007
# pos = 2019
# deck_size = 119315717514047
# pos = 2020
ans = part2(pos,deck_size,inst)
# print(ans.index(2019)) 
print(ans)
print(f'time used: {time() - start}')
print('2519 is at 2019')
