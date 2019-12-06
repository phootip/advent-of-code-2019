for i in range(100):
    for j in range(100):
        f = open("input.txt")
        # f = open("example.txt")
        mem = list(map(int, f.readline().strip().split(',')))
        noun = i
        verb = j
        mem[1] = noun
        mem[2] = verb
        print(mem)
        pos_opcode = 0
        pos1 = 1
        pos2 = 2
        pos3 = 3

        while True:
            # compute()

            if mem[pos_opcode] == 99:
                break
            elif mem[pos_opcode] == 1:
                mem[mem[pos3]] = mem[mem[pos1]] + mem[mem[pos2]]
            elif mem[pos_opcode] == 2:
                mem[mem[pos3]] = mem[mem[pos1]] * mem[mem[pos2]]

            # next()
            pos_opcode += 4
            pos1 += 4
            pos2 += 4
            pos3 += 4
            # print(mem)
        print(mem[0])
        if(mem[0] == 19690720):
            print(100 * noun + verb)
            exit()
