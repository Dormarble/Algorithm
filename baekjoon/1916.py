import sys
import heapq

input = sys.stdin.readline
INF = 10e9

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

s, e = map(int, input().split())

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (start, 0))
    distance[start] = 0
    while q:
        now, dist = heapq.heappop(q)
        
        if dist > distance[now]:
            continue

        for i, d in graph[now]:
            cost = dist + d
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (i, cost))

    return distance

distance = dijkstra(s)

print(distance[e])