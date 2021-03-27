import heapq

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input())

mx = [0, 0, -1, 1]
my = [-1, 1, 0, 0]

q = [(1, 0, 0, 0)]
visit_0 = [[0]*M for _ in range(N)]
visit_1 = [[0]*M for _ in range(N)]
visit_0[0][0] = 1

answer = 0
while q:
    c, b, x, y = heapq.heappop(q)
    if x == N-1 and y == M-1:
        answer = c
        break

    for i in range(4):
        nx = x + mx[i]
        ny = y + my[i]

        if 0<=nx and nx<N and 0<=ny and ny<M:
            if board[nx][ny] == '0':
                if visit_0[nx][ny] == 0 and b==0:
                    visit_0[nx][ny] = 1
                    heapq.heappush(q, (c+1, b, nx, ny))
                elif visit_1[nx][ny] == 0 and b==1:
                    visit_1[nx][ny] = 1
                    heapq.heappush(q, (c+1, b, nx, ny))                
            elif board[nx][ny] == '1' and visit_1[nx][ny] == 0 and b == 0:
                visit_1[nx][ny] = 1
                heapq.heappush(q, (c+1, 1, nx, ny))

if answer == 0:
    print(-1)
else:
    print(answer)
