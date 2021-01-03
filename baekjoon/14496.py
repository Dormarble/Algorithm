import sys
import heapq
input = sys.stdin.readline

a, b = map(int, input().split())
n, m = map(int, input().split())

graph = [[] for i in range(n+1)]
for i in range(m):
    t1, t2 = map(int, input().split())
    graph[t1].append(t2)
    graph[t2].append(t1)

INF = 1e9
q = []
distance = [INF] * (n+1)

heapq.heappush(q, (0, a))
distance[a] = 0
while q:
    dist, now = heapq.heappop(q)

    if dist > distance[now]:
        continue

    for i in graph[now]:
        cost = dist + 1
        if cost < distance[i]:
            distance[i] = cost
            heapq.heappush(q, (cost, i))

if distance[b] != INF:
    print(distance[b])
else:
    print(-1)