from itertools import combinations
from copy import deepcopy

def bfs(board, s):
    mx = [0, 0, -1, 1]
    my = [-1, 1, 0, 0]
    
    q = [s]
    while q:
        x, y = q.pop()
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<N and 0<=ny and ny<M:
                if board[nx][ny] == 0:
                    board[nx][ny] = 2
                    q.append((nx, ny))


N, M = map(int, input().split())

board = []
empty = []
start = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            empty.append((i, j))
        elif board[i][j] == 2:
            start.append((i, j))

m = 0
for w in combinations(empty, 3):
    b = deepcopy(board)
    for i, j in w:
        b[i][j] = 1

    for s in start:
        bfs(b, s)

    su = 0
    for i in range(N):
        for j in range(M):
            if b[i][j] == 0:
                su += 1

    m = max(su, m)

print(m)


    
