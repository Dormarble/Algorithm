import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    nm, k, e, m = input().split()
    arr.append((nm, int(k), int(e), int(m)))

arr.sort(key= lambda x: (-x[1], x[2], -x[3], x[0]))

for a in arr:
    print(a[0])