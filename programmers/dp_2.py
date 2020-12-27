dp = [[-1] * 501 for _ in range(501)]

def f(x, y, triangle):
    if dp[x][y] > 0:
        return dp[x][y]

    if x==len(triangle)-1:
        dp[x][y] = triangle[x][y]
        return dp[x][y]
    
    
    x1, y1 = x+1, y
    x2, y2 = x+1, y+1
    c1, c2 = 0, 0

    if 0<=x1 and 0<=y1 and y1<=x1:
        c1 = f(x1, y1, triangle)
    if 0<=x2 and 0<=y2 and y2<=x2:
        c2 = f(x2, y2, triangle)

    dp[x][y] = max(c1, c2) + triangle[x][y]

    return dp[x][y]

def solution(triangle):
    
    answer = f(0, 0, triangle)

    return answer



print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))