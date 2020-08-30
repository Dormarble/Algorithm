# number에서 가장 큰 숫자를 만들면서 수를 빼는 방법은 
# 1. number의 각 자릿수가 내림차순이 되도록 높은 자릿수의 수부터 제거
# 2. 1로부터 내림차순이 된 number의 가장 낮은 자릿수부터 제거

def solution(number, k):
    stack = []
    
    # 각 자리수가 내림차순이 되도록 수를 앞에서부터 차례로 제거
    # 스택 내부의 수들이 내림차순이 되도록 넣고 빼고를 반복함
    for num in number:
        # 스택의 top(현재 비교할 숫자의 앞에 있는 숫자)이 현재 비교할 자릿수보다 작다면 내림차순이 성립되지 않음
        # 반복문을 돌면서 스택에 있는 현재 비교할 자릿수의 숫자보다 작은 숫자들을 모두 빼냄
        while stack and k>0 and stack[-1] < num:        
            stack.pop()
            k-=1
        stack.append(num)
    
    # 이미 내림차순인 숫자를 뒤에서부터 짜름
    stack = stack[:len(stack)-k]
    
    return ''.join(stack)
print(solution(	"4177252841", 4))
        
            
