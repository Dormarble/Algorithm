def solution(n):
    i = 10
    sum = 0
    while int(n / i) != 0:
        sum += int(n % i / (i/10))
        i *= 10
    sum += int(n % i / (i/10))

    return sum

print(solution(123))