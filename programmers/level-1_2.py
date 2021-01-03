import math

def solution(n):
    
    sqrt = int(math.sqrt(n))
    if math.sqrt(n) == sqrt:
        return (sqrt+1)**2

    return -1

print(solution(3))