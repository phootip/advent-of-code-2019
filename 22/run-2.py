from time import time
import gmpy
mem = {}

def tokenize(data):
    inst = list(map(lambda x: x.strip().split(),data))
    return inst

def gen_deck(size):
    return list(range(size))

def deal_n(pos,deck_size,n):
    # new_pos = (n * pos) % deck_size
    x = 0
    # x = modinv(n,deck_size,pos)
    x = int(gmpy.divm(pos,n,deck_size))
    # while (n * x) % deck_size != pos:
    #     x += 1
    return x
# 0 1 2 3 4 5 6 7 8 9
# 0 3 6 . 2 5 . 1 4 .
# (7 * 3) % 10 => 1
# (7 * 2) % 10 => 4
# (7 * 1) % 10 => 7
# (3 * _) % 10 => 2
def shuffle(pos,deck_size,inst,loop):
    # print(f'pos, loop: {pos}, {loop}')
    if loop < 0:
        return pos
    order = inst[loop]
    if order[:2] == ['deal','into']:
        old_pos = deck_size - pos - 1
    elif order[:2] == ['deal','with']:
        n = int(order[-1])
        old_pos = deal_n(pos,deck_size,n)
    elif order[0] == 'cut':
        n = int(order[-1])
        old_pos = (n + pos) % deck_size
    # print(f'old_pos: {old_pos}')
    pos = shuffle(old_pos,deck_size,inst,loop-1)
    return pos
    
def part2(pos, deck_size,inst):
    # 119315717514047
    # 12854400258724
    # for i in range(101741582076661):
    #     print(i)
    #     deck = shuffle(deck,inst)
    start = pos
    print(f'pos, deck_size: {pos}, {deck_size}')
    loop = len(inst) - 1
    new_pos = shuffle(pos,deck_size,inst,loop)
    print(new_pos)
    # mem[pos] = new_pos
    # if new_pos == start:
    #     print(len(mem))
    #     break
    # loop = 0
    # result = []
    # for i in range(10):
    #     ans = shuffle(i,deck_size,inst,loop)
    #     result.append(ans)
    #     print(f'ans: {ans}')
    # print(result)
    return

start = time()

# f = open('example1.txt')
# f = open('example2.txt')
# f = open('example3.txt')
# f = open('example4.txt')
f = open('input.txt')
data = f.readlines()
inst = tokenize(data)
# deck_size = 10
# pos = 1
# deck_size = 10007
# pos = 2519
deck_size = 119315717514047
pos = 2020
ans = part2(pos,deck_size,inst)
# print(ans.index(2019)) 
print(f'time used: {time() - start}')
# print('2019 is at 2519')
