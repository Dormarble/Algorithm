dp = [-1] * 1000001

def rot(money):
    for n in range(len(money)):
        if n == 0:
            dp[n] = money[n]
            continue
        if n == 1:
            dp[n] = max(money[0], money[1])
            continue

        dp[n] = max(dp[n-1], dp[n-2] + money[n])
    
    return dp[len(money)-1]

        

def solution(money):
    global dp
    money_1 = money[:-1]
    money_2 = money[1:]
    dp = [-1] * 1000001
    result_1 = rot(money_1)

    dp = [-1] * 1000001
    result_2 = rot(money_2)
    
    return max(result_1, result_2)

print(solution([1, 2, 3, 4, 5]))