n = int(input())
p = list(map(int, input().split()))
m = int(input())
op = list(map(int, input().split()))

p.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

for i in op:
    if binary_search(p, i, 0, n) == None:
        print("no", end=' ')
    else:
        print("yes", end=' ')

