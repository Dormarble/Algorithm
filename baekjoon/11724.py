N, M = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0]*N
for i in range(N):
    parent[i] = i

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    union_parent(parent, a, b)

for i in range(N):
    find_parent(parent, i)

result = set()
for p in parent:
    result.add(p)

print(len(result))