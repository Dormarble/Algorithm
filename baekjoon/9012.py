t = int(input())

for _ in range(t):
    ps = input()
    r = 0
    v = True
    for c in ps:
        if c == '(':
            r += 1
        else:
            r -= 1
        if r < 0:
            v = False
            break
    if r==0 and v:
        print('YES')
    else:
        print('NO')