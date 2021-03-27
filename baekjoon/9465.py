T = int(input())

for _ in range(T):
    N = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))
    
    dp = [[0]*N for _ in range(2)]

    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    dp[0][1] = board[1][0] + board[0][1]
    dp[1][1] = board[0][0] + board[1][1]
    for i in range(2, N):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + board[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + board[1][i]

    print(max(dp[0][N-1], dp[1][N-1]))
    
