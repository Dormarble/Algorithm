n, m = map(int, input().split())
b = []
for _ in range(n):
    b.append(input())

visit = [[0]*m for _ in range(n)]
mx = [0, 0, 1, -1]
my = [1, -1, 0, 0]

def dfs(x, y):
    visit[x][y] = 1

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if 0<=nx and nx<n and 0<=ny and ny<m:
            if visit[nx][ny] == 0 and b[nx][ny] == '0':
                dfs(nx, ny)

cnt = 0
for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and b[i][j] == '0':
            dfs(i, j)
            cnt += 1

print(cnt)

