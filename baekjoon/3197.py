import sys
input = sys.stdin.readline

R, C = map(int, input().split())

mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

start = []
board = []
for i in range(R):
    row = list(input())
    for j, r in enumerate(row):
        if r == 'L':
            start.append((i, j))
    board.append(row[:-1])

first = start[0]
secend = start[1]

q = []
visit = [[0]*C for _ in range(R)]
visit[first[0]][first[1]] = 1
visit[secend[0]][secend[1]] = 1
q.append((first[0], first[1], 1))
q.append((secend[0], secend[1], 2))

result = 0

tmp = ['a']
while tmp:
    tmp = []
    result += 1
    while q:
        x, y, t = q.pop(0)

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<R and 0<=ny and ny<C:
                if visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    if board[nx][ny] == '.':
                        q.append((nx, ny, t))
                        board[nx][ny] = str(t)
                    elif board[nx][ny] == 'X':
                        tmp.append((nx, ny, t))
                        board[nx][ny] = str(t)
                else:
                    if (board[nx][ny] == '1' and t == 2) or (board[nx][ny] == '2' and t == 1):
                        print(result)
                        exit(0)
    q = tmp
