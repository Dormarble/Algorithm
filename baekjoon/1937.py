import sys
sys.setrecursionlimit(10**6)

N = int(input())

mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

field = []
dp = []
for _ in range(N):
    field.append(list(map(int, input().split())))
    dp.append([-1]*N)

def dfs(x, y):
    global dp
    global field

    if dp[x][y] >= 0:
        return dp[x][y]

    result = [0]
    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if 0<=nx and nx<N and 0<=ny and ny<N:
            if field[nx][ny] > field[x][y]:
                result.append(dfs(nx, ny))

    dp[x][y] = max(result) + 1
    return dp[x][y]


answer = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] < 0:
            answer = max(answer, dfs(i, j))


print(answer)