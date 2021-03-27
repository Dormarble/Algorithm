from collections import deque

N, K = map(int, input().split())

visit = [0]*100001
visit[N] = 1
q = deque([(N, 0)])
result = 0
while q:
    x, t = q.popleft()
    
    if x == K:
        result = t
        break

    for n in [x-1, x+1, x*2]:
        if 0 <= n and n <= 100000:
            if visit[n] == 0:
                visit[n] = 1
                q.append((n, t+1))
    
print(result)