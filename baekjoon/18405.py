import sys
from collections import deque

input = sys.stdin.readline

mx = [0, 0, 1, -1]
my = [-1, 1, 0, 0]

n, k = map(int, input().split())
board = []
virus = [[] for _ in range(k+1)]
for i in range(n):
    board.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            virus[board[i][j]].append((i, j))

q = deque()
for i in range(1, k+1):
    for coor in virus[i]:
        q.append(coor)

for _ in range(S):
    tmp_q = deque()
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<n and 0<=ny and ny<n:
                if board[nx][ny] == 0:
                    board[nx][ny] = board[x][y]
                    tmp_q.append((nx, ny))
    q = tmp_q

print(board[X-1][Y-1])
    