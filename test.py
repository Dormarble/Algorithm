def solution(tickets):
    s = set()
    path = []
    for ticket in tickets:
        s.add(ticket[0])
        s.add(ticket[1]) 
    
    cities = list(s)
    cities.sort()
    
    cityToIdx = {}
    for i, city in enumerate(cities):
        cityToIdx[city] = i
    print(cityToIdx)
    adjList = createAdjList(tickets, cityToIdx)
    


    dfs(cityToIdx["ICN"], adjList, path, 0, len(tickets))
    answer = []
    for i in path:
        answer.append(cities[i])
    return answer

def dfs(city, adjList, path, ticketNum, totalNum):
    path1 = path
    result = True
    if ticketNum == totalNum:
        return path1, True
    path1.append(city)
    isUsed = [0]*len(adjList[city])
    print(city, path1, ticketNum)
    for i, dest in enumerate(adjList[city]):
        if isUsed[i] == 0:
            isUsed[i] = 1 
            path1, d = dfs(dest, adjList, path1, ticketNum+1, totalNum)
            if d :
                result = True
            else:
                path1 = path1[:-2]
                isUsed[i] = 0
                result = False
    return path1, result




def createAdjList(tickets, cityToIdx):
    adjList = []
    for _ in range(len(cityToIdx)):
        adjList.append([])
    for ticket in tickets:
        start = cityToIdx[ticket[0]]
        desti = cityToIdx[ticket[1]]
        
        adjList[start].append(desti)
    
    for arr in adjList:
        arr.sort()
    return adjList


tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
d = solution(tickets)

print(d)