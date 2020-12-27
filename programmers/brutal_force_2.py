result = set()

def is_prime(n):
    if n < 2:
        return False
    if n == 2: 
        return True 
    if n % 2 == 0: 
        return False 
    
    for i in range(3, n, 2): 
        if n % i == 0: 
            return False 
    return True


def f(remain_numbers, n):
    global result
    if n != '':
        n = int(n)
    
        if is_prime(n):
            result.add(n)

    if remain_numbers:
        for i, a in enumerate(remain_numbers):
            f(remain_numbers[:i] + remain_numbers[i+1:], str(n)+a)



def solution(numbers):
    global result
    f(numbers, '')

    return len(result)

print(solution('17'))