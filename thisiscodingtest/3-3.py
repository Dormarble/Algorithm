n, m = map(int, input().split())

mins = []

for i in range(n):
    row = list(map(int, input().split()))
    mins.append(min(row))

print(max(mins))

