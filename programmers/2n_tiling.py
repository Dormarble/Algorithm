def solution(n):
    dp = [-1] * (n + 1)

    for i in range(2, n+1):
        if i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 3
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % 1000000007

    return dp[n]


print(solution(4))