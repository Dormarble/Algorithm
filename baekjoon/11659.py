import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

tot_arr = [0]
for i in arr:
    tot_arr.append(tot_arr[-1] + i)

for _ in range(M):
    i, j = map(int, input().split())
    print(tot_arr[j] - tot_arr[i-1])