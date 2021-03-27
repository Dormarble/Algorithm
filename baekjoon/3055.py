R, C = map(int, input().split())

mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

board = []
for _ in range(R):
    row = list(input())
    board.append(row)


def leak(board, visit, q):
    r = len(board)
    c = len(board[0])
    tmp_q = []
    while q:
        x, y = q.pop(0)
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx< r and 0<=ny and ny<c:
                if visit[nx][ny] == 0:
                    if board[nx][ny] == '.':
                        visit[nx][ny] = 1
                        board[nx][ny] = '*'
                        tmp_q.append((nx, ny))
    for a in tmp_q:
        q.append(a)

s_visit = [[0]*C for _ in range(R)]
w_visit = [[0]*C for _ in range(R)]

s_q = []
w_q = []
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            s_q.append((i, j, 0))
            s_visit[i][j] = 1
            board[i][j] = '.'

        elif board[i][j] == '*':
            w_q.append((i, j))
            w_visit[i][j] = 1

time = 0
while s_q:
    x, y, v = s_q.pop(0)

    if v == time:
        time += 1
        leak(board, w_visit, w_q)
    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if 0<=nx and nx< R and 0<=ny and ny<C:
            if s_visit[nx][ny] == 0:
                if board[nx][ny] == '.':
                    s_visit[nx][ny] = 1
                    s_q.append((nx, ny, v+1))
                elif board[nx][ny] == 'D':
                    print(v+1)
                    exit(0)

print("KAKTUS")