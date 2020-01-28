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
    x = int(gmpy.divm(pos,n,deck_size))
    # while (n * x) % deck_size != pos:
    #     x += 1
    return x

def prev_pos(pos,deck_size,inst,loop):
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
    pos = prev_pos(old_pos,deck_size,inst,loop-1)
    return pos
    
def next_pos(x, m , inst, times):
    while times > 0:
        times -= 1
        for order in inst: # f(x) = ax + b mod m
            if order[:2] == ['deal','into']:
                x = (- x - 1) % m # a=-1, b=-1
            elif order[:2] == ['deal','with']:
                n = int(order[-1])
                x = (n * x) % m # a=n, b=0
            elif order[0] == 'cut':
                n = int(order[-1])
                x = (x - n) % m # a=1, b=-n
    print(f'new_pos: {x}')
    
def compress_f(inst, m, times=1):
    a, b = 1,0
    for f in inst:
        # print(f'a,b: {a},{b}')
        if f[:2] == ['deal','into']:
            c = d = -1 # x = (- x - 1) % m
        elif f[:2] == ['deal','with']:
            n = int(f[-1])
            c,d = n, 0 # x = (n * x) % m
        elif f[0] == 'cut':
            n = int(f[-1])
            c, d = 1, -n # x = (x - n) % m
        
        a = (a*c) % m
        b = (b*c + d) % m
    # print(f'a,b: {a},{b}')
    k = times
    # A = (a**k) %   m
    A = pow(a,k,m)
    # B = (b*(1-a**k)/(1-a)) % m
    # B = ((b)*(A-1)/(a-1))
    # print(a)
    B = b * geometric(k,a,m)
    # print(B)
    return A,int(B)
def geometric(n,b,m):
    T=1
    e=b%m
    total = 0
    while n>0:
        if n&1==1:
            total = (e*total + T)%m
        T = ((e+1)*T)%m
        e = (e*e)%m
        n = n//2
        # //print '{} {} {}'.format(total,T,e)
    return total

def compress_f_inverse(inst, m, times=1):
    # print(inst)
    a, b = 1,0
    # for f in reversed(inst):
    #     print(f'inst: {f}')
    #     print(f'a,b: {a},{b}')
    #     if f[:2] == ['deal','into']:
    #         c = d = -1 # f(x) = (- x - 1) % m
    #     elif f[:2] == ['deal','with']:
    #         n = int(f[-1])
    #         c,d = gmpy.invert(n,m), 0 # f(x) = (n * x) % m # gmpy.divm(pos,n,deck_size)
    #     elif f[0] == 'cut':
    #         n = int(f[-1])
    #         c, d = 1, n # f(x) = (x + n) % m # (n + pos) % deck_size
        
    #     a = (a*c) % m
    #     b = (b*c + d) % m
    # print(f'a,b: {a},{b}')
    a = 114365604756913
    b = 109203610222234
    c = 1807813901728
    d = 0
    a = (a*c) % m
    b = (b*c + d) % m
    # print(f'a,b: {a},{b}')
    # 68621926557222, 41426505992898
    k = times
    # A = (a**k) % m
    # B = (b*(1-A)/(1-a)) % m
    A = pow(a,k,m)
    # B = b*((1-A)/(1-a)) % m
    B = b * geometric(k,a,m)
    return int(A),int(B)
    
def part2(pos, deck_size, inst, times):
    # 119315717514047
    # 12854400258724
    # for i in range(101741582076661):
    #     print(i)
    #     deck = prev_pos(deck,inst)
    c = 0
    while c < times:
        start = pos
        loop = len(inst) - 1
        new_pos = prev_pos(pos,deck_size,inst,loop)
        c += 1
        pos = new_pos
        # print(101741582076661 - c)
        # if new_pos == start:
        #     print(c)
        #     break
    # loop = 0
    # result = []
    # for i in range(10):
    #     ans = prev_pos(i,deck_size,inst,loop)
    #     result.append(ans)
    #     # print(f'ans: {ans}')
    # print(result)
    print(f'old_pos: {pos}')
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
# pos = 8611
# pos = 6343
# times = 1
deck_size = 119315717514047
pos = 2020
times = 101741582076661
# next_pos(pos,deck_size,inst,times)
# a,b = compress_f(inst, deck_size,times)
# print(f'compress_f: {(pos*a + b) % deck_size}')
# print(gmpy.invert(66,119315717514047))
# ans = part2(pos,deck_size,inst,times)
a,b = compress_f_inverse(inst, deck_size,times)
print(f'ans: {(pos*a + b) % deck_size}')
print('too low 14589521402977')
# print((pos*a + b))
# print(ans.index(2019)) 
print(f'time used: {time() - start}')
# print('2019 is at 2519')
