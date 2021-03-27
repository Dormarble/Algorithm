from itertools import combinations

T = int(input())

def f(n, m, dp):
    if n > m:
        dp[n][m] = 0
        return 0
    if n == 0:
        dp[n][m] = 0
        return 1
    
    if dp[n][m] > 0:
        return dp[n][m]
    
    for i in range(1, m+1):
        dp[n][m] += f(n-1, m-i, dp)
    return dp[n][m]

for _ in range(T):
    N, M = map(int, input().split())
    
    dp = [[0]*(M+1) for _ in range(N+1)]
    
    s = f(N, M, dp)

    print(int(s))
