from tokenizer import tokenize
f = open("input.txt")
# f = open("example.txt")
mem = list(map(int, f.readline().strip().split(',')))
pos = 0

while True:
    # compute()
    opcode = mem[pos]
    [A, B, C, opcode] = tokenize(opcode)
    mode = [A, B, C]
    # print(A, B, C, opcode)
    inc = 4
    if(opcode <= 2):
        if(A == 1):
            A = mem[pos+3]
        else:
            A = mem[mem[pos+3]]
        if(B == 1):
            B = mem[pos+2]
        else:
            B = mem[mem[pos+2]]
    if(opcode != 99):
        if(C == 1):
            C = mem[pos+1]
        else:
            C = mem[mem[pos+1]]

    if opcode == 99:
        break
    elif opcode == 1:
        mem[mem[pos+3]] = C + B
        # print('opcode 1, ' + str(C) + " " +
        #       str(B) + " " + str(mem[pos+3]))
    elif opcode == 2:
        mem[mem[pos+3]] = C * B
        # print('opcode 2, ' + str(C) + " " +
        #       str(B) + " " + str(mem[pos+3]))
    elif opcode == 3:
        # a = int(input("please give input >>> "))
        a = 1
        C = a
        inc = 2
    elif opcode == 4:
        print("output >> " + str(C))
        # break
        inc = 2
    # next()
    pos += inc
    # print(mem)

# print(mem[0])
