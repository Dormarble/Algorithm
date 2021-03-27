import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
low, high, s = 0, 0, arr[0]
while True:
    if s > M:
        s -= arr[low]
        low += 1
    elif s == M:
        result += 1
        s -= arr[low]
        low += 1
    else:
        high += 1
        if high >= N:
            break
        s += arr[high]

print(result)