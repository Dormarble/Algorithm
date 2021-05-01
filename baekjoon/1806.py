import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

front, end = 0, 0
s = arr[0]
shortest = 10000000000

while True:
    if s >= S:
        shortest = min(shortest, end-front+1)
        s -= arr[front]
        front += 1
    else:
        end += 1
        if end == len(arr):
            break
        s += arr[end]
    
if shortest == 10000000000:
    shortest = 0
print(shortest)