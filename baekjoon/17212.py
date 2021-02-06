N = int(input())

dp = [-1] * (100001)

dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 2
dp[4] = 2
dp[5] = 1
dp[6] = 2
dp[7] = 1
for i in range(8, N+1):
    c1 = dp[i-1] + 1
    c2 = dp[i-2] + 1
    c3 = dp[i-3] + 2
    c4 = dp[i-4] + 2
    c5 = dp[i-5] + 1
    c6 = dp[i-6] + 2
    c7 = dp[i-7] + 1
    
    dp[i] = min([c1, c2, c3, c4, c5, c6, c7])

print(dp[N])