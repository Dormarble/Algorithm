N = input()

dp = [0] * len(N)

if len(N) == 0 or N[0] == '0':
    print(0)
    exit(0)
else:
    dp[0] = 1

if len(N) == 1:
    print(dp[0])
    exit(0)

t = int(N[:2])
if  t == 10 or t==20:
    dp[1] = 1
elif t<=26:
    dp[1] = 2
else: 
    if t % 10 == 0:
        print(0)
        exit(0)
    else:
        dp[1] = 1
for idx in range(2, len(N)):
    if N[idx] != '0':
        dp[idx] = dp[idx-1] % 1000000

    num = int(N[idx-1:idx+1])
    if 10<num and num<=26:
        dp[idx] += dp[idx-2] % 1000000

    if num == 10 or num == 20:
        dp[idx] = dp[idx-2] % 1000000

print(dp[-1] % 1000000)