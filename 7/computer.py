import time


class Computer():
    def __init__(self, mem, inputs, number=0):
        self.mem = mem
        self.halted = False
        self.pc = 0
        self.inc = 4
        self.inputs = inputs
        self.outputs = []
        self.number = number

    def execute(self):
        print("start execution")
        while not self.halted:
            self.run()
            self.next()
        return 0

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
            while not len(self.inputs):
                None
            self.mem[self.mem[self.pc+1]] = self.inputs.pop(0)
            self.inc = 2
        elif opcode == 4:  # output
            self.output(self.get_para(1))
            print(
                f'number: {self.number}, outputs: {self.outputs}')
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

    def input(self, value):
        self.inputs.append(value)

    def output(self, value):
        self.outputs.append(value)
