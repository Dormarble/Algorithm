from itertools import combinations
from copy import deepcopy
from collections import deque

mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def bfs(board, start):
    if board[start[0]][start[1]] == 1:
        return
    q = deque([start])
    board[start[0]][start[1]] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<n and 0<=ny and ny<m:
                if board[nx][ny] != 1:
                    board[nx][ny] = 1
                    q.append((nx, ny))
                    
        
empty = []
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))
            
ma = 0
for e3 in list(combinations(empty, 3)):
    b = deepcopy(board)
    for e in e3:
        b[e[0]][e[1]] = 1

    for v in virus:
        bfs(b, v)
    
    cnt = 0
    for x in range(n):
        for y in range(m):
            if b[x][y] == 0:
                cnt += 1

    ma = max(ma, cnt)

print(ma)
