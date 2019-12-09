f = open("./input.txt")
# f = open("example.txt")
line1 = f.readline().strip().split(',')
line2 = f.readline().strip().split(',')
# print(line1, line2)


def draw():
    f = open('print.txt', 'a')
    for i in board:
        for j in range(len(i)):
            if isinstance(i[j], list):
                i[j] = '['+i[j][0] + ' ' + str(i[j][1])+']'
            # print(j)
        print(''.join(i))
        # print(i)
        # f.write(''.join(i) + '\n')


board = [['o']]
origin = [0, 0]
lines = [line1, line2]
for line in range(2):
    cor = origin[:]
    steps = [str(line), 0]
    for path in lines[line]:
        line = str(line)
        print(path)
        print(cor)
        direction = path[0]
        distant = int(path[1:])
        # switch case
        if direction == 'R':
            # expandBoard
            if cor[0] + distant >= len(board[0]):
                for y in board:
                    y += ['.' for k in range(cor[0] +
                                             distant - len(board[-1]) + 1)]
            # walk
            for i in range(distant):
                cor[0] += 1
                steps[1] += 1
                if board[cor[1]][cor[0]] == '.':
                    board[cor[1]][cor[0]] = steps[:]
                elif board[cor[1]][cor[0]][0] != line:
                    board[cor[1]][cor[0]] = [
                        '2', board[cor[1]][cor[0]][1] + steps[1]]
            # board[cor[1]][cor[0]] = '+'
        elif direction == 'D':
            # expandBoard
            if cor[1] + distant >= len(board):
                for i in range(cor[1] + distant - len(board) + 1):
                    board.append(['.' for j in range(len(board[0]))])
            # walk
            for i in range(distant):
                cor[1] += 1
                steps[1] += 1
                if board[cor[1]][cor[0]] == '.':
                    board[cor[1]][cor[0]] = steps[:]
                elif board[cor[1]][cor[0]][0] != line:
                    board[cor[1]][cor[0]] = [
                        '2', board[cor[1]][cor[0]][1] + steps[1]]
            # board[cor[1]][cor[0]] = '+'
        elif direction == 'L':
            # expandBoard
            if cor[0] - distant < 0:
                extra = -cor[0]+distant
                for y in board:
                    y[0:0] = ['.' for k in range(extra)]
                cor[0] += extra
                origin[0] += extra
            # walk
            for i in range(distant):
                cor[0] -= 1
                steps[1] += 1
                if board[cor[1]][cor[0]] == '.':
                    board[cor[1]][cor[0]] = steps[:]
                elif board[cor[1]][cor[0]][0] != line:
                    board[cor[1]][cor[0]] = [
                        '2', board[cor[1]][cor[0]][1] + steps[1]]
            # board[cor[1]][cor[0]] = '+'
        elif direction == 'U':
            # expandBoard
            if cor[1] - distant < 0:
                for i in range(- cor[1] + distant):
                    board.insert(0, ['.' for j in range(len(board[0]))])
                    cor[1] += 1
                    origin[1] += 1
            # walk
            for i in range(distant):
                cor[1] -= 1
                steps[1] += 1
                if board[cor[1]][cor[0]] == '.':
                    board[cor[1]][cor[0]] = steps[:]
                elif board[cor[1]][cor[0]][0] != line:
                    board[cor[1]][cor[0]] = [
                        '2', board[cor[1]][cor[0]][1] + steps[1]]
            # board[cor[1]][cor[0]] = '+'
# find answer
ans = 999999999
print(origin)
for y in range(len(board)):
    for x in range(len(board[0])):
        if board[y][x][0] == '2':
            ans = min(board[y][x][1], ans)
print(ans)
# draw()
