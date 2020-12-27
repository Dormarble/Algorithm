dp = [1000000000] * 30001

def f(n):
    if n == 1:
        return 0
    
    if dp[n] != 1000000000:
        return dp[n]

    if n % 5 == 0:
        dp[n] = min(dp[n], f(int(n/5)) + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], f(int(n/3)) + 1)
    if n % 2 == 0:
        dp[n] = min(dp[n], f(int(n/2)) + 1)
    dp[n] = min(dp[n], f(n-1) + 1)
    
    return dp[n]

n = int(input())

print(f(n))