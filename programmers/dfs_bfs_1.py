answer = 0
nums = []
t = 0

def f(depth, result):
    global answer
    if depth == len(nums):
        if result == t:
            answer += 1
    else:
        f(depth+1, result+nums[depth])
        f(depth+1, result-nums[depth])

def solution(numbers, target):
    global answer
    global t
    global nums
    t = target
    nums = numbers   

    f(0, 0)
    return answer


print(solution([1,1,1,1,1], 3))