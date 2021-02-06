n, k, l = map(int, input().split())

round = 1
while True:
    if abs(k-l) == 1:
        if max(k, l) % 2 == 0:
            break;
    
    k = (k+1) // 2
    l = (l+1) // 2
    round += 1

print(round)