def count_zero(layer):
    return layer.count('0')


# f = open('example.txt')
# width = 3
# height = 2
f = open('input.txt')
width = 25
height = 6

data = f.readline().strip()
size = width * height
mem = []
while data:
    mem.append(data[:size])
    data = data[size:]

fewest_zero = min(mem, key=count_zero)
# print(fewest_zero)
print(fewest_zero.count('1') * fewest_zero.count('2'))
