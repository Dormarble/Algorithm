N = int(input())
arr = list(map(int, input().split()))

def go(arr, s):
    i = 1
    visit = [0] * len(arr)
    cur = s
    visit[s] = 1
    while True:
        r = arr[cur]
        cur += r
        if visit[cur] == 1:
            break
        visit[cur] = 1
        i += 1

    return i+1

result = 0

for i in range(3):
    r = go(arr, i)
    result = max(result, r)

print(result)