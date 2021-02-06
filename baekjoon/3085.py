N = int(input())

mx = [0, 1]
my = [1, 0]

board = []
for _ in range(N):
    row = input()
    r = []
    for c in row:
        if c == 'C':
            r.append(0)
        elif c == 'P':
            r.append(1)
        elif c == 'Z':
            r.append(2)
        else:
            r.append(3)
    board.append(r)

case = []
for x in range(N):
    for y in range(N):
        for k in range(2):
            nx = x + mx[k]
            ny = y + my[k]
            
            if 0<=nx and nx<N and 0<=ny and ny<N:
                if board[x][y] != board[nx][ny]:
                    case.append((x, y, nx, ny))

result = 0
for i in range(N):
    for k in range(4):
        cnt = 0
        for j in range(N):
            if board[i][j] == k:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 0

for i in range(N):
    for k in range(4):
        cnt = 0
        for j in range(N):
            if board[j][i] == k:
                cnt += 1
                result = max(result, cnt)
            else:
                cnt = 0

for x1, y1, x2, y2 in case:
    tmp = board[x1][y1] 
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = tmp

    s1 = 0
    cnt = 0
    for i in range(N):
        if board[i][y1] == board[x1][y1]:
            cnt += 1
            s1 = max(s1, cnt)
        else:
            cnt = 0

    
    s2 = 0
    cnt = 0
    for i in range(N):
        if board[x1][i] == board[x1][y1]:
            cnt += 1
            s2 = max(s2, cnt)
        else:
            cnt = 0

    s3 = 0
    cnt = 0
    for i in range(N):
        if board[i][y2] == board[x2][y2]:
            cnt += 1
            s3 = max(s3, cnt)
        else:
            cnt = 0
    
    
    s4 = 0
    cnt = 0
    for i in range(N):
        if board[x2][i] == board[x2][y2]:
            cnt += 1
            s4 = max(s4, cnt)
        else:
            cnt = 0

    s = max([s1, s2, s3, s4])
    result = max(s, result)

    tmp = board[x1][y1] 
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = tmp

print(result)