import sys
sys.setrecursionlimit(10**6)

mx = [0, 0, -1, 1]
my = [1, -1, 0, 0]

M, N = map(int, input().split())

board = []
for _ in range(M):
    board.append(list(map(int, input().split())))

dp = [[-1]*N for _ in range(M)]

def dfs(board, x, y):
    if x == M-1 and y == N-1:
        return 1
    
    if dp[x][y] != -1:
        return dp[x][y]

    if dp[x][y] == -1:
        dp[x][y] = 0

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if 0<=nx and nx<M and 0<=ny and ny<N:
            if board[x][y] > board[nx][ny]:
                dp[x][y] += dfs(board, nx, ny)

    return dp[x][y]


result = dfs(board, 0, 0)
print(result)