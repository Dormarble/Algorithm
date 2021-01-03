from itertools import combinations
from collections import deque

n, m = map(int, input().split())
chicken = []
house = []
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))


def get_chicken_range(house, chicken):
    mx = [0, 0, 1, -1]
    my = [1, -1, 0, 0]
    
    r = 0
    for hx, hy in house:
        hm = 10e9
        for cx, cy in chicken:
            hm = min(hm, abs(cx-hx) + abs(cy-hy))
        r += hm
    return r
            
        
result = 10e9
for chicken in (list(combinations(chicken, m))):
    result = min(result, get_chicken_range(house, chicken))

print(result)