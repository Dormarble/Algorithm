N = int(input())

board = []
for _ in range(N):
    board.append(input())

def bfs(board, visit, s, colors):
    n = len(board)
    mx = [1, 0, 0, -1]
    my = [0, 1, -1, 0]

    q = [s]
    visit[s[0]][s[1]] = 1
    while q:
        x, y = q.pop(0)
    
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<n and 0<=ny and ny<n:
                if visit[nx][ny] == 0 and board[nx][ny] in colors:
                    visit[nx][ny] = 1
                    q.append((nx, ny))


visit = [[0]*N for _ in range(N)]
a = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            bfs(board, visit, (i, j), board[i][j])
            a += 1


visit = [[0]*N for _ in range(N)]

b = 0
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            if board[i][j] in ('R', 'G'):
                bfs(board, visit, (i, j), ('R', 'G'))
            else:
                bfs(board, visit, (i, j), board[i][j])
            b += 1

print(a, b)