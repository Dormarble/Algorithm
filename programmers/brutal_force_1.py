def solution(answers):
    p0 = [1, 2, 3, 4, 5]
    p1 = [2, 1, 2, 3, 2, 4, 2, 5]
    p2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = [0] * 3
    for i, a in enumerate(answers):
        if a == p0[i % 5]:
            answer[0] += 1
        if a == p1[i % 8]:
            answer[1] += 1
        if a == p2[i % 10]:
            answer[2] += 1

    mx = max(answer)
    result = []
    for i, s in enumerate(answer):
        if mx == s:
            result.append(i+1)

    return result

print(solution([1,3, 2, 4, 2]))