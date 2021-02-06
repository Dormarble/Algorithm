import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [-10e9] * N
dp[0] = arr[0]
for idx, a in enumerate(arr[1:]):
    idx += 1
    if a < 0:
        if dp[idx-1] + a < 0:
            dp[idx] = 0
        else:
            dp[idx] = dp[idx-1] + a
    else:
        dp[idx] = dp[idx-1] + a

if max(arr) < 0:
    print(max(arr))
else:
    print(max(dp))

