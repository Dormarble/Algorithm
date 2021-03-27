import heapq

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

start = (0, 0)
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            start = (i, j)

mx = [-1, 0, 0, 1]
my = [0, -1, 1, 0]

def eat(board, start, size):
    N = len(board)
    s = (0, start[0], start[1])
    q = [s]
    visit = [[0]*N for _ in range(N)]
    visit[start[0]][start[1]] = 1
    board[start[0]][start[1]] = 0

    while q:
        t, x, y = heapq.heappop(q)
        
        if 0<board[x][y] and board[x][y]<size:
            board[x][y] = 9
            return (x, y, t)
        
        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<N and 0<=ny and ny<N:
                if visit[nx][ny] == 0 and board[nx][ny] <= size:
                    visit[nx][ny] = 1
                    heapq.heappush(q, (t+1, nx, ny))

    return (-1, -1, -1)


size = 2
feed = 0
t = 0
while True:
    next_start = eat(board, start, size)
    if next_start[0] == -1:
        break

    t += next_start[2]
    feed += 1
    if feed == size:
        size += 1
        feed = 0

    start = (next_start[0], next_start[1])
    
print(t)