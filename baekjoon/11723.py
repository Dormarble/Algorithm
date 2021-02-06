import sys

input = sys.stdin.readline

N = int(input())

def check(s, x):
    for i in s:
        if i == x:
            return 1
    else:
        return 0

s = set()
for _ in range(N):
    line = input().split()
    if len(line) == 1:
        cmd = line[0]
        if cmd == 'all':
            s = set(range(1, 21))
        else:
            s = set()
    else:
        cmd, x = line
        x = int(x)
        if cmd == 'add':
            s.add(x)
        elif cmd == 'remove':
            try:
                s.remove(x)
            except:
                pass
        elif cmd == 'check':
            print(check(s, x))
        else:
            if check(s, x) == 1:
                try:
                    s.remove(x)
                except:
                    pass
            else:
                s.add(x)
