from computer import Computer

f = open("input.txt")
# f = open("example.txt")
mem = list(map(int, f.readline().strip().split(',')))
c = Computer(mem)
c.execute()
