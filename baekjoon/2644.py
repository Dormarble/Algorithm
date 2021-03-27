N = int(input())
A, B = map(int, input().split())
A -= 1
B -= 1
M = int(input())

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

result = 0

visit = [0]*N
visit[A] = 1
q = [(A, 0)]
while q:
    c, r = q.pop(0)
    if c == B:
        result = r
        break

    for n in graph[c]:
        if visit[n] == 0:
            visit[n] = 1
            q.append((n, r+1))

if result == 0:
    print(-1)
else:
    print(result)