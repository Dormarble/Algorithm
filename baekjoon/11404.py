import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[100000000]*N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    a-=1
    b-=1
    graph[a][b] = min(graph[a][b], c)

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for g in graph:
    for i in g:
        if i == 100000000:
            print(0, end=' ')
        else:
            print(i, end=' ')
    print()