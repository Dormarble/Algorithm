import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

print(arr[K-1])

"""
def quick_selection(arr, k):
    pivot = arr[len(arr) // 2]

    less = []
    equal = []
    than = []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            than.append(i)
        else:
            equal.append(i)
    
    if k < len(less):
        return quick_selection(less, k)
    elif k <= len(less) + len(equal):
        return pivot
    else:
        k -= len(less) + len(equal)
        return quick_selection(than, k)

print(quick_selection(arr, K))"""