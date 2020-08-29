def canChange(w1, w2):
    diff = 0
    for a, b in zip(w1, w2):
        if a != b:
            diff += 1

    if diff == 1:
        return True
    return False

def solution(begin, target, words):
    answer = 0
    q = [begin]

    while True:
        for word1 in q:
            tmpQ = []
            if word1 == target:
                return answer

            for i, word2 in enumerate(words):
                if canChange(word1, word2):
                    del words[i]
                    tmpQ.append(word2)
            
        answer += 1
        q = tmpQ
        if not q:
            return 0
    

    
print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log"]))