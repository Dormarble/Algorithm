import sys

input = sys.stdin.readline

N = int(input())
tower = list(map(int, input().split()))
result = [0]*N

stack = []
for idx, i in reversed(list(enumerate(tower))):
    while stack:
        index, val = stack.pop()
        if val <= i:
            result[index] = idx+1
        else:
            stack.append((index, val))
            break
    stack.append((idx, i))

for i in result:
    print(i, end=' ')