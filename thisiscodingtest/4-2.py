# 시각
n = int(input())

count = (n+1) * 60 * 60 - 1
result = 0
for i in range(count):
    hour = str(int(i / 3600))
    minute = str(int(i / 60 % 60))
    sec = str(int(i % 60))

    if '3' in hour + minute + sec:
        result += 1
    
print(result)
    