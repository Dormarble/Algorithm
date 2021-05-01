import sys
sys.setrecursionlimit(10**6)

N = int(input())

dp = [-1]*(N+1)

def dfs(n):
    if n < 0:
        return 10000000
    if dp[n] > 0:
        return dp[n]
    if n==3 or n==5:
        return 1

    dp[n] = min(dfs(n-5), dfs(n-3)) + 1

    return dp[n]

result = dfs(N)
if result > 100000:
    result = -1

print(result)
