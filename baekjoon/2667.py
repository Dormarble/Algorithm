n = int(input())
m = []
visit = [[False]*n for _ in range(n)]
result = []
num = 0

for _ in range(n):
    m.append(input())
    
moveX = [0, 0, 1, -1]
moveY = [1, -1, 0, 0]

def dfs(curX, curY):
    global num
    visit[curX][curY] = True
    num += 1
    for i in range(4):
        nextX = moveX[i] + curX
        nextY = moveY[i] + curY
        
        if 0<=nextX and nextX<n:
            if 0<=nextY and nextY<n:
                if m[nextX][nextY] == '1':
                    if not visit[nextX][nextY]:
                        dfs(nextX, nextY)

for a in range(n):
    for b in range(n):
        if m[a][b] == '1':
            if not visit[a][b]:
                num = 0
                dfs(a, b)
                result.append(num)

result.sort()
print(len(result))
for i in result:
    print(i)
