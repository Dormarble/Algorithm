from collections import deque

n, m = map(int, input().split())
p = []
visit = []

result = 10000

for i in range(n):
    p.append(input())
mx = [0, 1]
my = [1, 0]



for a in range(n-7):
    for b in range(m-7):
        fir_w = 0
        fir_b = 0
        visit = [[0]*8 for _ in range(8)]

        pp = []
        for i in range(a, a+8):
            pp.append(p[i][b:b+8])

        q = deque()
        q.append((0, 0, 0))
        visit[0][0] = 1
        while q:
            x, y, l = q.popleft()
            if l % 2 == 0:
                if pp[x][y] == 'W':
                    fir_b += 1
                else:
                    fir_w += 1
            else:
                if pp[x][y] == 'W':
                    fir_w += 1
                else:
                    fir_b += 1

            for i in range(2):
                nx = x + mx[i]
                ny = y + my[i]

                if nx<8 and ny<8 and visit[nx][ny] == 0:
                    q.append((nx, ny, l+1))
                    visit[nx][ny] = 1

        mm = min(fir_w, fir_b)
        result = min(result, mm)
    
print(result)
