class Node:
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value
        self.child = []

    def __str__(self):
        if not self.parent:
            self.parent = "None"
        return self.parent + ')' + self.value + '-' + ','.join([child.value for child in self.child])


nodes = []
unvisited = []
# f = open("example.txt")
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
        child = Node(line[1], line[0])
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
            new_node = Node(child, parent)
            nodes.append(new_node)
            print([parent, child])
            node.child.append(new_node)
            unvisited.append(new_node)


# for node in nodes:
#     print(node)


def cal(node, acc):
    if not node.child:
        print(f'node: {node.value}, {acc}')
        return acc
    else:
        result = 0
        for child in node.child:
            result += cal(child, acc+1)
        return result + acc


result = cal(root, 0)
print(result)
