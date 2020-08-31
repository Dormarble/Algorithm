def solution(participant, completion):
    dict = {}
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    for c in completion:
        dict[c] -= 1
        if dict[c] == 0:
            del dict[c]
    
    return list(dict.keys())[0]
    
print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))