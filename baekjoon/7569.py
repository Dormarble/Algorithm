from collections import deque

mx = [1, 0, 0, -1, 0, 0]
my = [0, 1, -1, 0, 0, 0]
mz = [0, 0, 0, 0, 1, -1]

M, N, H = map(int, input().split())

start = []
box = []
visit = []
for _ in range(H):
    visit.append([[0]*M for _ in range(N)])

for h in range(H):
    tmp = []
    for n in range(N):
        row = list(map(int, input().split()))
        for m, r in enumerate(row):
            if r == 1:
                start.append((h, n, m, 0))
        tmp.append(row)
        
    box.append(tmp)

result = 0
for s in start:
    visit[s[0]][s[1]][s[2]] = 1
q = deque(start)
while(q):
    x, y, z, c = q.popleft()

    for i in range(6):
        nx = x + mx[i]
        ny = y + my[i]
        nz = z + mz[i]

        if 0<=nx and nx<H and 0<=ny and ny<N and 0<=nz and nz<M:
            if visit[nx][ny][nz] == 0 and box[nx][ny][nz] == 0:
                visit[nx][ny][nz] = 1
                box[nx][ny][nz] = 1
                result = max(result, c+1)
                q.append((nx, ny, nz, c+1))

for i in range(H):
    if result < 0:
        break
    for j in range(N):
        if result < 0:
            break
        for k in range(M):
            if box[i][j][k] != -1 and visit[i][j][k] == 0:
                result = -1
                break

print(result)