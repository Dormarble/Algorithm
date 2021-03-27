N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

dp = [0] * (K+1)

dp[0] = 1

for c in coins:
    for j in range(c, K+1):
        dp[j] += dp[j-c]
print(dp[K])
    