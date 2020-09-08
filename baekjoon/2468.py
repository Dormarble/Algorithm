import sys

sys.setrecursionlimit(10**6)

n = int(input())
box = []
visit = [[0]*n for _ in range(n)]
for _ in range(n):
    box.append(list(map(int, input().split())))

mx = [1, 0, 0, -1]
my = [0, -1, 1, 0]

def dfs(curX, curY, height):
    visit[curX][curY] = 1
    
    for i in range(4):
        nextX = curX + mx[i]
        nextY = curY + my[i]
        if 0<=nextX and nextX<n and 0<=nextY and nextY<n:
            if box[nextX][nextY] > height and visit[nextX][nextY] == 0:
                dfs(nextX, nextY, height)

answer = 0
for h in range(101):
    safeNum = 0
    visit = [[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            if box[a][b] > h and not visit[a][b]:
                safeNum += 1
                dfs(a, b, h)
    answer = max(answer, safeNum)


print(answer)
