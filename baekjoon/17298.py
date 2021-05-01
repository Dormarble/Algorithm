import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [-1] * N

stack = []
for index, val in enumerate(arr):
    while stack:
        i, v = stack.pop()

        if v < val:
            result[i] = val
        else:
            stack.append((i, v))
            break
    
    stack.append((index, val))

for i in result:
    print(i, end=' ')