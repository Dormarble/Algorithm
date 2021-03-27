def main():
    T = int(input())

    for _ in range(T):
        M, N = map(int, input().split())
        board = []
        for i in range(M):
            row = list(map(int, input().split()))

            for j in range(len(row)):
                if row[j] == 2:
                    dest = (i, j)
                if row[j] == 3:
                    start = (i, j)
                if row[j] == 4:
                    key = (i, j)
            board.append(row)

        mx = [0, 0, -1, 1]
        my = [1, -1, 0, 0]

        visit = [[0]*N for _ in range(M)]

        q = [start]
        visit[start[0]][start[1]] = 1
        getKey = False
        while q:
            x, y = q.pop(0)

            for i in range(4):
                nx = x + mx[i]
                ny = y + my[i]
                if 0<=nx and nx<M and 0<=ny and ny<N:
                    if visit[nx][ny] == 0 and board[nx][ny] in [0, 2, 3, 4]:
                        visit[nx][ny] = 1
                        q.append((nx, ny))
                        if nx == key[0] and ny == key[1]:
                            getKey = True
                            break

        if not getKey:
            print(0)
            continue

        q = [key]
        visit = [[0]*N for _ in range(M)]
        getTreasure = False
        while q:
            x, y = q.pop(0)

            for i in range(4):
                nx = x + mx[i]
                ny = y + my[i]

                if 0<=nx and nx<M and 0<=ny and ny<N:
                    if visit[nx][ny] == 0 and board[nx][ny] in [0, 2, 3]:
                        visit[nx][ny] = 1
                        q.append((nx, ny))
                        if nx == dest[0] and ny == dest[1]:
                            getTreasure = True
                            break
        
        
        if getTreasure:
            print(1)
        else:
            print(0)





if __name__=="__main__":
    main()