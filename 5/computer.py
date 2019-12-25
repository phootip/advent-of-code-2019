class Computer():
    def __init__(self, mem):
        self.mem = mem
        self.halted = False
        self.pc = 0
        self.inc = 4

    def execute(self):
        print("start execution")
        while not self.halted:
            self.run()
            self.next()
        # return 0

    def run(self):
        self.mode, opcode = self.get_inst()
        if opcode == 99:
            self.halted = True
            return
        elif opcode == 1:  # plus
            self.mem[self.mem[self.pc+3]
                     ] = self.get_para(1) + self.get_para(2)
            self.inc = 4
        elif opcode == 2:  # multiply
            self.mem[self.mem[self.pc+3]
                     ] = self.get_para(1) * self.get_para(2)
            self.inc = 4
        elif opcode == 3:  # input
            a = int(input("please give input >>> "))
            self.mem[self.mem[self.pc+1]] = a
            self.inc = 2
        elif opcode == 4:  # output
            print("output >> " + str(self.get_para(1)))
            self.inc = 2
        elif opcode == 5:  # jump-if-true
            if(self.get_para(1) != 0):
                self.pc = self.get_para(2)
                self.inc = 0
            else:
                self.inc = 3
        elif opcode == 6:  # jump-if-false
            if(self.get_para(1) == 0):
                self.pc = self.get_para(2)
                self.inc = 0
            else:
                self.inc = 3
        elif opcode == 7:  # less than
            if(self.get_para(1) < self.get_para(2)):
                self.mem[self.mem[self.pc+3]] = 1
            else:
                self.mem[self.mem[self.pc+3]] = 0
            self.inc = 4
        elif opcode == 8:  # equal
            if(self.get_para(1) == self.get_para(2)):
                self.mem[self.mem[self.pc+3]] = 1
            else:
                self.mem[self.mem[self.pc+3]] = 0
            self.inc = 4

    def next(self):
        self.pc += self.inc

    def get_inst(self):
        # print(self.pc)
        opcode = self.mem[self.pc]
        opcode = str(opcode)
        opcode = '0'*(5 - len(opcode)) + opcode
        opcode = list(opcode)
        opcode[-1] = opcode[-2] + opcode.pop()
        opcode = list(map(int, opcode))
        mode = [opcode.pop(2), opcode.pop(1), opcode.pop(0)]
        opcode = opcode.pop()
        return [mode, opcode]

    def get_para(self, pos):
        mode = self.mode[pos-1]
        if(mode == 0):
            return self.mem[self.mem[self.pc + pos]]
        else:
            return self.mem[self.pc + pos]
