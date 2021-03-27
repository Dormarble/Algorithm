N = int(input())
cards = list(map(int, input().split()))

dp = [0]*(N+1)

for k in range(1, N+1):
    for n, c in enumerate(cards):
        n += 1
        if k-n >= 0:
            dp[k] = max(dp[k-n] + c, dp[k])

print(dp[N])
