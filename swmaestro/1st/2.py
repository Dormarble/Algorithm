P, N, H = map(int, input().split())

ps = [[] for _ in range(P+1)]
for _ in range(N):
    n, t = map(int, input().split())
    if t > H:
        continue
    ps[n].append(t)


for i in range(1,P+1):
    if len(ps[i]) == 0:
        print(str(i) + " " + str(0))
        continue
    dp = [0]*len(ps[i])
    for idx, t in enumerate(ps[i]):
        tmp = [0]
        for x in dp[:idx]:
            if x<=H-t:
                tmp.append(x)
        dp[idx] = max(tmp) + t
    print(str(i) + " " + str(dp[-1]*1000))