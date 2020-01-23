from time import time

def tokenize(data):
    inst = list(map(lambda x: x.strip().split(),data))
    return inst

def gen_deck(size):
    return list(range(size))

def deal_n(deck,n):
    deck_size = len(deck)
    new_deck = [0 for i in range(deck_size)]
    pos = n
    for i in range(deck_size):
        new_deck[(pos - n) % deck_size] = deck[i]
        pos += n
    return new_deck

def part1(deck,inst):
    while inst:
        order = inst.pop(0)
        # print(order)
        if order[:2] == ['deal','into']:
            deck = list(reversed(deck))
        elif order[:2] == ['deal','with']:
            n = int(order[-1])
            deck = deal_n(deck,n)
        elif order[0] == 'cut':
            n = int(order[-1])
            deck = deck[n:] + deck[:n]
        print(deck)
    return deck
    
start = time()

# f = open('example1.txt')
# f = open('example2.txt')
# f = open('example3.txt')
for i in range(1,5):
    f = open(f'example{i}.txt')
    # f = open('input.txt')
    data = f.readlines()
    inst = tokenize(data)
    deck_size = 10
    # deck_size = 10007
    deck = [i for i in range(deck_size)]
    print(deck)
    ans = part1(deck,inst)
    # print(ans.index(2019)) 
    # print(ans[2019]) 
    print(f'time used: {time() - start}')
    # print('5502 is too high')
    # print('1713 is too low')
    # break
