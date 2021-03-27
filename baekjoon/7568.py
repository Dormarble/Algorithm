N = int(input())

ws = []
ts = []
for _ in range(N):
    w, t = map(int, input().split())
    ws.append(w)
    ts.append(t)

for i in range(N):
    w = ws[i]
    t = ts[i]
    r = 1
    for j in range(N):
        if w < ws[j] and t < ts[j]:
            r+=1
    
    print(r, end=' ')