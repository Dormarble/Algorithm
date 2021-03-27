import heapq

import sys

input = sys.stdin.readline

N = int(input())
c = [0] * 20001

min_q = []
max_q = []

t = int(input())
print(t)
heapq.heappush(max_q, -t)

for _ in range(1, N):
    i = int(input())
    if i <= -max_q[0]:
        heapq.heappush(max_q, -i)
    else:
        heapq.heappush(min_q, i)

    if len(max_q) < len(min_q):
        heapq.heappush(max_q, -heapq.heappop(min_q))
    elif len(max_q) > len(min_q) + 1:
        heapq.heappush(min_q, -heapq.heappop(max_q))
    print(-max_q[0])
