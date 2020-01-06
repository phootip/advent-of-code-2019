class Node:
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value
        self.child = []

    def __str__(self):
        if not self.parent:
            return 'COM'
        return self.parent.value + ')' + self.value + '-' + ','.join([child.value for child in self.child])


nodes = []
unvisited = []
# f = open("example2.txt")
f = open("input.txt")
data = []


def tokenize(line):
    return line.strip().split(')')


def getNode(value):
    for node in nodes:
        if value == node.value:
            return node


for line in f:
    # [parent, child] = tokenize(line)
    data.append(tokenize(line))
for line in data:
    if line[0] == 'COM':
        root = Node(line[0], None)
        child = Node(line[1], root)
        root.child.append(child)
        nodes.append(root)
        nodes.append(child)
        unvisited = [child]
        data.remove(line)
        break


while unvisited:
    node = unvisited.pop()
    for line in data:
        if line[0] == node.value:
            [parent, child] = line
            new_node = Node(child, node)
            nodes.append(new_node)
            print([parent, child])
            node.child.append(new_node)
            unvisited.append(new_node)


# for node in nodes:
#     print(node)


# def cal(node, acc):
#     if not node.child:
#         print(f'node: {node.value}, {acc}')
#         return acc
#     else:
#         result = 0
#         for child in node.child:
#             result += cal(child, acc+1)
#         return result + acc
print(root)


def getDistant(node):
    c = 0
    while node.parent:
        node = node.parent
        c += 1
    # print(c)
    return c


def cal2():
    s = getNode('SAN')
    y = getNode('YOU')
    path_s = s.parent
    path_y = y.parent
    while path_s != path_y:
        if path_s != root:
            path_s = path_s.parent
            # print(path_s)
        else:
            path_s = s.parent
            path_y = path_y.parent
    dis_s = getDistant(s)
    dis_y = getDistant(y)
    return dis_s + dis_y - getDistant(path_s)*2 - 2


result = cal2()
print(result)
