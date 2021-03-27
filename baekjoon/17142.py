from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input().split()))

v = []
for i in range(N):
    for j in range(N):
        if board[i][j] == '2':
            v.append((i, j))


def bfs(board, vs):
    mx = [0, 0, -1, 1]
    my = [1, -1, 0, 0]

    history = [[0]*N for _ in range(N)] 
    visit = [[0]*N for _ in range(N)]
    q = []
    for v in vs:
        q.append((v[0], v[1], 0))
        visit[v[0]][v[1]] = 1

    result = 0
    while q:
        x, y, r = q.pop(0)
        
        result = max(result, r)
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<N and 0<=ny and ny<N:
                if board[nx][ny] != '1' and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    board[nx][ny] = '2'
                    history[nx][ny] = r+1
                    q.append((nx, ny, r+1))

    check = True
    for i in range(N):
        for j in range(N):
            if board[i][j] == '0':
                check = False

    return result, check

result = 10000000
check = False
for vs in combinations(v, M):
    b = deepcopy(board)
    r, c = bfs(b, vs)
    if c:
        check = True
        result = min(r, result)

    
if not check:
    print(-1)
else:
    print(result)
