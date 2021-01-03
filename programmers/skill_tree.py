# 스킬트리
def solution(skill, skill_trees):
    result = 0
    for skill_tree in skill_trees:
        st = ""
        for s in skill_tree:
            if s in skill:
                st += s
        
        if st == skill[:len(st)]:            
            result += 1

    return result

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))