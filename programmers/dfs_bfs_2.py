isVisited = []
adj = []

def solution(n, computers):
    global isVisited
    global adj
    isVisited = [False] * n
    adj = computers
    
    answer = 0

    for i in range(n):
        if not isVisited[i]:
            answer += 1
            dfs(i)
    
    return answer

def dfs(cur):
    global isVisited
    global adj

    isVisited[cur] = True
    for next in range(len(adj)):
        if adj[cur][next] == 1:
            if not isVisited[next]:
                dfs(next)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))