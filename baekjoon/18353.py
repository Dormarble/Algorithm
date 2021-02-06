N = int(input())
a = list(map(int, input().split()))

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)

result = 0
for i in range(N):
    result = max(result, dp[i])
print(N - result)