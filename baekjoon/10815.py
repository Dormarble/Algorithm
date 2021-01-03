n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

def binary_search(arr, start, end, target):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] == target:
        return 1
    elif arr[mid] < target:
        return binary_search(arr, mid+1, end, target)
    else:
        return binary_search(arr, start, mid-1, target)

for mm in b:
    print(binary_search(a, 0, len(a)-1, mm), end=' ')