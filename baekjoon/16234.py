from copy import deepcopy
from collections import deque

N, L, R = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
    
mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

def bfs(x, y, visit):
    group = [(x, y)]
    total = board[x][y]

    q = deque([(x, y)])
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if visit[nx][ny] == 0:
                    diff = abs(board[nx][ny] - board[x][y])
                    if L <= diff and diff <= R:
                        visit[nx][ny] = 1
                        group.append((nx, ny))
                        total += board[nx][ny]
                        q.append((nx, ny))
    
    return total, group

step = 0
while True:
    visit = [[0]*N for _ in range(N)]
    groups = []
    totals = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                total, group = bfs(i, j, visit)
                totals.append(total)
                groups.append(group)

    if len(totals) == N*N:
        break
    else:
        for total, group in zip(totals, groups):
            for x, y in group:
                board[x][y] = total // len(group)
        step += 1
print(step)