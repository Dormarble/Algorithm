import math

def solution(brown, yellow):
    candidate = []
    for i in range(1, int(math.sqrt(yellow))+1):
        if yellow % i == 0:
            candidate.append(i)
            
    for ver in candidate:
        hor = int(yellow / ver)

        if hor * 2 + (ver+2) * 2 == brown:
            return [hor + 2, ver + 2]


print(solution(24, 24))