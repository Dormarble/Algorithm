# 상하좌우
n = int(input())
c = list(map(str, input().split()))

cur = [1, 1]
d2t = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

for d in c:
    direction = d2t[d]
    next = [cur[0] + direction[0], cur[1] + direction[1]]

    if 1 <= next[0] and next[0] <= n:
        if 1 <= next[1] and next[1] <= n:
            cur = next

print(cur[0], cur[1])