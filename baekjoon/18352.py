import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [-1] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append(x)
distance[x] = 0
while q:
    cur = q.popleft()

    if distance[cur] > k:
        break
    
    for nx in graph[cur]:
        if distance[nx] == -1:
            distance[nx] = distance[cur] + 1
            q.append(nx)

check = True
for i in range(1, n+1):
    if distance[i] == k:
        check = False
        print(i)
if check:
    print(-1)