t = int(input())
dp = [-1]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4

def f(n):
    if dp[n] != -1:
        return dp[n]
    
    dp[n] = f(n-1) + f(n-2) + f(n-3)
    return dp[n]

result = []
for _ in range(t):
    m = int(input())
    print(f(m))