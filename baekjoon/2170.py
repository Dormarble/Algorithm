import sys
input = sys.stdin.readline

lines = []
N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    lines.append((a, b))

lines.sort()

end = lines[0][1]
result = lines[0][1] - lines[0][0]
for line in lines[1:]:
    if end < line[0]:
        result += line[1] - line[0]
    elif line[0] <= end and end < line[1]:
        result += line[1] - end
    else:
        continue
    end = line[1]

print(result)