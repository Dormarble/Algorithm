import sys
import heapq

input = sys.stdin.readline
INF = 10e9

V, E = map(int, input().split())
k = int(input())

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        now, dist = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for n, d in graph[now]:
            cost = dist + d
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (n, cost))

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)

for i in range(1, V+1):
    print("INF" if distance[i] == INF else distance[i])