def tokenize(opcode):
    opcode = str(opcode)
    opcode = '0'*(5 - len(opcode)) + opcode
    opcode = list(opcode)
    opcode[-1] = opcode[-2] + opcode.pop()
    return list(map(int, opcode))

# tokenize(1032)
