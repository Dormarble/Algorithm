n = int(input())

answer = -1
count = int(n/5)

for i in range(count, -1, -1):
    remain = n - 5*i

    if remain % 3 == 0:
        answer = i
        break

if answer == -1:
    print(answer)
else:
    answer += int((n-5*answer) / 3)
    print(answer)