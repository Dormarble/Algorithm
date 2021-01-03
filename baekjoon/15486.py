dp = [0]*1500001

n = int(input())

for i in range(n):
    ti, pi = map(int, input().split())
    if i > 0:
        dp[i] = max(dp[i], dp[i-1])

    if i+ti > n:
        continue
    else:
        dp[i+ti] = max(dp[i+ti], dp[i] + pi)

dp[n] = max(dp[n-1], dp[n])

print(dp[n])