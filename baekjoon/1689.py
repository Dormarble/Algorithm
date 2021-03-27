import sys

input = sys.stdin.readline

points = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    points.append((a, 1))
    points.append((b, -1))

points.sort()

result = 0
cnt = 0
for p in points:
    cnt += p[1]
    result = max(cnt, result)

print(result)