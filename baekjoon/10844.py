N = int(input())

dp = [[0] * 10 for _ in range(N)]

for i in range(1, 10):
    dp[0][i] = 1

for i in range(1, N):
    for j in range(10):
        left_idx = j-1
        right_idx = j+1
        if left_idx >= 0:
            dp[i][j] += dp[i-1][left_idx]
        if right_idx < 10:
            dp[i][j] += dp[i-1][right_idx]

sum = 0
for i in range(10):
    sum += dp[N-1][i]

print(sum % 1000000000)