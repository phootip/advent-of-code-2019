start = 353096
end = 843212
ans = 0
for n in range(start, end+1):
    print(n)
    n = str(n)
    prev = '-1'
    double = False
    pair = False
    ascend = True
    for char in n:
        if char == prev:
            double = True
            if n.count(char) == 2:
                pair = True
        if int(char) < int(prev):
            ascend = False
            break
        prev = char
    if ascend and double and pair:
        ans += 1
print(ans)
# 302 too low
