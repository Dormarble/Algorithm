N = int(input())

c = []
for i in range(N):
    c.append(list(map(int, input().split())))

for i in range(N-2, -1, -1):
    for j in range(0, i+1):
        c[i][j] = max(c[i+1][j], c[i+1][j+1]) + c[i][j]
    
print(c[0][0])