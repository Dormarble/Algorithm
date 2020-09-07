from collections import deque

m, n = map(int, input().split())
box = []
visit = [[False]*m for _ in range(n)]

moveX = [0, 0, 1, -1]
moveY = [-1, 1, 0, 0]

for _ in range(n):
    box.append(input().split())

for i in range(n):
    for j in range(m):
        if box[i][j] == '-1':
            visit[i][j] = True

q = deque([])
for i in range(n):
    for j in range(m):
        if box[i][j] == '1':
            q.append((i, j))
            visit[i][j] = True
tmp = []
answer = 0
while q:
    curX, curY = q.popleft()
    
    for i in range(4):
        nextX = curX + moveX[i]
        nextY = curY + moveY[i]
        
        if 0<=nextX and nextX<n and 0<=nextY and nextY<m:
            if not visit[nextX][nextY]:
                tmp.append((nextX, nextY))
                visit[nextX][nextY] = True

    if not q:
        q = deque(tmp)
        tmp = []
        answer += 1

answer -= 1

for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            answer = -1
            
print(answer)
