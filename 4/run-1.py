start = 353096
end = 843212
ans = 0
for n in range(start, end+1):
    print(n)
    n = str(n)
    prev = '-1'
    double = False
    ascend = True
    for char in n:
        if char == prev:
            double = True
        if int(char) < int(prev):
            ascend = False
        prev = char
    if ascend and double:
        ans += 1
print(ans)
