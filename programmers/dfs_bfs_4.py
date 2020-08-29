answer = ["ICN"]

def solution(tickets):
    global answer

    tickets = sorted(tickets, key= lambda x: (x[0], x[1]))
    
    dfs(answer[0], tickets, [])
    
    return answer

def dfs(cur, tickets, path):
    global answer
    if len(answer) != 1:
        return
    if not tickets:
        answer += path
        return

    for i, ticket in enumerate(tickets):
        if ticket[0] == cur:
            next = ticket[1]
            tmpTickets = tickets[:i] + tickets[i+1:]
            tmpPath = path + [next]
            dfs(next, tmpTickets, tmpPath)

print(solution(	[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))