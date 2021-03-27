M, N, K = map(int, input().split())

board = [[0]*N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1

mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

def bfs(board, visit, x, y):
    q = [(x, y)]
    visit[x][y] = 1
    result = 1
    while q:
        x, y = q.pop(0)

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<M and 0<=ny and ny<N:
                if visit[nx][ny] == 0 and board[nx][ny] == 0:
                    result += 1 
                    visit[nx][ny] = 1
                    q.append((nx, ny))

    return result


visit = [[0]*N for _ in range(M)]

answer = []
for i in range(M):
    for j in range(N):
        if visit[i][j] == 0 and board[i][j] == 0:
            answer.append(bfs(board, visit, i, j))

answer.sort()

print(len(answer))
for i in answer:
    print(i, end=" ")