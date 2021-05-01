from collections import deque

mx = [0, 0, 1, -1, -1, 1, -1, 1]
my = [1, -1, 0, 0, 1, 1, -1, -1]

while(True):
    w, h = map(int, input().split())
    if(w == 0 and h == 0):
        break

    result = 0
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))

    visit = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and board[i][j] == 1:
                visit[i][j] = 1
                result += 1
                q = deque([(i, j)])
                while(q):
                    x, y = q.popleft()
                    
                    for n in range(8):
                        nx = x + mx[n]
                        ny = y + my[n]

                        if 0<=nx and nx<h and 0<=ny and ny<w:
                            if visit[nx][ny] == 0 and board[nx][ny] == 1:
                                visit[nx][ny] = 1
                                q.append((nx, ny))

    print(result)
