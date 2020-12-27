n, m = map(int, input().split())
r = list(map(int, input().split()))

mx = max(r)

def binary_search(target, start, end):
    print(start, end)

    if start > end:
        return None
    mid = (start + end) // 2

    sum = 0
    for i in r:
        if i > mid:
            sum += i - mid
    
    if sum == target:
        return mid
    elif sum > target:
        return binary_search(target, mid+1, end)
    else:
        return binary_search(target, start, mid-1)

print(binary_search(m, 0, mx))