from itertools import combinations
from copy import deepcopy

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(str, input().split())))

empty = []
teacher = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            empty.append((i, j))
        elif board[i][j] == 'T':
            teacher.append((i, j))

detected = False
for o1, o2, o3 in combinations(empty, 3):
    detected = False

    b = deepcopy(board)
    b[o1[0]][o1[1]] = 'O'
    b[o2[0]][o2[1]] = 'O'
    b[o3[0]][o3[1]] = 'O'

    for t in teacher:
        x, y = t
        tmp_x = x
        tmp_y = y

        tmp_x += 1
        while tmp_x < N and b[tmp_x][y] != 'O':
            if b[tmp_x][y] == 'S':
                detected = True
            tmp_x += 1
        
        tmp_x -= 1
        while 0<=tmp_x and b[tmp_x][y] != 'O':
            if b[tmp_x][y] == 'S':
                detected = True
            tmp_x -= 1

        tmp_y += 1
        while tmp_y<N and b[x][tmp_y] != 'O':
            if b[x][tmp_y] == 'S':
                detected = True
            tmp_y += 1
        
        tmp_y -= 1
        while 0<=tmp_y and b[x][tmp_y] != 'O':
            if b[x][tmp_y] == 'S':
                detected = True
            tmp_y -= 1
        
        if detected:
            break
    
    if not detected:
        break
    

if detected:
    print("NO")
else:
    print("YES")