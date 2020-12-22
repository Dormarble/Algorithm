# 왕실의 나이트
c = input()

atoi = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}
x = atoi[c[0]]
y = int(c[1])

mx = [2, 2, -2, -2, 1, -1, 1, -1]
my = [1, -1, 1, -1, 2, 2, -2, -2]

cnt = 0
for i in range(8):
    nx = x + mx[i]
    ny = y + my[i]

    if 1 <= nx and nx <= 8:
        if 1 <= ny and ny <= 8:
            cnt += 1
    
print(cnt)