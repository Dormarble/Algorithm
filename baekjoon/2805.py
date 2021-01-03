n, m = map(int, input().split())
hs = list(map(int, input().split()))

end = max(hs)
start = 0

def binary_search(hs, start, end, target):
    if start > end:
        return end

    mid = (start + end) // 2

    length = 0
    for h in hs:
        if h > mid:
            length += h-mid

    if length == target:
        return mid
    elif length < target:
        return binary_search(hs, start, mid-1, target)
    else:
        return binary_search(hs, mid+1, end, target)


print(binary_search(hs, start, end, m))