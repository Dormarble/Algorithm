from collections import deque

mx = [0, 0, 1, -1]
my = [-1, 1, 0, 0]

def solution(m, n, puddles):
    board = [[0]*m for _ in range(n)]
    for puddle in puddles:
        board[puddle[1]-1][puddle[0]-1] = 1

    q = deque()
    c = [[0]*m for _ in range(n)]
    r = [[-1]*m for _ in range(n)]
    c[0][0] = 1         # 최단 경로 개수
    r[0][0] = 1         # 최단 거리
    q.append((0, 0))
    while q:
        x, y = q.popleft()       

        for i in range(4):
            nx = x + mx[i]
            ny = y + my[i]

            if 0<=nx and nx<n and 0<=ny and ny<m and board[nx][ny] == 0:
                if r[nx][ny] < 0:
                    r[nx][ny] = r[x][y] + 1
                    c[nx][ny] = c[x][y]
                    q.append((nx, ny))
                else:
                    if r[nx][ny] == r[x][y] + 1:
                        c[nx][ny] += c[x][y]
    
    return c[n-1][m-1] % 1000000007


print(solution(6, 5, [[2, 2], [3, 2], [1, 3], [5, 1], [5, 2], [5, 3], [3, 4], [4, 4]]))