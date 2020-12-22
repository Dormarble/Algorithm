# 게임 개발
n, m = map(int, input().split())
a, b, d = map(int, input().split())
m = []
visit = []

mx = [-1, 0, 1, 0]
my = [0, 1, 0, -1]

for i in range(n):
    m.append(list(map(int, input().split())))
    visit.append([0] * n)

def turn_left(d, i):
    return (d-i) % 4

x, y = a, b
visit[x][y] = 1
while True:
    move = False
    for i in range(1, 5):
        tmp_d = turn_left(d, i)
        nx = x + mx[tmp_d]
        ny = y + my[tmp_d]

        if visit[nx][ny] == 0:
            if m[nx][ny] == 0:
                visit[nx][ny] = 1
                x, y = nx, ny
                move = True
                d = turn_left(d, i)
                break
    
    if not move:
        nx = x - mx[d]
        ny = y - my[d]

        if m[nx][ny] == 1:
            break;
        else:
            x, y = nx, ny
            visit[x][y] = 1
    
s = 0
for arr in visit:
    s += sum(arr)
print(s)