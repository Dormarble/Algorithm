import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()
for _ in range(n):
    line = input().split()
    if len(line) == 2:
        cmd, i = line
        if cmd == 'push_back':
            q.append(i)
        else:
            q.appendleft(i)
    else:
        cmd = line[0]
        if cmd == 'pop_front':
            if not q:
                print(-1)
            else:
                print(q.popleft())
        elif cmd == 'pop_back':
            if not q:
                print(-1)
            else:
                print(q.pop())
        elif cmd == 'size':
            print(len(q))
        elif cmd == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif cmd == 'front':
            if not q:
                print(-1)
            else:
                print(q[0])
        else:
            if not q:
                print(-1)
            else:
                print(q[-1])
