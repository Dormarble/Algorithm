def solution(n, lost, reserve):
    answer = 0
    
    student = [1] * n
    for i in lost:
        student[i-1] -= 1
    for i in reserve:
        student[i-1] += 1

    for i in range(n):
        if student[i] == 0:
            if i-1 >= 0:
                if student[i-1] > 1:
                    answer+=1
                    student[i-1] -= 1
                    continue
            if i+1 < n:
                if student[i+1] > 1:
                    student[i+1] -= 1
                    answer+=1
                    continue
        if student[i] >= 1:
            answer += 1
    return answer

print(solution(5, [2, 4], [1, 3, 5]))