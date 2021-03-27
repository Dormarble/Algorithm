N, K = map(int, input().split())
Ws = []
Vs = []
for _ in range(N):
    w, v = map(int, input().split())
    Ws.append(w)
    Vs.append(v)

dp = [[0]*N for _ in range(K+1)]

for n in range(N):
    for k in range(1, K+1):
        w = Ws[n]
        v = Vs[n]
        dp[k][n] = dp[k][n-1]
        if k >= w:
            dp[k][n] = max(dp[k-w][n-1] + v, dp[k][n])

print(dp[K][N-1])