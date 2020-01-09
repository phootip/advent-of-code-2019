import time


class Computer():
    def __init__(self, mem, inputs=[], number=0):
        self.mem = mem
        self.halted = False
        self.pc = 0
        self.inc = 4
        self.inputs = inputs
        self.outputs = []
        self.number = number
        self.relative_base = 0
        self.need_input = False

    def execute(self):
        # print("start execution")
        stop = False
        self.need_input = False
        while not self.halted:
            stop = self.run()
            self.next()
            if stop:
                break
        return

    def run(self):
        self.mode, opcode = self.get_inst()
        if opcode == 99:
            self.halted = True
        elif opcode == 1:  # plus
            self.setValue(self.writePos(3),
                          self.get_para(1) + self.get_para(2))
            self.inc = 4
        elif opcode == 2:  # multiply
            self.setValue(self.writePos(3),
                          self.get_para(1) * self.get_para(2))
            self.inc = 4
        elif opcode == 3:  # input
            if len(self.inputs) == 0:
                self.need_input = True
                return True
            self.setValue(self.writePos(1), self.inputs.pop(0))
            self.inc = 2
        elif opcode == 4:  # output
            self.output(self.get_para(1))
            self.inc = 2
            return True
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
                self.setValue(self.writePos(3), 1)
            else:
                self.setValue(self.writePos(3), 0)
            self.inc = 4
        elif opcode == 8:  # equal
            if(self.get_para(1) == self.get_para(2)):
                self.setValue(self.writePos(3), 1)
            else:
                self.setValue(self.writePos(3), 0)
            self.inc = 4
        elif opcode == 9:  # relative base offset
            self.relative_base += self.get_para(1)
            self.inc = 2

    def next(self):
        self.pc += self.inc

    def get_inst(self):
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
        if(mode == 0):  # position
            return self.getValue(self.mem[self.pc + pos])
        elif(mode == 1):  # instant
            return self.getValue(self.pc + pos)
        elif(mode == 2):  # relative
            return self.getValue(self.relative_base + self.mem[self.pc + pos])

    def writePos(self, pos):
        mode = self.mode[pos-1]
        if(mode == 0):  # position
            return self.mem[self.pc + pos]
        elif(mode == 1):  # instant
            return None
        elif(mode == 2):  # relative
            return self.relative_base + self.mem[self.pc + pos]

    def input(self, value):
        self.inputs.append(value)

    def output(self, value):
        self.outputs.append(value)

    def get_output(self):
        return self.outputs.pop(0)

    def setValue(self, position, value):
        if position >= len(self.mem):
            self.mem += [0 for i in range(position - len(self.mem) + 1)]
        self.mem[position] = value

    def getValue(self, position):
        if position >= len(self.mem):
            self.mem += [0 for i in range(position - len(self.mem) + 1)]
        return self.mem[position]
