from computer import Computer

f = open('input.txt')
# f = open('example.txt')
program = list(map(int, f.readline().strip().split(',')))
com = Computer(program[:], [1])
com.execute()
# print(program)
# print(com.outputs)
# print(len(str(com.outputs[0])))
for output in com.outputs:
    print(output)

com = Computer(program[:], [2])
com.execute()
print(com.outputs)
