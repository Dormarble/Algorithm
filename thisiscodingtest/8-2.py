n = int(input())
k = list(map(int, input().split()))

dp = [0] * n

def f(n):
    if n == 0 or n == 1:
        dp[n] = k[n]
        return dp[n]
    elif n == 2:
        dp[n] = max(k[0] + k[2], k[1])
        return dp[n]

    n1 = f(n-2) + k[n]
    n2 = f(n-1)

    dp[n] = max([n1, n2])

    return dp[n]

print(f(n-1))