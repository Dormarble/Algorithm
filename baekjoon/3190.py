ma = [-1, 0, 1, 0]
mb = [0, 1, 0, -1]

n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1

L = int(input())
x = {}
for _ in range(L):
    X, C = input().split()
    x[int(X)] = C

snake = []
sec = 0
snake.append((0, 0))
d = 1
a, b = 0, 0
while True:
    sec += 1
    na = a + ma[d]
    nb = b + mb[d]
    
    if not(0<=na and na<n and 0<=nb and nb<n):
        break
    if (na, nb) in snake:
        break
    if board[na][nb] == 1:
        board[na][nb] = 0
    else:
        snake.pop(0)

    snake.append((na, nb))
    a, b = na, nb
    if sec in x:
        if x[sec] == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4

print(sec)