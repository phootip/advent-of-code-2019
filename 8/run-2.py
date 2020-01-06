from PIL import Image, ImageColor


def count_zero(layer):
    return layer.count('0')


# f = open('example2.txt')
# width = 2
# height = 2
f = open('input.txt')
width = 25
height = 6
im = Image.new('1', (width, height))  # create the Image of size 1 pixel

data = f.readline().strip()
size = width * height
mem = []
while data:
    mem.append(data[:size])
    data = data[size:]

image = list(mem.pop(0))
while mem:
    next_layer = list(mem.pop(0))
    for pixel in range(len(image)):
        if image[pixel] == '2':
            image[pixel] = next_layer[pixel]

for h in range(height):
    layer = image[:width]
    for w in range(width):
        if layer[w] == '0':
            # or whatever color you wish
            im.putpixel((w, h), ImageColor.getcolor('black', '1'))
        else:
            # or whatever color you wish
            im.putpixel((w, h), ImageColor.getcolor('white', '1'))
    print(''.join(layer))
    image = image[width:]

im.save('simplePixel.png')
