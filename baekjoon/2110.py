import sys

input = sys.stdin.readline

N, C = map(int, input().split())

x = []
for _ in range(N):
    x.append(int(input()))
x.sort()

end = x[-1] - x[0]
start = 1
result = 0

while start <= end:
    mid = (start + end) // 2
    value = x[0]
    count = 1

    for i in range(1, N):
        if x[i] >= value + mid:
            value = x[i]
            count += 1
    
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid -1

print(result)
    